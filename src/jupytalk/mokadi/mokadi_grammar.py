"""
@file
@brief Helpers with grammar for mokadi.
"""
from .mokadi_parser import get_tree_string, parse_mokadi, run_parse
from .mokadi_exceptions import MokadiException
from .MokadiGrammarParser import MokadiGrammarParser


def interpret(sentance):
    """
    Interpret a sentance and returns a list of word.

    @param      sentance        any string
    @return                     list of tuple (word, kind)
    """
    parser = parse_mokadi(sentance)
    stdout, stderr, tree = run_parse(parser)
    if stderr and len(stderr) > 0:
        raise MokadiException(
            "Unable to parse '{0}'\nOUT\n{1}\nERR\n{2}".format(sentance, stdout, stderr))
    res, simple = get_tree_string(tree, MokadiGrammarParser, sentance)
    return simple
