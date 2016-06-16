
.. _l-pydata2016:

PyData 06/14/2016 in Paris
==========================


Main presentation

* :ref:`10plottinglibrariesrst`

A couple of notebooks requires to be run to see the results because
a naive conversion does not take into account javascript dependencies
(pythreejs, vega, brython) or does not work at all because
it involves a server (bqplot).

**Static libraries**

* :ref:`imbasemaprst`
* :ref:`imbiopythonrst`
* :ref:`imete3rst`
* :ref:`imlifelinesrst`
* :ref:`immatplotlibrst`
* :ref:`immissingnorst`
* :ref:`imnetworkxrst`
* :ref:`imreportlabrst`
* :ref:`imseabornrst`

**Interactive libraries**

* :ref:`jsbokehrst`
* :ref:`jslightningpythonrst`
* :ref:`jsmpld3rst`
* :ref:`jsplotlyrst`
* :ref:`jspydymassspringdamperrst`
* :ref:`jspygalrst`
* :ref:`jspythreejsrst`
* :ref:`jsvegarst`

**Pure javascript**

* :ref:`jsonlytreantrst`

**Big Data**

* :ref:`bigdatashaderrst`

**GUI**

* :ref:`guigeoplotlibrst`

**Mix between Python and Javascript**

* :ref:`pyjsbqplotrst`
* :ref:`pyjsbrythonrst`
* :ref:`pyjscvispyrst`

**Not covered by this presentation**

* `vaex <https://www.astro.rug.nl/~breddels/vaex/>`_: the speaker just after me and the library is able
  to cope with bug data at a very high scale
* `graphviz <http://www.graphviz.org/>`_: famous library to draw graph, trees.
  I skipped because al the wrappers are not self contained and require to install 
  `graphviz <http://www.graphviz.org/>`_first.
  
**Dig into building a Jupyter extension**

* `Js extensinos <https://carreau.gitbooks.io/jupyter-book/content/Jsextensions.html>`_
* `Distributing Jupyter Extensions as Python Packages <http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html>`_
* `Notebook extensions <https://github.com/jupyter/scipy-advanced-tutorial/blob/master/Part1/04-notebook-extensions.md>`_

**PyData**

The presentation which follows showed how to use
`d3.js <https://d3js.org/>`_. It was amazingly easy and understandable:
*Building Visualisations in d3.js for Python Programmers* by Thomas Parslow.

The talk on `software-carpentry <http://software-carpentry.org>`_ was also quite interesting
as they developed strong experience in animating workshop. I grabbed a couple
of ideas for teachings.
