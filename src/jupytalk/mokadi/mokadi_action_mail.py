#-*- coding: utf-8 -*-
"""
@file
@brief Defines an action for Mokadi.
"""
from .mokadi_action import MokadiAction
from .mokadi_info import MokadiInfo
from .mokadi_exceptions import MokadiException
from .mokadi_mails import enumerate_last_mails


class MokadiActionMail(MokadiAction):
    """
    Action. Mail.
    """

    def __init__(self, user, pwd, server, fLOG=None):
        """
        Constructor.

        @param      user        login
        @param      pwd         password
        @param      server      server
        @param      fLOG        logging function
        """
        MokadiAction.__init__(self, fLOG=fLOG)
        self._user = user
        self._pwd = pwd
        self._server = server

    def can_do(self, interpreted, message):
        """
        Tells if the class can process the message.

        @param      interpreted     interpreted message
        @param      message         message
        @return                     true if the class can process the message
        """
        if len(interpreted) < 2:
            return False
        word = interpreted[1]
        for word in interpreted[1:]:
            if word[1] == ":mails:":
                return True
        return False

    def process_interpreted_message(self, interpretation, message):
        """
        Process the interpreted message.

        @param      interpretation      interpretation
        @param      message             original message
        @return                         iterator on Info
        """
        done = False
        if len(interpretation) == 4:
            if interpretation[1][1] == ":verb_voir:" and interpretation[2][1] == ":mails:":
                mails = enumerate_last_mails(
                    self._user, self._pwd, self._server, fLOG=self.fLOG)

                for mail in mails:
                    self.fLOG(mail.get_name(), "**", mail.get_nb_attachements(),
                              "**", mail.get_date_str())
                    h = mail.get_date().hour
                    yield MokadiInfo("ok", "Mail reçu vers {0} heures de {1}.".format(h, mail.get_name()))
                    yield MokadiInfo("ok", mail.get_field("subject").split("\n")[0])
                    nb = mail.get_nb_attachements()
                    if nb > 0:
                        yield MokadiInfo("ok", "Ce mail a {0} pièces jointes.".format(nb))

                done = True
        if not done:
            raise MokadiException(
                "Unable to interpret '{0}'\n{1} - {2}.".format(message, len(interpretation), interpretation))
