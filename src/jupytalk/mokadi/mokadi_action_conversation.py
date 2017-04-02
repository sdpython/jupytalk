#-*- coding: utf-8 -*-
"""
@file
@brief Defines an action for Mokadi.
"""
import os
from .mokadi_action import MokadiAction
from .mokadi_info import MokadiInfo
from .mokadi_exceptions import MokadiException


class MokadiActionConversation(MokadiAction):
    """
    Action. Conversation.
    """

    _sounds = {"hello": os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "hello.wav"),
               }

    def __init__(self, fLOG=None):
        """
        Constructor.

        @param      folder      folder where to look for presentation
        @param      fLOG        logging function
        """
        MokadiAction.__init__(self, fLOG=fLOG)

    def can_do(self, interpreted, message):
        """
        Tells if the class can process the message.

        @param      interpreted     interpreted message
        @param      message         message
        @return                     true if the class can process the message
        """
        if len(interpreted) <= 1:
            return False
        res = self.process_interpreted_message(interpreted, message)
        for info in res:
            return True
        return False

    def process_interpreted_message(self, interpretation, message):
        """
        Process the interpreted message.

        @param      interpretation      interpretation
        @param      message             original message
        @return                         iterator on Info
        """
        sentance = [w[0].lower() for w in interpretation[1:3]]
        if sentance[0] in {"hello", "bonjour"}:
            yield MokadiInfo("ok", "hello", sound=MokadiActionConversation._sounds["hello"])
        else:
            raise MokadiException(
                "Unable to answer to '{0}'.".format(sentance))
