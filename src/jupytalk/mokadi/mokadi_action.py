"""
@file
@brief Defines an action for Mokadi.
"""


class MokadiAction:
    """
    Action.
    """

    def __init__(self):
        """
        Constructor.
        """
        pass

    def can_do(self, interpreted, message):
        """
        Tells if the class can process the message.

        @param      interpreted     interpreted message
        @param      message         message
        @return                     true if the class can process the message
        """
        raise NotImplementedError("You should overload this method.")

    def process_interpreted_message(self, interpretation, message):
        """
        Process the interpreted message.

        @param      interpretation      interpretation
        @param      message             original message
        @return                         iterator on Info
        """
        raise NotImplementedError("You should overload this method.")
