#-*- coding: utf-8 -*-
"""
@file
@brief Defines an action for Mokadi.
"""
import os
from .mokadi_action import MokadiAction
from .mokadi_info import MokadiInfo


class MokadiActionSlides(MokadiAction):
    """
    Action.
    """

    def __init__(self, folder):
        """
        Constructor.

        @param      folder      folder where to look for presentation
        """
        self._folder = folder
        if not os.path.exists(folder):
            raise FileNotFoundError(folder)

    def can_do(self, interpreted, message):
        """
        Tells is the class.

        @param      interpreted     interpreted message
        @param      message         message
        @return                     true if the class can process the message
        """
        if len(interpreted) < 2:
            return False
        word = interpreted[1]
        for word in interpreted[1:3]:
            if word[1] == ":presentation:":
                return True
        return False

    def process_interpreted_message(self, interpretation, message):
        """
        Process the interpreted message.

        @param      interpretation      interpretation
        @param      message             original message
        @return                         iterator on Info
        """
        if len(interpretation) == 4:
            if interpretation[1][0] == "liste" and interpretation[2][1] == ":presentation:":
                pres = list(self.enumerate_listdir())
                yield MokadiInfo("ok", "Il y a {0} présentations.".format(len(pres)))
                for name in pres:
                    yield MokadiInfo("ok", name)

    def enumerate_listdir(self):
        """
        Return all presentations in a folder.

        @return         list of presentation
        """
        for name in os.listdir(self._folder):
            if os.path.splitext(name)[-1] == ".pptx":
                yield name
