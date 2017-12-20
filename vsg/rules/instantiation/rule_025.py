
from vsg import rule
from vsg import utilities

import re


class rule_025(rule.rule):
    '''
    Instantiation rule 025 checks the **map** keyword is on the same line as the (.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '025'
        self.solution = 'Move the ( to the same line as the "generic map" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericKeyword and '(' not in oLine.lineNoComment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('map', 'map (', oLine.line, 1, re.IGNORECASE))
            utilities.search_for_and_remove_keyword(oFile, iLineNumber, '\(')
