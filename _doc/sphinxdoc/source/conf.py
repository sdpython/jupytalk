# -*- coding: utf-8 -*-
import sys
import os
import pydata_sphinx_theme
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "jupytalk", "Xavier Dupré", 2021,
                     "pydata_sphinx_theme", pydata_sphinx_theme.get_html_theme_path(),
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/jupytalk/issues/%s', 'issue')),
                     github_user="sdpython", github_repo="jupytalk", book=True, nblayout='table')

html_theme_options = {
    'navbar_title': "BASE",
    'navbar_site_name': "Site",
    'navbar_links': [
        ("XD", "http://www.xavierdupre.fr", True),
        ("blog", "blog/main_0000.html", True),
        ("index", "genindex"),
    ],
    'navbar_sidebarrel': True,
    'navbar_pagenav': True,
    'navbar_pagenav_name': "Page",
    'bootswatch_theme': "readable",
    'bootstrap_version': "3",
    'source_link_position': "footer",
}

blog_root = "http://www.xavierdupre.fr/app/jupytalk/helpsphinx/"
blog_background = False
pygments_style = 'default'
html_css_files = ['my-styles.css']

# https://github.com/peterhudec/foundation-sphinx-theme
# http://docs.guzzlephp.org/en/latest/
# http://sphinx-better-theme.readthedocs.io/en/latest/

epkg_dictionary.update({
    'asciitree': 'https://github.com/mbr/asciitree',
    'cartopy': 'https://scitools.org.uk/cartopy/docs/latest/',
    'Custom Extensions to ML.net': 'http://www.xavierdupre.fr/app/machinelearningext/helpsphinx/index.html',
    'C#': 'https://fr.wikipedia.org/wiki/C_sharp',
    'CNTK': 'https://github.com/Microsoft/CNTK',
    'ensae_teaching_cs': 'http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html',
    'jupytalk': 'http://www.xavierdupre.fr/app/jupytalk/helpsphinx/index.html',
    'Microsoft': 'https://docs.microsoft.com/en-us/',
    'ML.net': "https://github.com/dotnet/machinelearning",
    'networkx': "https://networkx.github.io/",
    'nimbusml': 'https://docs.microsoft.com/en-us/nimbusml/overview',
    'onnx': "https://github.com/onnx/onnx",
    'ONNX': "https://onnx.ai/",
    'onnxmltools': "https://github.com/onnx/onnxmltools",
    'onnxruntime': "https://docs.microsoft.com/en-us/python/api/overview/azure/onnx/intro",
    'OrderedDict': 'https://docs.python.org/3/library/collections.html#collections.OrderedDict',
    'pydy': "https://github.com/pydy/pydy",
    'pytorch': 'https://pytorch.org/',
    'quizlet': 'https://quizlet.com/fr-fr',
    'RenderJsDot': 'http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/jyquickhelper/jspy/render_nb_js_dot.html?highlight=renderjsdot#jyquickhelper.jspy.render_nb_js_dot.RenderJsDot',
    'seaborn': "https://seaborn.pydata.org/",
    'sklearn-onnx': 'https://github.com/onnx/sklearn-onnx',
    'xavierdupre.fr': 'http://www.xavierdupre.fr/',
})
