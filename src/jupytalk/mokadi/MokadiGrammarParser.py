# Generated from C:\xadupre\__home_\GitHub\jupytalk\src\jupytalk\mokadi\MokadiGrammar.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\37")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4\"\n\4\3\5\3\5\7\5&\n\5\f\5\16")
        buf.write("\5)\13\5\3\6\3\6\3\6\5\6.\n\6\3\7\3\7\3\b\3\b\3\b\5\b")
        buf.write("\65\n\b\3\t\3\t\3\n\5\n:\n\n\3\n\3\n\3\13\5\13?\n\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13F\n\13\3\13\5\13I\n\13\3\13")
        buf.write("\5\13L\n\13\3\13\3\13\3\13\5\13Q\n\13\3\13\5\13T\n\13")
        buf.write("\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\4\3\2\3\6\3\2\t")
        buf.write("\25X\2\26\3\2\2\2\4\32\3\2\2\2\6!\3\2\2\2\b#\3\2\2\2\n")
        buf.write("-\3\2\2\2\f/\3\2\2\2\16\64\3\2\2\2\20\66\3\2\2\2\229\3")
        buf.write("\2\2\2\24S\3\2\2\2\26\27\5\4\3\2\27\30\5\6\4\2\30\31\7")
        buf.write("\2\2\3\31\3\3\2\2\2\32\33\t\2\2\2\33\5\3\2\2\2\34\"\5")
        buf.write("\b\5\2\35\36\7\7\2\2\36\37\5\b\5\2\37 \7\b\2\2 \"\3\2")
        buf.write("\2\2!\34\3\2\2\2!\35\3\2\2\2\"\7\3\2\2\2#\'\5\n\6\2$&")
        buf.write("\5\n\6\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\t")
        buf.write("\3\2\2\2)\'\3\2\2\2*.\7\31\2\2+.\5\16\b\2,.\5\f\7\2-*")
        buf.write("\3\2\2\2-+\3\2\2\2-,\3\2\2\2.\13\3\2\2\2/\60\t\3\2\2\60")
        buf.write("\r\3\2\2\2\61\65\5\22\n\2\62\65\5\24\13\2\63\65\5\20\t")
        buf.write("\2\64\61\3\2\2\2\64\62\3\2\2\2\64\63\3\2\2\2\65\17\3\2")
        buf.write("\2\2\66\67\7\32\2\2\67\21\3\2\2\28:\7\37\2\298\3\2\2\2")
        buf.write("9:\3\2\2\2:;\3\2\2\2;<\7\30\2\2<\23\3\2\2\2=?\7\37\2\2")
        buf.write(">=\3\2\2\2>?\3\2\2\2?@\3\2\2\2@A\7\30\2\2AB\7\26\2\2B")
        buf.write("H\7\30\2\2CE\7\27\2\2DF\7\37\2\2ED\3\2\2\2EF\3\2\2\2F")
        buf.write("G\3\2\2\2GI\7\30\2\2HC\3\2\2\2HI\3\2\2\2IT\3\2\2\2JL\7")
        buf.write("\37\2\2KJ\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\30\2\2NP\7\27")
        buf.write("\2\2OQ\7\37\2\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RT\7\30\2")
        buf.write("\2S>\3\2\2\2SK\3\2\2\2T\25\3\2\2\2\r!\'-\649>EHKPS")
        return buf.getvalue()


class MokadiGrammarParser (Parser):

    grammarFileName = "MokadiGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'MOKADI'", "'mokadie'", "'leocadie'",
                    "'Leocadie'", "'('", "')'", "'+'", "'-'", "'*'", "'/'",
                    "'%'", "'&&'", "'||'", "'=='", "'!='", "'<='", "'>='",
                    "'>'", "'<'", "'.'", "'e'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "Digits", "Identifier",
                     "STRING", "STRING_DOUBLE_QUOTE", "STRING_QUOTE", "LINE_COMMENT",
                     "WS", "Sign"]

    RULE_parse = 0
    RULE_mokadi = 1
    RULE_expression_stmt = 2
    RULE_expression = 3
    RULE_word_name = 4
    RULE_operator = 5
    RULE_constant = 6
    RULE_string_literal = 7
    RULE_integer_number = 8
    RULE_real_number = 9

    ruleNames = ["parse", "mokadi", "expression_stmt", "expression", "word_name",
                 "operator", "constant", "string_literal", "integer_number",
                 "real_number"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    Digits = 22
    Identifier = 23
    STRING = 24
    STRING_DOUBLE_QUOTE = 25
    STRING_QUOTE = 26
    LINE_COMMENT = 27
    WS = 28
    Sign = 29

    def __init__(self, input: TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mokadi(self):
            return self.getTypedRuleContext(MokadiGrammarParser.MokadiContext, 0)

        def expression_stmt(self):
            return self.getTypedRuleContext(MokadiGrammarParser.Expression_stmtContext, 0)

        def EOF(self):
            return self.getToken(MokadiGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_parse

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParse"):
                listener.enterParse(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParse"):
                listener.exitParse(self)

    def parse(self):

        localctx = MokadiGrammarParser.ParseContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.mokadi()
            self.state = 21
            self.expression_stmt()
            self.state = 22
            self.match(MokadiGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MokadiContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_mokadi

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMokadi"):
                listener.enterMokadi(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMokadi"):
                listener.exitMokadi(self)

    def mokadi(self):

        localctx = MokadiGrammarParser.MokadiContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mokadi)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MokadiGrammarParser.T__0) | (1 << MokadiGrammarParser.T__1) | (1 << MokadiGrammarParser.T__2) | (1 << MokadiGrammarParser.T__3))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MokadiGrammarParser.ExpressionContext, 0)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_expression_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression_stmt"):
                listener.enterExpression_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression_stmt"):
                listener.exitExpression_stmt(self)

    def expression_stmt(self):

        localctx = MokadiGrammarParser.Expression_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression_stmt)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MokadiGrammarParser.T__6, MokadiGrammarParser.T__7, MokadiGrammarParser.T__8, MokadiGrammarParser.T__9, MokadiGrammarParser.T__10, MokadiGrammarParser.T__11, MokadiGrammarParser.T__12, MokadiGrammarParser.T__13, MokadiGrammarParser.T__14, MokadiGrammarParser.T__15, MokadiGrammarParser.T__16, MokadiGrammarParser.T__17, MokadiGrammarParser.T__18, MokadiGrammarParser.Digits, MokadiGrammarParser.Identifier, MokadiGrammarParser.STRING, MokadiGrammarParser.Sign]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expression()
                pass
            elif token in [MokadiGrammarParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(MokadiGrammarParser.T__4)
                self.state = 28
                self.expression()
                self.state = 29
                self.match(MokadiGrammarParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def word_name(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(MokadiGrammarParser.Word_nameContext)
            else:
                return self.getTypedRuleContext(MokadiGrammarParser.Word_nameContext, i)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)

    def expression(self):

        localctx = MokadiGrammarParser.ExpressionContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.word_name()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MokadiGrammarParser.T__6) | (1 << MokadiGrammarParser.T__7) | (1 << MokadiGrammarParser.T__8) | (1 << MokadiGrammarParser.T__9) | (1 << MokadiGrammarParser.T__10) | (1 << MokadiGrammarParser.T__11) | (1 << MokadiGrammarParser.T__12) | (1 << MokadiGrammarParser.T__13) | (1 << MokadiGrammarParser.T__14) | (1 << MokadiGrammarParser.T__15) | (1 << MokadiGrammarParser.T__16) | (1 << MokadiGrammarParser.T__17) | (1 << MokadiGrammarParser.T__18) | (1 << MokadiGrammarParser.Digits) | (1 << MokadiGrammarParser.Identifier) | (1 << MokadiGrammarParser.STRING) | (1 << MokadiGrammarParser.Sign))) != 0):
                self.state = 34
                self.word_name()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Word_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MokadiGrammarParser.Identifier, 0)

        def constant(self):
            return self.getTypedRuleContext(MokadiGrammarParser.ConstantContext, 0)

        def operator(self):
            return self.getTypedRuleContext(MokadiGrammarParser.OperatorContext, 0)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_word_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWord_name"):
                listener.enterWord_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWord_name"):
                listener.exitWord_name(self)

    def word_name(self):

        localctx = MokadiGrammarParser.Word_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_word_name)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MokadiGrammarParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(MokadiGrammarParser.Identifier)
                pass
            elif token in [MokadiGrammarParser.Digits, MokadiGrammarParser.STRING, MokadiGrammarParser.Sign]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.constant()
                pass
            elif token in [MokadiGrammarParser.T__6, MokadiGrammarParser.T__7, MokadiGrammarParser.T__8, MokadiGrammarParser.T__9, MokadiGrammarParser.T__10, MokadiGrammarParser.T__11, MokadiGrammarParser.T__12, MokadiGrammarParser.T__13, MokadiGrammarParser.T__14, MokadiGrammarParser.T__15, MokadiGrammarParser.T__16, MokadiGrammarParser.T__17, MokadiGrammarParser.T__18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.operator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_operator

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOperator"):
                listener.enterOperator(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOperator"):
                listener.exitOperator(self)

    def operator(self):

        localctx = MokadiGrammarParser.OperatorContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operator)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MokadiGrammarParser.T__6) | (1 << MokadiGrammarParser.T__7) | (1 << MokadiGrammarParser.T__8) | (1 << MokadiGrammarParser.T__9) | (1 << MokadiGrammarParser.T__10) | (1 << MokadiGrammarParser.T__11) | (1 << MokadiGrammarParser.T__12) | (1 << MokadiGrammarParser.T__13) | (1 << MokadiGrammarParser.T__14) | (1 << MokadiGrammarParser.T__15) | (1 << MokadiGrammarParser.T__16) | (1 << MokadiGrammarParser.T__17) | (1 << MokadiGrammarParser.T__18))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_number(self):
            return self.getTypedRuleContext(MokadiGrammarParser.Integer_numberContext, 0)

        def real_number(self):
            return self.getTypedRuleContext(MokadiGrammarParser.Real_numberContext, 0)

        def string_literal(self):
            return self.getTypedRuleContext(MokadiGrammarParser.String_literalContext, 0)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_constant

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConstant"):
                listener.enterConstant(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConstant"):
                listener.exitConstant(self)

    def constant(self):

        localctx = MokadiGrammarParser.ConstantContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constant)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.integer_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.real_number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.string_literal()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_literalContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MokadiGrammarParser.STRING, 0)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_string_literal

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterString_literal"):
                listener.enterString_literal(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitString_literal"):
                listener.exitString_literal(self)

    def string_literal(self):

        localctx = MokadiGrammarParser.String_literalContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MokadiGrammarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Integer_numberContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digits(self):
            return self.getToken(MokadiGrammarParser.Digits, 0)

        def Sign(self):
            return self.getToken(MokadiGrammarParser.Sign, 0)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_integer_number

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInteger_number"):
                listener.enterInteger_number(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInteger_number"):
                listener.exitInteger_number(self)

    def integer_number(self):

        localctx = MokadiGrammarParser.Integer_numberContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_integer_number)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == MokadiGrammarParser.Sign:
                self.state = 54
                self.match(MokadiGrammarParser.Sign)

            self.state = 57
            self.match(MokadiGrammarParser.Digits)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Real_numberContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digits(self, i: int=None):
            if i is None:
                return self.getTokens(MokadiGrammarParser.Digits)
            else:
                return self.getToken(MokadiGrammarParser.Digits, i)

        def Sign(self, i: int=None):
            if i is None:
                return self.getTokens(MokadiGrammarParser.Sign)
            else:
                return self.getToken(MokadiGrammarParser.Sign, i)

        def getRuleIndex(self):
            return MokadiGrammarParser.RULE_real_number

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterReal_number"):
                listener.enterReal_number(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitReal_number"):
                listener.exitReal_number(self)

    def real_number(self):

        localctx = MokadiGrammarParser.Real_numberContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_real_number)
        self._la = 0  # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 10, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == MokadiGrammarParser.Sign:
                    self.state = 59
                    self.match(MokadiGrammarParser.Sign)

                self.state = 62
                self.match(MokadiGrammarParser.Digits)
                self.state = 63
                self.match(MokadiGrammarParser.T__19)
                self.state = 64
                self.match(MokadiGrammarParser.Digits)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == MokadiGrammarParser.T__20:
                    self.state = 65
                    self.match(MokadiGrammarParser.T__20)
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == MokadiGrammarParser.Sign:
                        self.state = 66
                        self.match(MokadiGrammarParser.Sign)

                    self.state = 69
                    self.match(MokadiGrammarParser.Digits)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == MokadiGrammarParser.Sign:
                    self.state = 72
                    self.match(MokadiGrammarParser.Sign)

                self.state = 75
                self.match(MokadiGrammarParser.Digits)
                self.state = 76
                self.match(MokadiGrammarParser.T__20)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == MokadiGrammarParser.Sign:
                    self.state = 77
                    self.match(MokadiGrammarParser.Sign)

                self.state = 80
                self.match(MokadiGrammarParser.Digits)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
