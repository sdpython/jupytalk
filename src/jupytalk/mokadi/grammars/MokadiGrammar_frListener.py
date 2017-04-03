# Generated from \MokadiGrammar_fr.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MokadiGrammar_frParser import MokadiGrammar_frParser
else:
    from MokadiGrammar_frParser import MokadiGrammar_frParser

# This class defines a complete listener for a parse tree produced by
# MokadiGrammar_frParser.


class MokadiGrammar_frListener(ParseTreeListener):

    # Enter a parse tree produced by MokadiGrammar_frParser#parse.
    def enterParse(self, ctx: MokadiGrammar_frParser.ParseContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#parse.
    def exitParse(self, ctx: MokadiGrammar_frParser.ParseContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#expression_stmt.
    def enterExpression_stmt(self, ctx: MokadiGrammar_frParser.Expression_stmtContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#expression_stmt.
    def exitExpression_stmt(self, ctx: MokadiGrammar_frParser.Expression_stmtContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#expression.
    def enterExpression(self, ctx: MokadiGrammar_frParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#expression.
    def exitExpression(self, ctx: MokadiGrammar_frParser.ExpressionContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#slides_stmt.
    def enterSlides_stmt(self, ctx: MokadiGrammar_frParser.Slides_stmtContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#slides_stmt.
    def exitSlides_stmt(self, ctx: MokadiGrammar_frParser.Slides_stmtContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#mail_stmt.
    def enterMail_stmt(self, ctx: MokadiGrammar_frParser.Mail_stmtContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#mail_stmt.
    def exitMail_stmt(self, ctx: MokadiGrammar_frParser.Mail_stmtContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#news_stmt.
    def enterNews_stmt(self, ctx: MokadiGrammar_frParser.News_stmtContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#news_stmt.
    def exitNews_stmt(self, ctx: MokadiGrammar_frParser.News_stmtContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#news_query.
    def enterNews_query(self, ctx: MokadiGrammar_frParser.News_queryContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#news_query.
    def exitNews_query(self, ctx: MokadiGrammar_frParser.News_queryContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#anything_stmt.
    def enterAnything_stmt(self, ctx: MokadiGrammar_frParser.Anything_stmtContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#anything_stmt.
    def exitAnything_stmt(self, ctx: MokadiGrammar_frParser.Anything_stmtContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#mokadi.
    def enterMokadi(self, ctx: MokadiGrammar_frParser.MokadiContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#mokadi.
    def exitMokadi(self, ctx: MokadiGrammar_frParser.MokadiContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#presentation.
    def enterPresentation(self, ctx: MokadiGrammar_frParser.PresentationContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#presentation.
    def exitPresentation(self, ctx: MokadiGrammar_frParser.PresentationContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#news.
    def enterNews(self, ctx: MokadiGrammar_frParser.NewsContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#news.
    def exitNews(self, ctx: MokadiGrammar_frParser.NewsContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#time_indication.
    def enterTime_indication(self, ctx: MokadiGrammar_frParser.Time_indicationContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#time_indication.
    def exitTime_indication(self, ctx: MokadiGrammar_frParser.Time_indicationContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#apropos.
    def enterApropos(self, ctx: MokadiGrammar_frParser.AproposContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#apropos.
    def exitApropos(self, ctx: MokadiGrammar_frParser.AproposContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#slides.
    def enterSlides(self, ctx: MokadiGrammar_frParser.SlidesContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#slides.
    def exitSlides(self, ctx: MokadiGrammar_frParser.SlidesContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#mails.
    def enterMails(self, ctx: MokadiGrammar_frParser.MailsContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#mails.
    def exitMails(self, ctx: MokadiGrammar_frParser.MailsContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#verb_voir.
    def enterVerb_voir(self, ctx: MokadiGrammar_frParser.Verb_voirContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#verb_voir.
    def exitVerb_voir(self, ctx: MokadiGrammar_frParser.Verb_voirContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#stop_words.
    def enterStop_words(self, ctx: MokadiGrammar_frParser.Stop_wordsContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#stop_words.
    def exitStop_words(self, ctx: MokadiGrammar_frParser.Stop_wordsContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#questions_mark.
    def enterQuestions_mark(self, ctx: MokadiGrammar_frParser.Questions_markContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#questions_mark.
    def exitQuestions_mark(self, ctx: MokadiGrammar_frParser.Questions_markContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#word_name.
    def enterWord_name(self, ctx: MokadiGrammar_frParser.Word_nameContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#word_name.
    def exitWord_name(self, ctx: MokadiGrammar_frParser.Word_nameContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#operator.
    def enterOperator(self, ctx: MokadiGrammar_frParser.OperatorContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#operator.
    def exitOperator(self, ctx: MokadiGrammar_frParser.OperatorContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#question.
    def enterQuestion(self, ctx: MokadiGrammar_frParser.QuestionContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#question.
    def exitQuestion(self, ctx: MokadiGrammar_frParser.QuestionContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#constant.
    def enterConstant(self, ctx: MokadiGrammar_frParser.ConstantContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#constant.
    def exitConstant(self, ctx: MokadiGrammar_frParser.ConstantContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#string_literal.
    def enterString_literal(self, ctx: MokadiGrammar_frParser.String_literalContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#string_literal.
    def exitString_literal(self, ctx: MokadiGrammar_frParser.String_literalContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#integer_number.
    def enterInteger_number(self, ctx: MokadiGrammar_frParser.Integer_numberContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#integer_number.
    def exitInteger_number(self, ctx: MokadiGrammar_frParser.Integer_numberContext):
        pass

    # Enter a parse tree produced by MokadiGrammar_frParser#real_number.
    def enterReal_number(self, ctx: MokadiGrammar_frParser.Real_numberContext):
        pass

    # Exit a parse tree produced by MokadiGrammar_frParser#real_number.
    def exitReal_number(self, ctx: MokadiGrammar_frParser.Real_numberContext):
        pass
