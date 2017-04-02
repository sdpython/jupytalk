#-*- coding: utf-8 -*-
"""
@brief      test log(time=5s)
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


class TestGrammarMokadiExtended(unittest.TestCase):

    def test_mokadi_interpret_long_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.jupytalk.mokadi import interpret

        codes = ["MOKADI fetch mail",
                 "MOKADI liste presentation",
                 "MOKADI lire présentation 1 slide 2",
                 "MOKADI Comment vas-tu ?",
                 "MOKADI hello",
                 ]
        expec = [[('MOKADI', ':MOKADI:'), ('fetch', ':word:'), ('mail', ':word:')],
                 [('MOKADI', ':MOKADI:'), ('liste', ':verb:'),
                  ('presentation', ':presentation:')],
                 [('MOKADI', ':MOKADI:'), ('lire', ':verb:'), ('présentation', ':presentation:'),
                  ('1', ':int:'), ('slide', ':slide:'), ('2', ':int:')],
                 [('MOKADI', ':MOKADI:'), ('Comment', ':word:'), ('vas', ':word:'),
                  ('-', ':op:'), ('tu', ':word:'), ('?', ':question:')],
                 [('MOKADI', ':MOKADI:'), ('hello', ':word:')],
                 ]
        expec = [_ + [('<EOF>', ':P:')] for _ in expec]

        for i, code in enumerate(codes):
            fLOG("{0}/{1}: {2}".format(i + 1, len(codes), code))
            simple = interpret(code)
            self.assertEqual(simple, expec[i])


if __name__ == "__main__":
    unittest.main()
