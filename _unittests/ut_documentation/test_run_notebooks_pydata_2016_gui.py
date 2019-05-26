# -*- coding: utf-8 -*-
"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
import jyquickhelper
import jupytalk


class TestRunNotebooksPyData2016_gui(unittest.TestCase):

    def test_run_notebook_gui(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            if ".show" in cell:
                return False
            return True

        self.assertTrue(jupytalk is not None)
        self.assertTrue(jyquickhelper is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "2016", "pydata")
        test_notebook_execution_coverage(
            __file__, "gui", folder, 'jupytalk', copy_files=[], fLOG=fLOG,
            valid=valid)


if __name__ == "__main__":
    unittest.main()
