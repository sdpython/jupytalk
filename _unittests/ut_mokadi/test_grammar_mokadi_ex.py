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
        from src.jupytalk.mokadi.grammars import MokadiGrammar_frParser, MokadiGrammar_frLexer, MokadiGrammar_frListener

        codes = ["MOKADI lire mail",  # 1
                 "MOKADI liste presentation",  # 2
                 "MOKADI lire présentation 1 slide 2",  # 3
                 "MOKADI Comment vas-tu ?",  # 4
                 "MOKADI hello",  # 5
                 "MOKADI lire nouvelles",  # 6
                 "MOKADI lire dernières nouvelles",  # 7
                 "MOKADI quelles sont les nouvelles ?",  # 8
                 "MOKADI quelles sont les dernières nouvelles ?",  # 9
                 "MOKADI news",  # 10
                 ]
        expec = [[('MOKADI', ':MOKADI:'), ('lire', ':verb_voir:'), ('mail', ':mails:')],  # 1
                 [('MOKADI', ':MOKADI:'), ('liste', ':verb_voir:'),
                  ('presentation', ':presentation:')],  # 2
                 [('MOKADI', ':MOKADI:'), ('lire', ':verb_voir:'), ('présentation', ':presentation:'),
                  ('1', ':int:'), ('slide', ':slide:'), ('2', ':int:')],  # 3
                 [('MOKADI', ':MOKADI:'), ('Comment', ':word:'), ('vas', ':word:'),
                  ('-', ':op:'), ('tu', ':word:'), ('?', ':question:')],  # 4
                 [('MOKADI', ':MOKADI:'), ('hello', ':word:')],  # 5
                 [('MOKADI', ':MOKADI:'), ('lire', ':verb_voir:'),
                  ('nouvelles', ':news:')],  # 6
                 [('MOKADI', ':MOKADI:'), ('lire', ':verb_voir:'), ('dernières',
                                                                    ':time_indication:'), ('nouvelles', ':news:')],  # 7
                 [('MOKADI', ':MOKADI:'), ('quelles', ':verb_voir:'), ('sont', ':verb_voir:'), ('les', ':stopword:'),
                  ('nouvelles', ':news:'), ('?', ':question_mark:')],  # 8
                 [('MOKADI', ':MOKADI:'), ('quelles', ':verb_voir:'), ('sont', ':verb_voir:'), ('les', ':stopword:'), ('dernières', ':time_indication:'),
                  ('nouvelles', ':news:'), ('?', ':question_mark:')],  # 9
                 [('MOKADI', ':MOKADI:'), ('news', ':news:')],  # 10
                 ]
        expec = [_ + [('<EOF>', ':P:')] for _ in expec]

        for i, code in enumerate(codes):
            fLOG("{0}/{1}: {2}".format(i + 1, len(codes), code))
            try:
                simple = interpret(code, MokadiGrammar_frParser,
                                   MokadiGrammar_frLexer, MokadiGrammar_frListener)
            except SyntaxError as e:
                raise Exception(
                    "Unable to interpret '{0}'".format(code)) from e
            if i >= len(expec):
                raise Exception(simple[:-1])
            self.assertEqual(simple, expec[i])


if __name__ == "__main__":
    unittest.main()
