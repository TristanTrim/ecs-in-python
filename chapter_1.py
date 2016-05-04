
from nand import nand_gate

# All of these gates need to be implemented using Nand gates.
# It would be easy to say 'out = not in' but we won't be doing that,
# cause then we wouldn't be learning about elemenary logic gates.
# We would just be doing weird re-implementation of basic operators.
# So without further ado, elementary logic gates implemented with our
# pretend nand gate, and gates implemented here:

def not_gate(input):
    return nand_gate(input,True)
        
def and_gate(a,b):
    return not_gate(nand_gate(a,b))

def or_gate(a,b):
    return nand_gate(not_gate(a),not_gate(b))

def xor_gate(a,b):
    return and_gate(nand_gate(a,b),or_gate(a,b))

def multiplexor(a,b,selector):
    return or_gate( \
             and_gate(a,not_gate(selector)),
             and_gate(b,selector))

def demultiplexor(input,selector):
    return(and_gate(input,not_gate(selector)),
           and_gate(input,selector))

