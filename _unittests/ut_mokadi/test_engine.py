#-*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder
from src.jupytalk.mokadi import MokadiEngine, MokadiMessage, MokadiInfo


class TestEngine(unittest.TestCase):

    def test_engine_simple(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_engine_simple")
        clog = CustomLog(temp)
        engine = MokadiEngine(temp, clog)
        mes = MokadiMessage("nokadi", 1)
        res = list(engine.process(mes))
        self.assertEqual(len(res), 1)
        self.assertTrue(isinstance(res[0], MokadiInfo))
        fLOG(res[0])


if __name__ == "__main__":
    unittest.main()
