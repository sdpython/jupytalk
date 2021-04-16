# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup
from pyquicksetup import read_version, read_readme, default_cmdclass
from distutils.core import Command

#########
# settings
#########

project_var_name = "jupytalk"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = project_var_name + ', first name, last name'
DESCRIPTION = """Material for presentations. The documentation generation is using pyquickhelper."""


CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######


class SetupCommandBuildScript(Command):
    description = "Updates grammars."

    user_options = [
        ('g=', None, 'grammar file to recompile, R.g4 for example)')
    ]

    def initialize_options(self):
        self.g = None

    def finalize_options(self):
        pass

    def run(self):
        if self.g is None:
            raise RuntimeError(
                "Expecting a grammar file: python setup.py update_grammars R.g4")
        grammar = self.g
        from pyensae.languages import build_grammar
        if not os.path.exists(grammar):
            cdir = os.path.abspath(os.path.dirname(__file__))
            g2 = os.path.join(cdir, "src", "jupytalk",
                              "mokadi", "grammars", grammar)
            if not os.path.exists(g2):
                raise FileNotFoundError("{0}\n{1}".format(grammar, g2))
            grammar = g2
        try:
            from pyensae.languages import build_grammar
        except ImportError:
            sys.path.append(os.path.join(
                os.path.dirname(__file__), "..", "pyensae", "src"))
            from pyensae.languages import build_grammar
        build_grammar(grammar, fLOG=logging_function)


packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".mokadi.grammars": ["*.g4", "*.tokens"],
                project_var_name + ".mokadi.data": ["*.wav", "*.ico"]}
command = default_cmdclass().copy()
command['update_grammars'] = SetupCommandBuildScript


setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name, subfolder='src'),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/jupytalk/helpsphinx/index.html",
    download_url="https://github.com/sdpython/jupytalk",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=command,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=["pyquicksetup"],
    install_requires=[
        'pyquickhelper>=1.10', 'jyquickhelper',
        'cpyquickhelper>=0.2.226'
    ],
)
