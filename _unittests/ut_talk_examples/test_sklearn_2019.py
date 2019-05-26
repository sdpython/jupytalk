"""
@brief      test log(time=35s)
"""

import sys
import os
import unittest
from asciitree import LeftAligned
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
import numpy as np
from IPython.core.display import HTML
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from jupytalk.talk_examples.treant_wrapper import display_treant
from jupytalk.talk_examples.onnx_helper import edges2asciitree, onnx2graph, docstring2html


class TestSklearn2019(ExtTestCase):

    def test_sklearn_onnx(self):
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
        data = load_iris()
        X, y = data.data, data.target
        clr = LogisticRegression(multi_class="auto", solver="liblinear").fit(X, y)
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
        rst = docstring2html(docstring2html.__doc__)
        self.assertIsInstance(rst, HTML)
        
        

if __name__ == "__main__":
    unittest.main()
