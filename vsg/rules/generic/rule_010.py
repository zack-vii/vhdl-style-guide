
from vsg import parser
from vsg import rule_item
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils

lTokens = []
lTokens.append(token.generic_clause.close_parenthesis)


class rule_010(rule_item.Rule):
    '''
    Moves code after the ) to the next line.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object type to split a line at
    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'generic', '010')
        self.solution = 'Closing parenthesis must be on a line by itself.'
        self.phase = 1
        self.lTokens = lTokens

    def analyze(self, oFile):
        aToi = oFile.get_tokens_bounded_by(token.generic_clause.close_parenthesis, parser.carriage_return)
        lToi = oFile.get_token_and_n_tokens_before_it(token.generic_clause.close_parenthesis, 2)
        for iToi, oToi in enumerate(lToi):

            lTokens = oToi.get_tokens()

            if isinstance(lTokens[0], parser.carriage_return) or isinstance(lTokens[1], parser.carriage_return):
                continue

            sSolution = self.solution
            dAction = {}

            if utils.does_token_type_exist_in_list_of_tokens(token.generic_clause.semicolon, aToi[iToi].get_tokens()):
                for iToken, oToken in enumerate(aToi[iToi].get_tokens()):
                    if isinstance(oToken, token.generic_clause.semicolon):
                        dAction['action'] = 'move'
                        dAction['index'] = iToken
                        break
            else:
                dAction['action'] = 'insert'

            oViolation = violation.New(aToi[iToi].get_line_number(), aToi[iToi], sSolution)
            oViolation.set_action(dAction)
            self.add_violation(oViolation)

    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            dAction = oViolation.get_action()
            if dAction['action'] == 'insert':
                lTokens.insert(0, parser.carriage_return())
            else:
                lNewTokens = lTokens[dAction['index'] + 1:]
                lNewTokens.extend(lTokens[:dAction['index'] + 1])
                lNewTokens.append(parser.carriage_return())

            oViolation.set_tokens(lNewTokens)
               
        oFile.update(self.violations)

