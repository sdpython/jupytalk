#-*- coding: utf-8 -*-
"""
@brief      test log(time=8s)
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

from pyquickhelper.loghelper import fLOG, CustomLog, run_cmd
from pyquickhelper.pycode.venv_helper import is_virtual_environment
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
from pyquickhelper.ipythonhelper import install_python_kernel_for_unittest
import src.jupytalk


class TestLONGRunNotebooksPyData2016_im2(unittest.TestCase):

    def test_run_notebook_im2(self):
        """
        If the test does not end, it is probably due to PyQt4 needed by ete3.
        Try ``import PyQt4.QtCore``.
        Try to remove PyQt5, uninstall PyQt4, reinstall it from
        http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4 (Windows).
        """
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            warnings.warn("issue with datashader.bokeh_ext, skipping")
            return

        if is_virtual_environment() and sys.platform.startswith("win"):
            pp = os.environ.get('PYTHONPATH', '')
            if "SECONDTRY" in pp:
                raise Exception(
                    "Not working**EXE\n{0}\n**PP\n{1}\n****".format(sys.executable, pp))
            # We need to run this file with the main python.
            # Otherwise it fails for tables: DLL load failed.
            import numpy
            rootn = os.path.normpath(os.path.join(
                os.path.dirname(numpy.__file__), "..", ".."))
            exe = os.path.normpath(os.path.join(
                rootn, "..", "python.exe"))
            cmd = '"{0}" -u "{1}"'.format(exe, os.path.abspath(__file__))
            import jyquickhelper
            import pyquickhelper
            add = ["SECONDTRY"]
            for mod in [pyquickhelper, jyquickhelper]:
                add.append(os.path.normpath(os.path.join(
                    os.path.dirname(mod.__file__), "..")))
            fLOG("set PYTHONPATH={0}".format(";".join(add)))
            os.environ['PYTHONPATH'] = ";".join(add)
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
            if len(err) > 0:
                lines = err.split("\n")
                lines = [_ for _ in lines if _[0] != " "]
                lines = [_ for _ in lines if "warning" not in _.lower()]
                if len(lines) > 0:
                    raise Exception("--CMD:\n{0}\n--OUT:\n{1}\n--ERR\n{2}\n--ERR2\n{3}\n--PP\n{4}".format(
                        cmd, out, err, "\n".join(lines), pp))
            return

        kernel_name = None if is_travis_or_appveyor() else install_python_kernel_for_unittest(
            "python3_module_template")

        temp = get_temp_folder(__file__, "temp_run_notebooks_im2")

        # selection of notebooks
        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks", "2016", "pydata"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "im_" in f and "ete" in f:
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
        for cop in ["green_tripdata_2015-12_sample.csv",
                    "NYPD_Motor_Vehicle_Collisions_sample.csv",
                    "NYPD_Motor_Vehicle_Collisions_small.csv"]:
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

        clog = CustomLog(temp)

        # run the notebooks
        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths,
            kernel_name=kernel_name, detailed_log=clog)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.jupytalk)


if __name__ == "__main__":
    unittest.main()
