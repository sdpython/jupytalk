"""
@file
@brief Custom listener for the parser
"""
from .MokadiGrammarParser import MokadiGrammarParser
from .MokadiGrammarListener import MokadiGrammarListener

# This class defines a complete listener for a parse tree produced by
# MokadiGrammarParser.


class MokadiListener(MokadiGrammarListener):

    def __init__(self, *l, **p):
        """
        Constrcutor
        """
        MokadiGrammarListener.__init__(self, *l, **p)
        self._parsed = []

    @property
    def Parsed(self):
        """
        Return the results of the parsed results.
        """
        return self._parsed

    # Enter a parse tree produced by MokadiGrammarParser#parse.
    def enterParse(self, ctx: MokadiGrammarParser.ParseContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#parse.
    def exitParse(self, ctx: MokadiGrammarParser.ParseContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#expression_stmt.
    def enterExpression_stmt(self, ctx: MokadiGrammarParser.Expression_stmtContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#expression_stmt.
    def exitExpression_stmt(self, ctx: MokadiGrammarParser.Expression_stmtContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#expression.
    def enterExpression(self, ctx: MokadiGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#expression.
    def exitExpression(self, ctx: MokadiGrammarParser.ExpressionContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#word_name.
    def enterWord_name(self, ctx: MokadiGrammarParser.Word_nameContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#word_name.
    def exitWord_name(self, ctx: MokadiGrammarParser.Word_nameContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#operator.
    def enterOperator(self, ctx: MokadiGrammarParser.OperatorContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#operator.
    def exitOperator(self, ctx: MokadiGrammarParser.OperatorContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#constant.
    def enterConstant(self, ctx: MokadiGrammarParser.ConstantContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#constant.
    def exitConstant(self, ctx: MokadiGrammarParser.ConstantContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#string_literal.
    def enterString_literal(self, ctx: MokadiGrammarParser.String_literalContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#string_literal.
    def exitString_literal(self, ctx: MokadiGrammarParser.String_literalContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#integer_number.
    def enterInteger_number(self, ctx: MokadiGrammarParser.Integer_numberContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#integer_number.
    def exitInteger_number(self, ctx: MokadiGrammarParser.Integer_numberContext):
        pass

    # Enter a parse tree produced by MokadiGrammarParser#real_number.
    def enterReal_number(self, ctx: MokadiGrammarParser.Real_numberContext):
        pass

    # Exit a parse tree produced by MokadiGrammarParser#real_number.
    def exitReal_number(self, ctx: MokadiGrammarParser.Real_numberContext):
        pass
