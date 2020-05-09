"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
from asciitree import LeftAligned
import numpy as np
from IPython.core.display import HTML
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


class TestSklearn2019(ExtTestCase):

    def test_sklearn_onnx(self):
        from jupytalk.talk_examples.sklearn2019 import edges2asciitree
        data = {'X': ['LinearClassifier[LinearClassifier]'],
                'LinearClassifier[LinearClassifier]':
                    ['label', 'probability_tensor'],
                'probability_tensor': ['Normalizer[Normalizer]'],
                'Normalizer[Normalizer]': ['probabilities'],
                'label': ['Cast[Cast]'],
                'Cast[Cast]': ['output_label'],
                'probabilities': ['ZipMap[ZipMap]'],
                'ZipMap[ZipMap]': ['output_probability']}

        res = edges2asciitree(data)

        tr = LeftAligned()
        v = str(tr(res))

        exp = '''
        X
         +-- LinearClassifier[LinearClassifier]
             +-- label
             |   +-- Cast[Cast]
             |       +-- output_label
             +-- probability_tensor
                 +-- Normalizer[Normalizer]
                     +-- probabilities
                         +-- ZipMap[ZipMap]
                             +-- output_probability
        '''.replace('\n', '').replace(' ', '')
        self.assertEqual(exp, v.replace('\n', '').replace(' ', ''))

    def test_sklearn_onnx_full(self):
        from skl2onnx import to_onnx
        from jupytalk.talk_examples.sklearn2019 import onnx2graph
        data = load_iris()
        X, y = data.data, data.target  # pylint: disable=E1101
        clr = LogisticRegression(
            multi_class="auto", solver="liblinear").fit(X, y)
        model_onnx = to_onnx(clr, X.astype(np.float32))
        res = onnx2graph(model_onnx)
        tr = LeftAligned()
        v = str(tr(res))

        exp = '''
        X
         +-- LinearClassifier[LinearClassifier]
             +-- label
             |   +-- Cast[Cast]
             |       +-- output_label
             +-- probability_tensor
                 +-- Normalizer[Normalizer]
                     +-- probabilities
                         +-- ZipMap[ZipMap]
                             +-- output_probability
        '''.replace('\n', '').replace(' ', '')
        self.assertEqual(exp, v.replace('\n', '').replace(' ', ''))

    def test_doc_full(self):
        from jupytalk.talk_examples.sklearn2019 import onnxdocstring2html
        rst = onnxdocstring2html(onnxdocstring2html.__doc__)
        self.assertIsInstance(rst, HTML)

    def test_sklearn_onnx_rename(self):
        from skl2onnx import to_onnx
        from jupytalk.talk_examples.sklearn2019 import rename_input_output
        data = load_iris()
        X, y = data.data, data.target  # pylint: disable=E1101
        clr = LogisticRegression(
            multi_class="auto", solver="liblinear").fit(X, y)
        model_onnx = to_onnx(clr, X.astype(np.float32))
        model2 = rename_input_output(model_onnx)
        self.assertIn("outputlabel", str(model2))

    def test_profile_graph(self):
        from jupytalk.talk_examples.sklearn2019 import profile_fct_graph

        def plus1(x):
            return x + 1
        ax = profile_fct_graph(lambda: plus1(3), "t", highlights=['plus1'])
        self.assertNotEmpty(ax)


if __name__ == "__main__":
    unittest.main()
