"""
@file
@brief Simple wrapper for `treant-js <http://fperucic.github.io/treant-js/>`_.
"""
from collections import OrderedDict


def onnx2graph(onnx_model):
    """
    Converts an :epkg:`ONNX` model into a readable graph.

    @param      onnx_model      onnx_model
    @return                     graph defined with :epkg:`OrderedDict`
                                so that it can be processed by epkg:`asciitree`
    """
    vars = {}

    for node in onnx_model.graph.node:
        key = "%s[%s]" % (node.name, node.op_type)
        for inp in node.input:
            if inp not in vars:
                vars[inp] = []
            if key not in vars[inp]:
                vars[inp].append(key)
        vars[key] = []
        for out in node.output:
            if out not in vars[key]:
                vars[key].append(out)

    return edges2asciitree(vars)


def edges2asciitree(edges):
    """
    Converts a set of edges into a combination
    of :epkg:`OrderedDict` which can be understood
    by :epkg:`asciitree`. This does not work if one node
    has multiple inputs.

    @param      edges       set of edges
    @return                 :epkg:`OrderedDict`

    .. runpython::
        :showcode:

        data = {'X': ['LinearClassifier[LinearClassifier]'],
                'LinearClassifier[LinearClassifier]':
                    ['label', 'probability_tensor'],
                'probability_tensor': ['Normalizer[Normalizer]'],
                'Normalizer[Normalizer]': ['probabilities'],
                'label': ['Cast[Cast]'],
                'Cast[Cast]': ['output_label'],
                'probabilities': ['ZipMap[ZipMap]'],
                'ZipMap[ZipMap]': ['output_probability']}

        from jupytalk.talk_examples import edges2asciitree
        res = edges2asciitree(data)

        import pprint
        pprint.pprint(res)

        from asciitree import LeftAligned
        tr = LeftAligned()
        print(tr(res))
    """
    roots = []
    values = []
    for _, eds in edges.items():
        values.extend(eds)
    vs = set(values)
    for key in edges:
        if key not in vs:
            roots.append(key)

    if len(roots) > 1:
        edges = edges.copy()
        edges['root'] = roots
        roots = ['root']

    res = OrderedDict()
    find = {}
    for r in roots:
        res[r] = OrderedDict()
        find[r] = res[r]

    modif = 1
    while modif > 0:
        modif = 0
        for k, eds in edges.items():
            if k in find:
                ord = find[k]
                for edge in eds:
                    if edge not in ord:
                        ord[edge] = OrderedDict()
                        find[edge] = ord[edge]
                        modif += 1

    return res


def docstring2html(doc):
    """
    Converts a doc string into :epkg:`RST`.
    """
    from pyquickhelper.helpgen.rst_converters import docstring2html
    import warnings
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        return docstring2html(doc.replace("Default value is ````", ""))
