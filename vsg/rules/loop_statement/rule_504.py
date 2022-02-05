
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.end_loop_label)


class rule_504(token_case_with_prefix_suffix):
    '''
    This rule checks the proper case of the end label on a loop statement.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

         end loop LABEL;
         end loop Label;

    **Fix**

    .. code-block:: vhdl

         end loop label;
         end loop label;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'loop_statement', '504', lTokens)
        self.groups.append('case::label')