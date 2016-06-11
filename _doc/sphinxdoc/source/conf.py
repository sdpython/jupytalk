# -*- coding: utf-8 -*-
import sys
import os
import datetime
import re
import wild_sphinx_theme

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
set_sphinx_variables(__file__, "jupyter", "Xavier Dupré", 2016,
                     "wild", wild_sphinx_theme.get_theme_dir(), locals(),
                     extlinks=dict(issue=('https://github.com/sdpython/jupytalk/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/jupytalk/helpsphinx/"

# https://github.com/pinax/pinax-theme-bootstrap
# https://pypi.python.org/pypi/guzzle_sphinx_theme/0.7.11
# https://pypi.python.org/pypi/hbp-sphinx-theme/0.3.4
# https://pypi.python.org/pypi/oslosphinx/3.2.0
# https://pypi.python.org/pypi/foundation-sphinx-theme/0.0.3
# https://pypi.python.org/pypi/pietroalbini-sphinx-themes/1.3.0
# https://github.com/lucywyman/colorful-hieroglyph-theme
# https://pypi.python.org/pypi/openstackdocstheme/1.3.0
# https://pypi.python.org/pypi/sphinx_theme_pd/0.0.8