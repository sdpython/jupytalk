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
