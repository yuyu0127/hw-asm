#! /usr/bin/env python3

from inst import Inst

filename = 'out2.hex'

_addrBase = 5
_pattern  = 10
patterns = [
    0b11100000,
    0b01110000,
    0b00111000,
    0b00011100,
    0b10001100,
    0b11000100,
]

program = []

program.append( Inst.LUI(_addrBase, 0x04000000) )

for p in patterns[:-1]:
    program.append( Inst.ADDI(_pattern, 0, p) )
    program.append( Inst.SB(_addrBase, _pattern, 0x00) )
    program.append( Inst.JAL(0, 0) )

program.append( Inst.ADDI(_pattern, 0, patterns[-1]) )
program.append( Inst.SB(_addrBase, _pattern, 0x00) )

program.append( Inst.JAL(0, -4*18) )

# generate assembly
#print('')
print('sample program 2')
for i in program :
    print('{:08x} | {}'.format(i.gen_code(), i.gen_mnemonic()))

# generate intel hex format
with open(filename, 'w', encoding='utf-8') as file:
    for offset, inst in enumerate(program) :
        file.write(inst.gen_HEX(offset))
        file.write("\n")
    file.write(':00000001FF\n')
