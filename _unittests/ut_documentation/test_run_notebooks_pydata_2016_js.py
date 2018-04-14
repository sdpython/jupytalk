# -*- coding: utf-8 -*-
"""
@brief      test log(time=52s)
"""

import sys
import os
import unittest
import shutil


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

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
from pyquickhelper.ipythonhelper import install_python_kernel_for_unittest
import src.jupytalk


class TestRunNotebooksPyData2016_js(unittest.TestCase):

    def test_run_notebook_js(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            return

        kernel_name = None if is_travis_or_appveyor() else install_python_kernel_for_unittest(
            "python3_module_template")

        temp = get_temp_folder(__file__, "temp_run_notebooks_js")

        # selection of notebooks
        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks", "2016", "pydata"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "js_" in f and "pyjs_" not in f and "lightning" not in f:
                if sys.platform.startswith("win") or "plotly" not in f:
                    # plotly requires cufflinks which requires ta-lib which is difficult to install on travis
                    keepnote.append(os.path.join(fnb, f))

        # function to tell that a can be run
        def valid(cell):
            if "open_html_form" in cell:
                return False
            if "open_window_params" in cell:
                return False
            if '<div style="position:absolute' in cell:
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
        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths, kernel_name=kernel_name)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.jupytalk)


if __name__ == "__main__":
    unittest.main()
