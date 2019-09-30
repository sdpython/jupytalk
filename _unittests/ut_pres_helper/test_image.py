# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest
import numpy
from pyquickhelper.pycode import ExtTestCase
from jupytalk.pres_helper import show_images


class TestPresHelperImage(ExtTestCase):

    def test_show_images(self):
        this = os.path.abspath(os.path.dirname(__file__))
        img = os.path.join(this, "data", "wiki.jpg")
        ax = show_images(img, title1="a")
        self.assertNotEmpty(ax)
        ax = show_images(img, img, title1="a", title2="b")
        self.assertNotEmpty(ax)
        self.assertEqual(ax.shape, (2, ))


if __name__ == "__main__":
    unittest.main()
