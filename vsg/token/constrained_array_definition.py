
from vsg import parser


class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class index_constraint(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class of_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class subtype_indication(parser.subtype_indication):

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)