# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest
import numpy
from pyquickhelper.pycode import ExtTestCase
from jupytalk.benchmark import timeexec, make_dataframe


class TestTimeExec(ExtTestCase):

    def test_timeexec(self):
        code = "3 * 45535266234653452"
        res = timeexec("multiplication", code, verbose=False)
        self.assertIn("legend", res)
        self.assertIn("deviation", res)

    def test_make_dataframe(self):
        df = make_dataframe([0, 1], [numpy.zeros((2, 3)), numpy.ones((2, 1))])
        self.assertEqual(df.shape, (2, 5))
        self.assertEqual(list(df.columns),
                         ["Label", "F0_0", "F0_1", "F0_2", "F1_0"])
        df = make_dataframe([0, 1], numpy.zeros((2, 3)))
        self.assertEqual(df.shape, (2, 4))
        self.assertEqual(list(df.columns), ["Label", "F0", "F1", "F2"])


if __name__ == "__main__":
    unittest.main()
