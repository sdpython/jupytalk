"""
@file
@brief Defines results for mokadi.
"""
import os


class MokadiInfo:
    """
    Defines results for mokadi.
    """

    _allowed_status = {"error", "ok", "empty"}

    def __init__(self, status: str, info: str, error: str, image):
        """
        Constructor

        @param      status          message (string)
        @param      info            text to display
        @param      error           error message
        @param      image           image name
        """
        self._status = status
        self._info = info
        self._error = error
        self._image = image

        if not isinstance(status, str):
            raise TypeError("status must be a string")
        if not isinstance(info, str):
            raise TypeError("info must be a string")
        if not isinstance(error, str):
            raise TypeError("error must be a string")
        if status not in MokadiInfo._allowed_status:
            raise ValueError("status must be in {0}".format(
                MokadiInfo._allowed_status))
        if image is not None and len(image) > 0:
            if not os.path.exists(image):
                raise FileNotFoundError(image)

    def __str__(self):
        """
        message to string
        """
        if self._error:
            return "%s - %s" % (self._status, self._error)
        else:
            return "%s - %s" % (self._status, self._info)

    def __repr__(self):
        """
        message to string
        """
        return "MokadiInfo('%s', '%s', '%s')" % (self._status, self._info.replace("'", "\\'"), self._error.replace("'", "\\'"))

    def _repr_html_(self):
        """
        for notebooks
        """
        if self._status == "ok":
            if self._image:
                return "<i>%s</i><br /><img src=\"%s\" />" % (self._info, self._image)
            else:
                return "<i>%s</i>" % self._info
        else:
            return "<b>%s<b> <i>%s</i>" % (self._status, self._info)

    @property
    def Info(self):
        """
        property
        """
        return self._info

    @property
    def Status(self):
        """
        property
        """
        return self._status
