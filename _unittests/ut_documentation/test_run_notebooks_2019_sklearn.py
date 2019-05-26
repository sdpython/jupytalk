# -*- coding: utf-8 -*-
"""
@brief      test log(time=22s)
"""

import sys
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
import jyquickhelper
import jupytalk


class TestRunNotebooks2019_sklearn(unittest.TestCase):

    def test_notebook_sklearn(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(jupytalk is not None)
        self.assertTrue(jyquickhelper is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "2019", "sklearn")
        test_notebook_execution_coverage(
            __file__, "sklearn", folder, 'jupytalk', copy_files=[], fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
