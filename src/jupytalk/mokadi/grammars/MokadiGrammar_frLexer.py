# Generated from \MokadiGrammar_fr.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u0269\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;")
        buf.write("\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\5@\u01ef\n@\3@\5@\u01f2\n@\3A\3A\3A\3A\3A\3A\3A\3A\5")
        buf.write("A\u01fc\nA\3A\5A\u01ff\nA\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\5B\u0210\nB\3C\3C\3D\6D\u0215\nD\rD\16")
        buf.write("D\u0216\3E\3E\3F\3F\7F\u021d\nF\fF\16F\u0220\13F\3G\3")
        buf.write("G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u022c\nG\3H\3H\3H\5H\u0231")
        buf.write("\nH\3I\3I\5I\u0235\nI\3J\3J\3J\3J\7J\u023b\nJ\fJ\16J\u023e")
        buf.write("\13J\3J\3J\3K\3K\3K\3K\7K\u0246\nK\fK\16K\u0249\13K\3")
        buf.write("K\3K\3L\3L\3M\3M\3N\3N\5N\u0253\nN\3O\3O\3P\3P\3Q\3Q\7")
        buf.write("Q\u025b\nQ\fQ\16Q\u025e\13Q\3Q\5Q\u0261\nQ\3Q\3Q\3Q\3")
        buf.write("R\3R\3R\3R\3\u025c\2S\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085")
        buf.write("D\u0087E\u0089F\u008bG\u008d\2\u008f\2\u0091H\u0093I\u0095")
        buf.write("J\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1K\u00a3")
        buf.write("L\3\2\b\4\2--//\3\2))\3\2$$\3\2\62;\6\2C\\aac|\u0082\u0101")
        buf.write("\5\2\13\f\17\17\"\"\2\u0276\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\3\u00a5\3\2\2\2\5\u00a7\3\2\2\2\7\u00a9")
        buf.write("\3\2\2\2\t\u00b0\3\2\2\2\13\u00b8\3\2\2\2\r\u00c1\3\2")
        buf.write("\2\2\17\u00ca\3\2\2\2\21\u00d1\3\2\2\2\23\u00dc\3\2\2")
        buf.write("\2\25\u00e6\3\2\2\2\27\u00ef\3\2\2\2\31\u00f4\3\2\2\2")
        buf.write("\33\u0101\3\2\2\2\35\u010d\3\2\2\2\37\u0115\3\2\2\2!\u011e")
        buf.write("\3\2\2\2#\u0125\3\2\2\2%\u0129\3\2\2\2\'\u0130\3\2\2\2")
        buf.write(")\u0136\3\2\2\2+\u0142\3\2\2\2-\u0147\3\2\2\2/\u014d\3")
        buf.write("\2\2\2\61\u0153\3\2\2\2\63\u0157\3\2\2\2\65\u015e\3\2")
        buf.write("\2\2\67\u0163\3\2\2\29\u0167\3\2\2\2;\u016c\3\2\2\2=\u0171")
        buf.write("\3\2\2\2?\u0176\3\2\2\2A\u017c\3\2\2\2C\u0183\3\2\2\2")
        buf.write("E\u018b\3\2\2\2G\u0190\3\2\2\2I\u0195\3\2\2\2K\u019c\3")
        buf.write("\2\2\2M\u01a0\3\2\2\2O\u01a4\3\2\2\2Q\u01a7\3\2\2\2S\u01aa")
        buf.write("\3\2\2\2U\u01ad\3\2\2\2W\u01b0\3\2\2\2Y\u01b4\3\2\2\2")
        buf.write("[\u01b8\3\2\2\2]\u01bb\3\2\2\2_\u01bf\3\2\2\2a\u01c1\3")
        buf.write("\2\2\2c\u01c3\3\2\2\2e\u01c5\3\2\2\2g\u01c7\3\2\2\2i\u01c9")
        buf.write("\3\2\2\2k\u01cb\3\2\2\2m\u01ce\3\2\2\2o\u01d1\3\2\2\2")
        buf.write("q\u01d4\3\2\2\2s\u01d7\3\2\2\2u\u01da\3\2\2\2w\u01dd\3")
        buf.write("\2\2\2y\u01df\3\2\2\2{\u01e1\3\2\2\2}\u01e3\3\2\2\2\177")
        buf.write("\u01e5\3\2\2\2\u0081\u01f3\3\2\2\2\u0083\u0200\3\2\2\2")
        buf.write("\u0085\u0211\3\2\2\2\u0087\u0214\3\2\2\2\u0089\u0218\3")
        buf.write("\2\2\2\u008b\u021a\3\2\2\2\u008d\u022b\3\2\2\2\u008f\u0230")
        buf.write("\3\2\2\2\u0091\u0234\3\2\2\2\u0093\u0236\3\2\2\2\u0095")
        buf.write("\u0241\3\2\2\2\u0097\u024c\3\2\2\2\u0099\u024e\3\2\2\2")
        buf.write("\u009b\u0252\3\2\2\2\u009d\u0254\3\2\2\2\u009f\u0256\3")
        buf.write("\2\2\2\u00a1\u0258\3\2\2\2\u00a3\u0265\3\2\2\2\u00a5\u00a6")
        buf.write("\7*\2\2\u00a6\4\3\2\2\2\u00a7\u00a8\7+\2\2\u00a8\6\3\2")
        buf.write("\2\2\u00a9\u00aa\7O\2\2\u00aa\u00ab\7Q\2\2\u00ab\u00ac")
        buf.write("\7M\2\2\u00ac\u00ad\7C\2\2\u00ad\u00ae\7F\2\2\u00ae\u00af")
        buf.write("\7K\2\2\u00af\b\3\2\2\2\u00b0\u00b1\7o\2\2\u00b1\u00b2")
        buf.write("\7q\2\2\u00b2\u00b3\7m\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5")
        buf.write("\7f\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7g\2\2\u00b7\n")
        buf.write("\3\2\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7q\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be")
        buf.write("\7f\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7g\2\2\u00c0\f")
        buf.write("\3\2\2\2\u00c1\u00c2\7N\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7")
        buf.write("\7f\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7g\2\2\u00c9\16")
        buf.write("\3\2\2\2\u00ca\u00cb\7j\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd")
        buf.write("\7o\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\20\3\2\2\2\u00d1\u00d2\7r\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7y\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6\u00d7\7r\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7v\2\2\u00db\22")
        buf.write("\3\2\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7w\2\2\u00df\u00e0\7x\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7n\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\24\3\2\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7x\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\26\3\2\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7y\2\2\u00f2\u00f3\7u\2\2\u00f3\30")
        buf.write("\3\2\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7o\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7k\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100")
        buf.write("\7u\2\2\u0100\32\3\2\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7h\2\2\u0104\u0105\7q\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7o\2\2\u0107\u0108\7c\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109\u010a\7k\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\34\3\2\2\2\u010d\u010e\7p\2\2\u010e\u010f")
        buf.write("\7q\2\2\u010f\u0110\7w\2\2\u0110\u0111\7x\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\u0113\7c\2\2\u0113\u0114\7w\2\2\u0114\36")
        buf.write("\3\2\2\2\u0115\u0116\7p\2\2\u0116\u0117\7q\2\2\u0117\u0118")
        buf.write("\7w\2\2\u0118\u0119\7x\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write("\7c\2\2\u011b\u011c\7w\2\2\u011c\u011d\7z\2\2\u011d \3")
        buf.write("\2\2\2\u011e\u011f\7r\2\2\u011f\u0120\7t\2\2\u0120\u0121")
        buf.write("\7q\2\2\u0121\u0122\7r\2\2\u0122\u0123\7q\2\2\u0123\u0124")
        buf.write("\7u\2\2\u0124\"\3\2\2\2\u0125\u0126\7u\2\2\u0126\u0127")
        buf.write("\7w\2\2\u0127\u0128\7t\2\2\u0128$\3\2\2\2\u0129\u012a")
        buf.write("\7u\2\2\u012a\u012b\7n\2\2\u012b\u012c\7k\2\2\u012c\u012d")
        buf.write("\7f\2\2\u012d\u012e\7g\2\2\u012e\u012f\7u\2\2\u012f&\3")
        buf.write("\2\2\2\u0130\u0131\7u\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7f\2\2\u0134\u0135\7g\2\2\u0135(\3")
        buf.write("\2\2\2\u0136\u0137\7v\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7c\2\2\u0139\u013a\7p\2\2\u013a\u013b\7u\2\2\u013b\u013c")
        buf.write("\7r\2\2\u013c\u013d\7c\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7p\2\2\u0140\u0141\7v\2\2\u0141*\3")
        buf.write("\2\2\2\u0142\u0143\7o\2\2\u0143\u0144\7c\2\2\u0144\u0145")
        buf.write("\7k\2\2\u0145\u0146\7n\2\2\u0146,\3\2\2\2\u0147\u0148")
        buf.write("\7o\2\2\u0148\u0149\7c\2\2\u0149\u014a\7k\2\2\u014a\u014b")
        buf.write("\7n\2\2\u014b\u014c\7u\2\2\u014c.\3\2\2\2\u014d\u014e")
        buf.write("\7g\2\2\u014e\u014f\7o\2\2\u014f\u0150\7c\2\2\u0150\u0151")
        buf.write("\7k\2\2\u0151\u0152\7n\2\2\u0152\60\3\2\2\2\u0153\u0154")
        buf.write("\7o\2\2\u0154\u0155\7g\2\2\u0155\u0156\7n\2\2\u0156\62")
        buf.write("\3\2\2\2\u0157\u0158\7g\2\2\u0158\u0159\7o\2\2\u0159\u015a")
        buf.write("\7c\2\2\u015a\u015b\7k\2\2\u015b\u015c\7n\2\2\u015c\u015d")
        buf.write("\7u\2\2\u015d\64\3\2\2\2\u015e\u015f\7o\2\2\u015f\u0160")
        buf.write("\7g\2\2\u0160\u0161\7n\2\2\u0161\u0162\7u\2\2\u0162\66")
        buf.write("\3\2\2\2\u0163\u0164\7n\2\2\u0164\u0165\7k\2\2\u0165\u0166")
        buf.write("\7v\2\2\u01668\3\2\2\2\u0167\u0168\7x\2\2\u0168\u0169")
        buf.write("\7q\2\2\u0169\u016a\7k\2\2\u016a\u016b\7t\2\2\u016b:\3")
        buf.write("\2\2\2\u016c\u016d\7n\2\2\u016d\u016e\7k\2\2\u016e\u016f")
        buf.write("\7u\2\2\u016f\u0170\7v\2\2\u0170<\3\2\2\2\u0171\u0172")
        buf.write("\7n\2\2\u0172\u0173\7k\2\2\u0173\u0174\7t\2\2\u0174\u0175")
        buf.write("\7g\2\2\u0175>\3\2\2\2\u0176\u0177\7n\2\2\u0177\u0178")
        buf.write("\7k\2\2\u0178\u0179\7u\2\2\u0179\u017a\7v\2\2\u017a\u017b")
        buf.write("\7g\2\2\u017b@\3\2\2\2\u017c\u017d\7n\2\2\u017d\u017e")
        buf.write("\7k\2\2\u017e\u017f\7u\2\2\u017f\u0180\7v\2\2\u0180\u0181")
        buf.write("\7g\2\2\u0181\u0182\7t\2\2\u0182B\3\2\2\2\u0183\u0184")
        buf.write("\7s\2\2\u0184\u0185\7w\2\2\u0185\u0186\7g\2\2\u0186\u0187")
        buf.write("\7n\2\2\u0187\u0188\7n\2\2\u0188\u0189\7g\2\2\u0189\u018a")
        buf.write("\7u\2\2\u018aD\3\2\2\2\u018b\u018c\7u\2\2\u018c\u018d")
        buf.write("\7q\2\2\u018d\u018e\7p\2\2\u018e\u018f\7v\2\2\u018fF\3")
        buf.write("\2\2\2\u0190\u0191\7s\2\2\u0191\u0192\7w\2\2\u0192\u0193")
        buf.write("\7g\2\2\u0193\u0194\7n\2\2\u0194H\3\2\2\2\u0195\u0196")
        buf.write("\7s\2\2\u0196\u0197\7w\2\2\u0197\u0198\7g\2\2\u0198\u0199")
        buf.write("\7n\2\2\u0199\u019a\7n\2\2\u019a\u019b\7g\2\2\u019bJ\3")
        buf.write("\2\2\2\u019c\u019d\7g\2\2\u019d\u019e\7u\2\2\u019e\u019f")
        buf.write("\7v\2\2\u019fL\3\2\2\2\u01a0\u01a1\7n\2\2\u01a1\u01a2")
        buf.write("\7g\2\2\u01a2\u01a3\7u\2\2\u01a3N\3\2\2\2\u01a4\u01a5")
        buf.write("\7n\2\2\u01a5\u01a6\7g\2\2\u01a6P\3\2\2\2\u01a7\u01a8")
        buf.write("\7n\2\2\u01a8\u01a9\7c\2\2\u01a9R\3\2\2\2\u01aa\u01ab")
        buf.write("\7f\2\2\u01ab\u01ac\7w\2\2\u01acT\3\2\2\2\u01ad\u01ae")
        buf.write("\7f\2\2\u01ae\u01af\7g\2\2\u01afV\3\2\2\2\u01b0\u01b1")
        buf.write("\7f\2\2\u01b1\u01b2\7g\2\2\u01b2\u01b3\7u\2\2\u01b3X\3")
        buf.write("\2\2\2\u01b4\u01b5\7o\2\2\u01b5\u01b6\7q\2\2\u01b6\u01b7")
        buf.write("\7p\2\2\u01b7Z\3\2\2\2\u01b8\u01b9\7o\2\2\u01b9\u01ba")
        buf.write("\7c\2\2\u01ba\\\3\2\2\2\u01bb\u01bc\7o\2\2\u01bc\u01bd")
        buf.write("\7g\2\2\u01bd\u01be\7u\2\2\u01be^\3\2\2\2\u01bf\u01c0")
        buf.write("\7A\2\2\u01c0`\3\2\2\2\u01c1\u01c2\7-\2\2\u01c2b\3\2\2")
        buf.write("\2\u01c3\u01c4\7/\2\2\u01c4d\3\2\2\2\u01c5\u01c6\7,\2")
        buf.write("\2\u01c6f\3\2\2\2\u01c7\u01c8\7\61\2\2\u01c8h\3\2\2\2")
        buf.write("\u01c9\u01ca\7\'\2\2\u01caj\3\2\2\2\u01cb\u01cc\7(\2\2")
        buf.write("\u01cc\u01cd\7(\2\2\u01cdl\3\2\2\2\u01ce\u01cf\7~\2\2")
        buf.write("\u01cf\u01d0\7~\2\2\u01d0n\3\2\2\2\u01d1\u01d2\7?\2\2")
        buf.write("\u01d2\u01d3\7?\2\2\u01d3p\3\2\2\2\u01d4\u01d5\7#\2\2")
        buf.write("\u01d5\u01d6\7?\2\2\u01d6r\3\2\2\2\u01d7\u01d8\7>\2\2")
        buf.write("\u01d8\u01d9\7?\2\2\u01d9t\3\2\2\2\u01da\u01db\7@\2\2")
        buf.write("\u01db\u01dc\7?\2\2\u01dcv\3\2\2\2\u01dd\u01de\7@\2\2")
        buf.write("\u01dex\3\2\2\2\u01df\u01e0\7>\2\2\u01e0z\3\2\2\2\u01e1")
        buf.write("\u01e2\7\60\2\2\u01e2|\3\2\2\2\u01e3\u01e4\7g\2\2\u01e4")
        buf.write("~\3\2\2\2\u01e5\u01e6\7f\2\2\u01e6\u01e7\7g\2\2\u01e7")
        buf.write("\u01e8\7t\2\2\u01e8\u01e9\7p\2\2\u01e9\u01ea\7k\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u01ec\5\u008dG\2\u01ec\u01ee\7t\2")
        buf.write("\2\u01ed\u01ef\7g\2\2\u01ee\u01ed\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01f2\7u\2\2\u01f1")
        buf.write("\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u0080\3\2\2\2")
        buf.write("\u01f3\u01f4\7t\2\2\u01f4\u01f5\5\u008dG\2\u01f5\u01f6")
        buf.write("\7e\2\2\u01f6\u01f7\7g\2\2\u01f7\u01f8\7p\2\2\u01f8\u01f9")
        buf.write("\7v\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01fc\7g\2\2\u01fb\u01fa")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd")
        buf.write("\u01ff\7u\2\2\u01fe\u01fd\3\2\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ff\u0082\3\2\2\2\u0200\u0201\7r\2\2\u0201\u0202\7")
        buf.write("t\2\2\u0202\u0203\3\2\2\2\u0203\u0204\5\u008dG\2\u0204")
        buf.write("\u0205\7u\2\2\u0205\u0206\7g\2\2\u0206\u0207\7p\2\2\u0207")
        buf.write("\u0208\7v\2\2\u0208\u0209\7c\2\2\u0209\u020a\7v\2\2\u020a")
        buf.write("\u020b\7k\2\2\u020b\u020c\7q\2\2\u020c\u020d\7p\2\2\u020d")
        buf.write("\u020f\3\2\2\2\u020e\u0210\7u\2\2\u020f\u020e\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u0084\3\2\2\2\u0211\u0212\5")
        buf.write("\u008fH\2\u0212\u0086\3\2\2\2\u0213\u0215\5\u009dO\2\u0214")
        buf.write("\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0214\3\2\2\2")
        buf.write("\u0216\u0217\3\2\2\2\u0217\u0088\3\2\2\2\u0218\u0219\t")
        buf.write("\2\2\2\u0219\u008a\3\2\2\2\u021a\u021e\5\u009fP\2\u021b")
        buf.write("\u021d\5\u009bN\2\u021c\u021b\3\2\2\2\u021d\u0220\3\2")
        buf.write("\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u008c")
        buf.write("\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u022c\4\u00ea\u00ed")
        buf.write("\2\u0222\u0223\7\u00c5\2\2\u0223\u022c\7\u00ab\2\2\u0224")
        buf.write("\u022c\7g\2\2\u0225\u0226\7\u00c5\2\2\u0226\u022c\7\u00aa")
        buf.write("\2\2\u0227\u0228\7\u00c5\2\2\u0228\u022c\7\u00ac\2\2\u0229")
        buf.write("\u022a\7\u00c5\2\2\u022a\u022c\7\u00ad\2\2\u022b\u0221")
        buf.write("\3\2\2\2\u022b\u0222\3\2\2\2\u022b\u0224\3\2\2\2\u022b")
        buf.write("\u0225\3\2\2\2\u022b\u0227\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022c\u008e\3\2\2\2\u022d\u0231\7\u00e2\2\2\u022e\u022f")
        buf.write("\7\u00c5\2\2\u022f\u0231\7\u00a2\2\2\u0230\u022d\3\2\2")
        buf.write("\2\u0230\u022e\3\2\2\2\u0231\u0090\3\2\2\2\u0232\u0235")
        buf.write("\5\u0093J\2\u0233\u0235\5\u0095K\2\u0234\u0232\3\2\2\2")
        buf.write("\u0234\u0233\3\2\2\2\u0235\u0092\3\2\2\2\u0236\u023c\7")
        buf.write("$\2\2\u0237\u023b\5\u0099M\2\u0238\u0239\7^\2\2\u0239")
        buf.write("\u023b\7$\2\2\u023a\u0237\3\2\2\2\u023a\u0238\3\2\2\2")
        buf.write("\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3")
        buf.write("\2\2\2\u023d\u023f\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0240")
        buf.write("\7$\2\2\u0240\u0094\3\2\2\2\u0241\u0247\7)\2\2\u0242\u0246")
        buf.write("\5\u0097L\2\u0243\u0244\7^\2\2\u0244\u0246\7)\2\2\u0245")
        buf.write("\u0242\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u0249\3\2\2\2")
        buf.write("\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024a\3")
        buf.write("\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\7)\2\2\u024b\u0096")
        buf.write("\3\2\2\2\u024c\u024d\n\3\2\2\u024d\u0098\3\2\2\2\u024e")
        buf.write("\u024f\n\4\2\2\u024f\u009a\3\2\2\2\u0250\u0253\5\u009f")
        buf.write("P\2\u0251\u0253\5\u009dO\2\u0252\u0250\3\2\2\2\u0252\u0251")
        buf.write("\3\2\2\2\u0253\u009c\3\2\2\2\u0254\u0255\t\5\2\2\u0255")
        buf.write("\u009e\3\2\2\2\u0256\u0257\t\6\2\2\u0257\u00a0\3\2\2\2")
        buf.write("\u0258\u025c\7%\2\2\u0259\u025b\13\2\2\2\u025a\u0259\3")
        buf.write("\2\2\2\u025b\u025e\3\2\2\2\u025c\u025d\3\2\2\2\u025c\u025a")
        buf.write("\3\2\2\2\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2\u025f")
        buf.write("\u0261\7\17\2\2\u0260\u025f\3\2\2\2\u0260\u0261\3\2\2")
        buf.write("\2\u0261\u0262\3\2\2\2\u0262\u0263\7\f\2\2\u0263\u0264")
        buf.write("\bQ\2\2\u0264\u00a2\3\2\2\2\u0265\u0266\t\7\2\2\u0266")
        buf.write("\u0267\3\2\2\2\u0267\u0268\bR\3\2\u0268\u00a4\3\2\2\2")
        buf.write("\24\2\u01ee\u01f1\u01fb\u01fe\u020f\u0216\u021e\u022b")
        buf.write("\u0230\u0234\u023a\u023c\u0245\u0247\u0252\u025c\u0260")
        buf.write("\4\3Q\2\b\2\2")
        return buf.getvalue()


class MokadiGrammar_frLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    Dernieres = 63
    Recent = 64
    Presentation = 65
    Astopword = 66
    Digits = 67
    Sign = 68
    Identifier = 69
    STRING = 70
    STRING_DOUBLE_QUOTE = 71
    STRING_QUOTE = 72
    LINE_COMMENT = 73
    WS = 74

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'('", "')'", "'MOKADI'", "'mokadie'", "'leocadie'", "'Leocadie'",
                    "'humeur'", "'powerpoint'", "'nouvelles'", "'nouvelle'", "'news'",
                    "'informations'", "'information'", "'nouveau'", "'nouveaux'",
                    "'propos'", "'sur'", "'slides'", "'slide'", "'transparent'",
                    "'mail'", "'mails'", "'email'", "'mel'", "'emails'", "'mels'",
                    "'lit'", "'voir'", "'list'", "'lire'", "'liste'", "'lister'",
                    "'quelles'", "'sont'", "'quel'", "'quelle'", "'est'", "'les'",
                    "'le'", "'la'", "'du'", "'de'", "'des'", "'mon'", "'ma'", "'mes'",
                    "'?'", "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'=='",
                    "'!='", "'<='", "'>='", "'>'", "'<'", "'.'", "'e'"]

    symbolicNames = ["<INVALID>",
                     "Dernieres", "Recent", "Presentation", "Astopword", "Digits",
                     "Sign", "Identifier", "STRING", "STRING_DOUBLE_QUOTE", "STRING_QUOTE",
                     "LINE_COMMENT", "WS"]

    ruleNames = ["T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6",
                 "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13",
                 "T__14", "T__15", "T__16", "T__17", "T__18", "T__19",
                 "T__20", "T__21", "T__22", "T__23", "T__24", "T__25",
                 "T__26", "T__27", "T__28", "T__29", "T__30", "T__31",
                 "T__32", "T__33", "T__34", "T__35", "T__36", "T__37",
                 "T__38", "T__39", "T__40", "T__41", "T__42", "T__43",
                 "T__44", "T__45", "T__46", "T__47", "T__48", "T__49",
                 "T__50", "T__51", "T__52", "T__53", "T__54", "T__55",
                 "T__56", "T__57", "T__58", "T__59", "T__60", "T__61",
                 "Dernieres", "Recent", "Presentation", "Astopword", "Digits",
                 "Sign", "Identifier", "E_CODE", "A_CODE", "STRING", "STRING_DOUBLE_QUOTE",
                 "STRING_QUOTE", "NO_QUOTE", "NO_DOUBLE_QUOTE", "LETTER_DIGIT",
                 "DIGIT", "LETTER", "LINE_COMMENT", "WS"]

    grammarFileName = "MokadiGrammar_fr.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

    def action(self, localctx: RuleContext, ruleIndex: int, actionIndex: int):
        if self._actions is None:
            actions = dict()
            actions[79] = self.LINE_COMMENT_action
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def LINE_COMMENT_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 0:
            skip()
