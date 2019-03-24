# -*- coding: utf-8 -*-
"""
@brief      test log(time=8s)
"""

import sys
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG, CustomLog, run_cmd
from pyquickhelper.pycode.venv_helper import is_virtual_environment
from pyquickhelper.pycode import get_temp_folder, skipif_travis
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut


class TestLONGRunNotebooksPyData2016_im2(unittest.TestCase):

    @skipif_travis("issue with datashader.bokeh_ext, skipping")
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
                lines = [_.lower().strip() for _ in lines if len(_) > 0 and _[
                    0] not in (" ", "-", ".", "-")]
                lines = [
                    _ for _ in lines if "warning" not in _ and not _.startswith("ran ") and _ != "ok"]
                if len(lines) > 0:
                    raise Exception("--CMD:\n{0}\n--OUT:\n{1}\n--ERR\n{2}\n--ERR2\n{3}\n--PP\n{4}".format(
                        cmd, out, err, "\n".join(lines), pp))
            return

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

        os.environ["DISPLAY"] = ":0"

        clog = CustomLog(temp)

        # run the notebooks
        import jupytalk        
        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths,
            detailed_log=clog)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=jupytalk)


if __name__ == "__main__":
    unittest.main()
