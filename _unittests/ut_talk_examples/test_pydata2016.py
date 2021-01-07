"""
@brief      test log(time=35s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv, ExtTestCase
from jupytalk.talk_examples.pydata2016 import example_networkx, example_confidence_interval, example_cartopy


class TestPyData2016(ExtTestCase):

    def test_example_networkx(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        try:
            import cairo
        except ImportError as e:
            warnings.warn("Unable to import cairo %r." % e)
            return
        temp = get_temp_folder(__file__, "temp_example_networkx")
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        example_networkx(ax=ax)
        assert ax is not None
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        self.assertExists(img)
        if __name__ == "__main__":
            fig.show()
        plt.close('all')
        fLOG("end")

    def test_example_confidence_interval(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        try:
            import cairo
        except ImportError as e:
            warnings.warn("Unable to import cairo %r." % e)
            return
        temp = get_temp_folder(__file__, "temp_example_networkx")
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        example_confidence_interval(ax=ax)
        assert ax is not None
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        self.assertExists(img)
        if __name__ == "__main__":
            fig.show()
        plt.close('all')
        fLOG("end")

    def test_example_cartopy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        try:
            import cairo
        except ImportError as e:
            warnings.warn("Unable to import cairo %r." % e)
            return
        temp = get_temp_folder(__file__, "temp_example_networkx")
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        example_cartopy(ax=ax)
        assert ax is not None
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        self.assertExists(img)
        if __name__ == "__main__":
            fig.show()
        plt.close('all')
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
