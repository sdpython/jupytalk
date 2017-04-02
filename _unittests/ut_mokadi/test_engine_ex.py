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

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.jupytalk.mokadi import MokadiEngine, MokadiMessage
from src.jupytalk.mokadi.mokadi_action_slides import MokadiActionSlides
from src.jupytalk.mokadi.mokadi_action_conversation import MokadiActionConversation


class TestEngineExtended(unittest.TestCase):

    def test_engine_ex(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        messages = ["MOKADI liste presentation",
                    "MOKADI lire presentation 1 slide 2",
                    "MOKADI hello"]

        temp = get_temp_folder(__file__, "temp_engine_ex")
        clog = fLOG
        folder = os.path.join(temp, "..", "data")

        actions = [MokadiActionSlides(folder, fLOG=fLOG),
                   MokadiActionConversation(fLOG=fLOG),
                   ]

        engine = MokadiEngine(temp, clog, actions=actions)
        verif = 0
        for i, text in enumerate(messages):
            fLOG("***", text)
            mes = MokadiMessage(text, 1)
            res = list(engine.process(mes, exc=True))
            fLOG(res)
            self.assertTrue(len(res) > 0)
            if i == 2:
                self.assertEqual(len(res), 1)
                self.assertTrue(res[0].HasSound)
                verif += 1
        self.assertTrue(verif > 0)


if __name__ == "__main__":
    unittest.main()
