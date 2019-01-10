# -*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version


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


class TestLONGFunctionTestNotebook2018msexpONNX(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["jyquickhelper", "pymyinstall"], __file__, hide=True)

    def test_notebook_msexp_onnx(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import pymyinstall
        self.assertTrue(src.jupytalk is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "2018", "msexp")
        files = [_ for _ in os.listdir(
            folder) if '.png' in _ or '.csv' in _ or '.jpg' in _]
        test_notebook_execution_coverage(__file__, "onnx", folder,
                                         this_module_name="jupytalk", fLOG=fLOG,
                                         copy_files=files, modules=[pymyinstall])


if __name__ == "__main__":
    unittest.main()
