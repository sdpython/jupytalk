"""
@file
@brief Defines a message for mokadi.
"""
from .mokadi_grammar import interpret


class MokadiMessage:
    """
    Defines a message for mokadi.
    """

    def __init__(self, message: str, confidence: float):
        """
        Constructor

        @param      message         message (string)
        @param      confidence
        """
        self._message = message
        self._confidence = confidence

    def __str__(self):
        """
        message to string
        """
        return self._message

    def __repr__(self):
        """
        message to string
        """
        return "MokadiMessage('%s', %f)" % (self._message.replace("'", "\\'"), self._confidence)

    def _repr_html_(self):
        """
        for notebooks
        """
        return "<b>%1.2f<b> <i>%s</i>" % (self._confidence, self._message)

    @property
    def Message(self):
        """
        property
        """
        return self._message

    @property
    def Confidence(self):
        """
        property
        """
        return self._confidence

    def interpret(self, exc=True):
        """
        Interpret the message with the grammar.

        @param      exc     raises an exception if error
        @return             interpretation
        """
        if exc:
            return interpret(self._message)
        else:
            try:
                return interpret(self._message)
            except Exception as e:
                if not hasattr(self, "_errors"):
                    self._errors = []
                self._errors.append(e)
                return e
