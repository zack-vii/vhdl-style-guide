
context c1 is

  library ieee;
    context cr1;

end context c1;

-- try multiline
context c1 is

  library ieee;
    context cr1,cr2;

end context c1;

context c1 is

  library ieee;

end context c1;

context c1 is

    context cr1,cr2;

  library ieee;

end context c1;

context c1 is

  library ieee;

end context c1;

-- Try single line
context c1 is

  library ieee; use ieee.std_logic_1164;
    context cr1,cr2;

end context c1;

-- Check comments

context c1 is -- comment 1

-- comment 2
-- comment 3

  library ieee; -- comment 4

end context c1; -- comment 5

-- comment 6
-- comment 7
-- comment 8

library ieee;
  context
cr1
,
cr2
;

