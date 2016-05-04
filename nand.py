
"""This is the nand gate. We are pretending we have one of these
implemented, and can use it to implement the rest of a computer.
The inputs are bit a and bit b, which should be booleans.
"""

def nand_gate(a,b):
    if a and b:
        return False
    else:
        return True

