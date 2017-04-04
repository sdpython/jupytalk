# -*- coding: utf-8 -*-
"""
@file
@brief Tkinter application for Mokadi
"""
import tkinter
import tkinter.ttk as ttk
import tkinter.scrolledtext as ScrolledText
import os
import threading
from queue import Queue
from PIL import Image, ImageTk
from pyquickhelper.loghelper import CustomLog, fLOG
from .grammars import MokadiGrammar_frParser, MokadiGrammar_frLexer, MokadiGrammar_frListener
from . import MokadiEngine, MokadiMessage
from .mokadi_action_conversation import MokadiActionConversation
from .mokadi_action_emotion import MokadiActionEmotion
from .mokadi_action_mail import MokadiActionMail
from .mokadi_action_news import MokadiActionNews
from .mokadi_action_slides import MokadiActionSlides
from .mokadi_record import play_speech, record_speech
from .mokadi_speak import speak
from .cognitive_services_helper import call_api_speech_reco
from .mokadi_picture import take_picture


class ThreadSpeech(threading.Thread):

    def __init__(self, win, subkey):
        threading.Thread.__init__(self)
        self.win = win
        self.subkey = subkey

    def run(self):
        speech = record_speech()
        reco = call_api_speech_reco(self.subkey, memwav=speech)
        print(reco)
        if "results" not in reco:
            reco = "erreur 1", 1
        else:
            results = reco["results"]
            if len(results) != 1:
                reco = "erreur 2", 1
            else:
                res = results[0]
                if "lexical" not in res:
                    reco = "erreur 3", 1
                else:
                    conf = res["confidence"]
                    reco = res["lexical"], conf

        self.win.queue.put_nowait(reco)
        self.win.event_generate("<<thread_fini>>")


class TkinterMokadi(tkinter.Frame):
    """
    Defines a frame.
    """

    def __init__(self, parent, mokadi, speak=False, subkey_speech=None, fLOG=fLOG):
        """
        Constructor.

        @param      parent          a frame
        @param      mokadi          the bot @see cl MokadiEngine
        @param      speak           speak the answer and not just display it
        @param      subkey_speech   key for the speech
        @param      fLOG            logging function
        """
        tkinter.Frame.__init__(self, parent)
        self._mokadi = mokadi
        self._speak = speak
        self._subkey_speech = subkey_speech
        self.initialize()
        self.fLOG = fLOG
        self.queue = Queue()

    def initialize(self):
        """
        Initialisation.
        """
        self.grid()
        self.subframe1 = tkinter.Frame(self)
        self.subframe2 = tkinter.Frame(self)
        self.subframe1.grid(column=0, row=0)
        self.subframe2.grid(column=1, row=0)

        self.respond = ttk.Button(
            self.subframe1, text='Demander', command=self.get_response)
        self.respond.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)
        self.respond.config(width=5)

        self.usr_input = ttk.Entry(self.subframe1, state='normal')
        self.usr_input.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)
        self.usr_input.bind("<Return>", self.bound_enter)
        self.usr_input.config(width=5)

        self.conversation_lbl = ttk.Label(
            self.subframe1, anchor=tkinter.E, text='Conversation')
        self.conversation_lbl.grid(
            column=0, row=1, sticky='nesw', padx=3, pady=3)
        self.conversation_lbl.config(width=50)

        self.conversation = ScrolledText.ScrolledText(
            self.subframe1, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2,
                               sticky='nesw', padx=3, pady=3)
        self.conversation.config(width=50)
        self.bind("<<thread_fini>>", self.receive_speech)
        self._waiting = False

    def bound_enter(self, *l):
        """
        Returned was pressed.
        """
        self.get_response()

    def get_response(self):
        """
        Get the text in the message box.
        Retrieve the answer.
        """
        if self._waiting:
            self.fLOG("[TkinterMokadi] already waiting")
            return
        user_text = self.usr_input.get()
        self.usr_input.delete(0, tkinter.END)

        if len(user_text) == 0:
            # We record the speech instead.
            self.start_speech_recording()
        else:
            user_input = MokadiMessage("MOKADI " + user_text, 1)
            self.process(user_input)

    def start_speech_recording(self):
        """
        Launches a thread which record the speech.
        """
        self.conversation_lbl.config(text='Parlez (< 5s) et attendez.')
        self.conversation_lbl.update_idletasks()
        self._waiting = True
        th = ThreadSpeech(self, self._subkey_speech)
        th.run()

    def receive_speech(self, *l):
        """
        Reveices the recognized speech.
        """
        self.conversation_lbl.config(text='Conversation')
        self.conversation_lbl.update_idletasks()

        data = self.queue.get()
        self.queue.task_done()
        self._waiting = False

        if isinstance(data, tuple):
            data = data[0]

        self.usr_input.insert(0, data)
        self.usr_input.event_generate("<Return>")

    def process(self, user_input):
        """
        Process an input.

        @param      user_input      user input
        """
        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tkinter.END, "\n\nVous : " + user_input.message)
        iter = self._mokadi.process(user_input, exc=False)
        self.fLOG("[TkinterMokadi] sent:", user_input)

        for info in iter:
            speakable = []

            self.fLOG("[TkinterMokadi] received:", info,
                      info.has_sound, info.has_image)

            if info.status == "ok":
                if info.has_sound:
                    play_speech(info.sound)
                elif info.has_image:
                    if isinstance(info.image, str) and not info.image.startswith("http"):
                        monimage = Image.open(info.image)
                        photo = ImageTk.PhotoImage(monimage)
                        label = tkinter.Label(self.subframe2, image=photo)
                        label.image = photo
                        label.grid(column=1, row=0)
                if info.info:
                    self.conversation.insert(
                        tkinter.END, "\nMokadi : " + info.info)
                    if not info.has_sound:
                        speakable.append(info.info)
            elif info.status == "error":
                self.conversation.insert(
                    tkinter.END, "\nMokadi : " + info.info)
                speakable.append(info.info)

            if self._speak and len(speakable) > 0:
                for text in speakable:
                    speak(text)

        self.conversation['state'] = 'disabled'
        self.conversation.see(tkinter.END)


def gui_mokadi(fLOG=None, folder_slides=None):
    """
    Launches the application.

    There is a bug somewhere. Taking a picture fails if the vocal synthesis
    runs first. We need to take a picture first.
    """
    take_picture()
    import keyring
    user = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "user")
    pwd = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "pwd")
    server = "imap.gmail.com"
    subkey_news = keyring.get_password(
        "cogser", os.environ["COMPUTERNAME"] + "news")
    subkey_emo = keyring.get_password(
        "cogser", os.environ["COMPUTERNAME"] + "emotions")
    subkey_speech = keyring.get_password(
        "cogser", os.environ["COMPUTERNAME"] + "voicereco")

    if folder_slides is None:
        folder_slides = os.path.abspath(os.path.dirname(__file__))
        folder_slides = os.path.join(folder_slides, "demo")

    folder = os.path.abspath("temp_mokadi_folder")
    if not os.path.exists(folder):
        os.mkdir(folder)
    clog = CustomLog(folder)

    actions = [MokadiActionSlides(folder=folder_slides, fLOG=fLOG),
               MokadiActionMail(user=user, pwd=pwd, server=server, fLOG=fLOG),
               MokadiActionNews(subkey_news, fLOG=fLOG),
               MokadiActionEmotion(subkey_emo, folder, fLOG=fLOG),
               MokadiActionConversation(fLOG=fLOG),
               ]

    engine = MokadiEngine(folder, clog, actions, MokadiGrammar_frParser,
                          MokadiGrammar_frLexer, MokadiGrammar_frListener)

    tk = tkinter.Tk()
    tk.iconbitmap(os.path.join(os.path.dirname(__file__), 'project_ico.ico'))
    tk.title("Mokadi")
    TkinterMokadi(tk, engine, speak=True, subkey_speech=subkey_speech)
    tk.mainloop()
