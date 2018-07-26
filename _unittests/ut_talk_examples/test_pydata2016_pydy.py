"""
@brief      test log(time=35s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv, ExtTestCase


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

from src.jupytalk.talk_examples.pydata2016 import example_pydy


class TestPyData2016pydy(ExtTestCase):

    def test_example_pydy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_example_pydy")
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        try:
            example_pydy(ax=ax)
        except Exception as e:
            if 'can only concatenate list (not "tuple") to list' in str(e):
                warnings.warn("Pydy needs to be updated for Python 3.7")
                return
            else:
                raise e
        self.assertNotEmpty(ax)
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        self.assertExists(img)
        if __name__ == "__main__":
            fig.show()
        plt.close('all')
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
