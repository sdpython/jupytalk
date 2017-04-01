# -*- coding: utf-8 -*-
"""
@file
@brief Make Mokadi's engine.
"""
import os
import random
from pyquickhelper.loghelper import CustomLog
from .mokadi_message import MokadiMessage
from .mokadi_info import MokadiInfo


class MokadiEngine:
    """
    Defines results for mokadi.
    """

    _messages = {"dontunderstand": ["Je n'ai pas compris.", "Parlez vous mokadi?"],
                 "failure": ["Un imprévu s'est produit.", "Grosse tuile"]}

    @staticmethod
    def peak_random(mes: list):
        """
        Pick a random message

        @param      mes     list of strings
        @return             one string
        """
        i = random.randint(0, len(mes) - 1)
        return mes[i]

    def __init__(self, root, clog: CustomLog):
        """
        Constructor

        @param      root        root folder
        @param      clog        custom log
        """
        self._clog = clog
        self._root = root

        if not os.path.exists(root):
            raise FileNotFoundError(root)

    def fLOG(self, *l, **p):
        """
        message to string
        """
        self._clog(*l, **p)

    def process(self, message: MokadiMessage):
        """
        Process one message and returns an iterator on @see cl MokadiInfo.

        @param      message     @see cl MokadiMessage
        @return                 iterator on @see cl MokadiInfo
        """
        self.fLOG("[MokadiEngine.process]", message)
        res = message.interpret(exc=False)
        if isinstance(res, Exception):
            info = MokadiInfo("error", MokadiEngine.peak_random(
                MokadiEngine._messages["dontunderstand"]), str(res), None)
            self.fLOG("[MokadiEngine.process]", info)
            yield info
        else:
            try:
                for info in self.process_interpreted_message(res, message):
                    self.fLOG("[MokadiEngine.process]", info)
                    yield info
            except Exception as e:
                info = MokadiInfo("error", MokadiEngine.peak_random(
                    MokadiEngine._messages["failure"]), str(e), None)
                self.fLOG("[MokadiEngine.process]", info)
                yield info

    def process_interpreted_message(self, interpretation, message):
        """
        Process the interpreted message.

        @param      interpretation      interpretation
        @param      message             original message
        @return                         iterator on Info
        """
        raise NotImplementedError("")
