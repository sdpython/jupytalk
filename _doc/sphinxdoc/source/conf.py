# -*- coding: utf-8 -*-
import sys
import os
# import sphinx_readable_theme
import sphinxjp.themes.basicstrap
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "jupytalk", "Xavier Dupré", 2018,
                     # "readable", [sphinx_readable_theme.get_html_theme_path()],
                     "basicstrap", None,
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/jupytalk/issues/%s', 'issue')),
                     github_user="sdpython", github_repo="jupytalk", book=True)

blog_root = "http://www.xavierdupre.fr/app/jupytalk/helpsphinx/"
blog_background = False
html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css'],
}

# https://github.com/peterhudec/foundation-sphinx-theme
# http://docs.guzzlephp.org/en/latest/
# http://sphinx-better-theme.readthedocs.io/en/latest/

epkg_dictionary.update({
    'Custom Extensions to ML.net': 'http://www.xavierdupre.fr/app/machinelearningext/helpsphinx/index.html',
    'C#': 'https://fr.wikipedia.org/wiki/C_sharp',
    'Microsoft': 'https://docs.microsoft.com/en-us/',
    'ML.net': "https://github.com/dotnet/machinelearning",
    'networkx': "https://networkx.github.io/",
    'nimbusml': 'https://docs.microsoft.com/en-us/nimbusml/overview',
    'onnx': "https://github.com/onnx/onnx",
    'ONNX': "https://onnx.ai/",
    'onnxmltools': "https://github.com/onnx/onnxmltools",
    'onnxruntime': "https://docs.microsoft.com/en-us/python/api/overview/azure/onnx/intro",
    'pydy': "https://github.com/pydy/pydy",
    'seaborn': "https://seaborn.pydata.org/",
})
