#-*- coding: utf-8 -*-
"""
@brief      test log(time=52s)
"""

import sys
import os
import unittest
import shutil
import warnings


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
    import jyquickhelper as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "jyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import jyquickhelper as skip__


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
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
from pyquickhelper.pycode import compare_module_version
from pyquickhelper.ipythonhelper import install_python_kernel_for_unittest
import src.jupytalk
import IPython


class TestRunNotebooksPyData2016_lightning_js(unittest.TestCase):

    def test_run_notebook_lightning_js(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        warnings.warn(
            "The unit test relies on lightning-python but it shares the same name as another one. We disable it.")
        return

        if sys.version_info[0] == 2:
            # notebooks are not converted into python 2.7, so not tested
            return

        if compare_module_version(IPython.__version__, "4.0.0") < 0:
            # IPython is not recnt enough
            return

        kernel_name = None if "travis" in sys.executable else install_python_kernel_for_unittest(
            "python3_module_template")

        temp = get_temp_folder(__file__, "temp_run_notebooks_js")

        # selection of notebooks
        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks", "2016", "pydata"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "js_" in f and "lightning" in f:
                keepnote.append(os.path.join(fnb, f))
        assert len(keepnote) > 0

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

        # creation of a kernel
        kernel_name = None if "travis" in sys.executable else install_python_kernel_for_unittest(
            "python3_module_template")

        # run the notebooks
        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths, kernel_name=kernel_name)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.jupytalk)


if __name__ == "__main__":
    unittest.main()
