# -*- coding: utf-8 -*-
"""
@brief      test log(time=52s)
"""

import sys
import os
import unittest
import shutil
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_circleci
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut

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

import src.jupytalk


class TestRunNotebooksPyData2016_js_pydy(unittest.TestCase):

    @skipif_circleci('TypeError: can only concatenate list (not "tuple") to list, revisit that issue later')
    def test_run_notebook_js_pydy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from sklearn.datasets import load_iris
        self.assertTrue(load_iris is not None)
        temp = get_temp_folder(__file__, "temp_run_notebooks_js_pydy")

        # selection of notebooks
        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks", "2016", "pydata"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "js_" in f and "pyjs_" not in f and \
                    "lightning" not in f and "pydy" in f:
                keepnote.append(os.path.join(fnb, f))

        # function to tell that a can be run
        def valid(cell):
            if 'bar.render(path="render.png")' in cell:
                return False
            return True

        # file to copy
        for cop in ["pydy.svg"]:
            fsrc = os.path.join(fnb, cop)
            if os.path.exists(fsrc):
                dest = temp
                shutil.copy(fsrc, dest)

        # additionnal path to add
        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "pyquickhelper", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "jyquickhelper", "src"))
        ]

        keepnote = [_ for _ in keepnote if 'mpld3' not in _]

        # run the notebooks
        try:
            res = execute_notebook_list(
                temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths)
            execute_notebook_list_finalize_ut(
                res, fLOG=fLOG, dump=src.jupytalk)
        except Exception as e:
            if 'can only concatenate list (not "tuple") to list' in str(e):
                warnings.warn("Pydy needs to be updated for Python 3.7")
                return
            else:
                raise e


if __name__ == "__main__":
    unittest.main()
