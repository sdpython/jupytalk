# -*- coding: utf-8 -*-
"""
@file
@brief Tkinter application for Mokadi
"""
import tkinter
import tkinter.ttk as ttk
import tkinter.scrolledtext as ScrolledText
from PIL import Image, ImageTk
import os
from pyquickhelper.loghelper import CustomLog, fLOG
from .grammars import MokadiGrammar_frParser, MokadiGrammar_frLexer, MokadiGrammar_frListener
from . import MokadiEngine, MokadiMessage
from .mokadi_action_conversation import MokadiActionConversation
from .mokadi_action_emotion import MokadiActionEmotion
from .mokadi_action_mail import MokadiActionMail
from .mokadi_action_news import MokadiActionNews
from .mokadi_action_slides import MokadiActionSlides
from .mokadi_record import play_speech
from .mokadi_speak import speak


class TkinterMokadi(tkinter.Frame):
    """
    Defines a frame.
    """

    def __init__(self, parent, mokadi, speak=False, fLOG=fLOG):
        """
        Constructor.

        @param      parent      a frame
        @param      mokadi      the bot @see cl MokadiEngine
        @param      speak       speak the answer and not just display it
        @param      fLOG        logging function
        """
        tkinter.Frame.__init__(self, parent)
        self._mokadi = mokadi
        self._speak = speak
        self.initialize()
        self.fLOG = fLOG

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
            self.subframe1, anchor=tkinter.E, text='Conversation:')
        self.conversation_lbl.grid(
            column=0, row=1, sticky='nesw', padx=3, pady=3)
        self.conversation_lbl.config(width=50)

        self.conversation = ScrolledText.ScrolledText(
            self.subframe1, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2,
                               sticky='nesw', padx=3, pady=3)
        self.conversation.config(width=50)

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
        user_input = MokadiMessage("MOKADI " + self.usr_input.get(), 1)
        self.usr_input.delete(0, tkinter.END)
        self.process(user_input)

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
    """
    import keyring
    user = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "user")
    pwd = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "pwd")
    server = "imap.gmail.com"
    subkey_news = keyring.get_password(
        "cogser", os.environ["COMPUTERNAME"] + "news")
    subkey_emo = keyring.get_password(
        "cogser", os.environ["COMPUTERNAME"] + "emotions")

    if folder_slides is None:
        folder_slides = os.path.abspath(os.path.dirname(__file__))
        folder_slides = os.path.join(folder_slides, "demo")

    folder = os.path.abspath("temp_mokadi_folder")
    if not os.path.exists(folder):
        os.mkdir(folder)
    clog = CustomLog(folder)

    actions = [MokadiActionSlides(folder=folder_slides, fLOG=fLOG),
               MokadiActionConversation(fLOG=fLOG),
               MokadiActionMail(user=user, pwd=pwd, server=server, fLOG=fLOG),
               MokadiActionNews(subkey_news, fLOG=fLOG),
               MokadiActionEmotion(subkey_emo, folder, fLOG=fLOG),
               ]

    engine = MokadiEngine(folder, clog, actions, MokadiGrammar_frParser,
                          MokadiGrammar_frLexer, MokadiGrammar_frListener)

    tk = tkinter.Tk()
    tk.iconbitmap(os.path.join(os.path.dirname(__file__), 'project_ico.ico'))
    tk.title("Mokadi")
    TkinterMokadi(tk, engine, speak=True)
    tk.mainloop()
