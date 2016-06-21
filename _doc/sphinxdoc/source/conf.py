# -*- coding: utf-8 -*-
import sys
import os
import datetime
import re
# import sphinx_readable_theme
import sphinxjp.themes.basicstrap

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables
set_sphinx_variables(__file__, "jupytalk", "Xavier Dupré", 2016,
                     # "readable", [sphinx_readable_theme.get_html_theme_path()],
                     "basicstrap", None,
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/jupytalk/issues/%s', 'issue')),
                     github_user="sdpython", github_repo="jupytalk")

blog_root = "http://www.xavierdupre.fr/app/jupytalk/helpsphinx/"
blog_background = False
html_context = {
    'css_files': ['_static/my-styles.css'],
}

# https://github.com/peterhudec/foundation-sphinx-theme
# http://docs.guzzlephp.org/en/latest/
# http://sphinx-better-theme.readthedocs.io/en/latest/
