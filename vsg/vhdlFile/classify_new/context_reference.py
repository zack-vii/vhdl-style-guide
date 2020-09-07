
from vsg import parser
from vsg.token import context_reference as token

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    context_reference ::=
        context selected_name { , selected_name } ;
    '''
    if utils.object_value_is(lObjects, iCurrent, 'context'):
        if not utils.find_in_range('is', iCurrent, ';', lObjects):
            return classify(iCurrent, lObjects)
    return iCurrent


def classify(iCurrent, lObjects):
    '''
    context_reference ::=
        context selected_name { , selected_name } ;
    '''
    iStart, iEnd = utils.get_range(lObjects, iCurrent, ';')
    
    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
            if utils.classify_token('context', token.keyword, iToken, lObjects):
                continue
            if utils.classify_token(',', token.comma, iToken, lObjects):
                continue
            utils.assign_token(lObjects, iToken, token.selected_name)

    utils.classify_token(';', token.semicolon, iEnd, lObjects)
    return iEnd