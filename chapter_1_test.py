
from chapter_1 import *

gates = {
  "not_gate":(
    ((True,),False),
    ((False,),True),
    ),
  "and_gate":(
    ((True,True),True),
    ((True,False),False),
    ((False,True),False),
    ((False,False),False),
    ),
  "or_gate":(
    ((True,True),True),
    ((True,False),True),
    ((False,True),True),
    ((False,False),False),
    ),
  "xor_gate":(
    ((True,True),False),
    ((True,False),True),
    ((False,True),True),
    ((False,False),False),
    ),
  "multiplexor":(
    ((True,  True,  True),    True),
    ((True,  True,  False),   True),
    ((True,  False, True),    False),
    ((True,  False, False),   True),
    ((False, True,  True),    True),
    ((False, True,  False),   False),
    ((False, False, True),    False),
    ((False, False, False),   False),
    ),
  "demultiplexor":(
    ((True,  True),    (False,True )),
    ((True,  False),   (True, False)),
    ((False, True),    (False,False)),
    ((False, False),   (False,False)),
    ),
  }

def test_gate(gate,truth_table):
  for input, output in truth_table:
    if gate(*input) == output:
      # It's good!
      continue
    else:
      return False
  return True

for gate_name, gate_truths in gates.iteritems():
  if not gate_name in vars():
    print("{} is not yet implemented.".format(gate_name))
  elif test_gate(vars()[gate_name], gate_truths):
    print("{} is working".format(gate_name))
  else:
   print("{} is *not* working".format(gate_name))

