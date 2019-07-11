#! /usr/bin/env python3

from inst import Inst

filename = 'program.hex'


_num0 = 0
_wr = 1
_barY1 = 2
_barY2 = 3
_addrBase = 4

_pattern0 = 5
_pattern1 = 6
_pattern2 = 7
_pattern3 = 8

_posX = 9
_posY = 10
_velX = 11
_velY = 12
_dirX = 13
_dirY = 14

_input = 15

_num1 = 26
_num2 = 27
_num3 = 28
_num13 = 29


initialize = []
loop = []
finalize = []

# 初期化部分
initialize.append( Inst.LUI(_addrBase, 0x04000000) )    # addrBase = [0x04000000]
initialize.append( Inst.ADDI(_wr, _num0, 1) )           # wr = 1
initialize.append( Inst.SLLI(_wr, _wr, 14) )            # wr <<= 14
initialize.append( Inst.ADDI(_barY1, _num0, 0) )        # barY1 = 1
initialize.append( Inst.ADDI(_barY2, _num0, 1) )        # barY2 = 2
initialize.append( Inst.ADDI(_posX, _num0, 7) )         # posX = 7
initialize.append( Inst.ADDI(_posY, _num0, 1) )         # posY = 1
initialize.append( Inst.ADDI(_velX, _num0, 1) )         # velX = 1
initialize.append( Inst.ADDI(_velY, _num0, 1) )         # velY = 1
initialize.append( Inst.ADDI(_num1  , _num0, 1) )       # num1 = 1
initialize.append( Inst.ADDI(_num2  , _num0, 2) )       # num2 = 2
initialize.append( Inst.ADDI(_num3, _num0, 3) )         # num3 = 3
initialize.append( Inst.ADDI(_num13, _num0, 13) )       # num13 = 13

# ループ部分
# パターン初期化
loop.append( Inst.ADDI(_pattern0, _num0, 0) )           # pattern0 = 0
loop.append( Inst.ADDI(_pattern1, _num0, 0) )           # pattern1 = 0
loop.append( Inst.ADDI(_pattern2, _num0, 0) )           # pattern2 = 0
loop.append( Inst.ADDI(_pattern3, _num0, 0) )           # pattern3 = 0

# ボールがある列にボールを表示
loop.append( Inst.BNE(_posY, _num0, 8) )                # if posY == 0
loop.append( Inst.ADDI(_pattern0, _num0, 1) )           #   pattern0 = 1
loop.append( Inst.SLL(_pattern0, _pattern0, _posX) )    #   pattern0 <<= posX
loop.append( Inst.BNE(_posY, _num1, 8) )                # if posY == 1
loop.append( Inst.ADDI(_pattern1, _num0, 1) )           #   pattern1 = 1
loop.append( Inst.SLL(_pattern1, _pattern1, _posX) )    #   pattern1 <<= posX
loop.append( Inst.BNE(_posY, _num2, 8) )                # if posY == 2
loop.append( Inst.ADDI(_pattern2, _num0, 1) )           #   pattern2 = 1
loop.append( Inst.SLL(_pattern2, _pattern2, _posX) )    #   pattern2 <<= posX
loop.append( Inst.BNE(_posY, _num3, 8) )                # if posY == 3
loop.append( Inst.ADDI(_pattern3, _num0, 1) )           #   pattern3 = 1
loop.append( Inst.SLL(_pattern3, _pattern3, _posX) )    #   pattern3 <<= posX

# 左側のバーの表示
loop.append( Inst.BNE(_barY1, _num0, 4) )               # if barY1 == 0
loop.append( Inst.ADDI(_pattern0, _pattern0, 2) )       #   pattern0 += 2
loop.append( Inst.BNE(_barY1, _num1, 4) )               # if barY1 == 1
loop.append( Inst.ADDI(_pattern1, _pattern1, 2) )       #   pattern1 += 2
loop.append( Inst.BNE(_barY1, _num2, 4) )               # if barY1 == 2
loop.append( Inst.ADDI(_pattern2, _pattern2, 2) )       #   pattern2 += 2
loop.append( Inst.BNE(_barY1, _num3, 4) )               # if barY1 == 3
loop.append( Inst.ADDI(_pattern3, _pattern3, 2) )       #   pattern3 += 2

# 右側のバーの表示
loop.append( Inst.BNE(_barY2, _num0, 4) )               # if barY2 == 0
loop.append( Inst.ADD(_pattern0, _pattern0, _wr) )      #   pattern0 += wr
loop.append( Inst.BNE(_barY2, _num1, 4) )               # if barY2 == 1
loop.append( Inst.ADD(_pattern1, _pattern1, _wr) )      #   pattern1 += wr
loop.append( Inst.BNE(_barY2, _num2, 4) )               # if barY2 == 2
loop.append( Inst.ADD(_pattern2, _pattern2, _wr) )      #   pattern2 += wr
loop.append( Inst.BNE(_barY2, _num3, 4) )               # if barY2 == 3
loop.append( Inst.ADD(_pattern3, _pattern3, _wr) )      #   pattern3 += wr

# ドットマトリックスLEDの発光
loop.append( Inst.SH(_addrBase, _pattern0, 0x40) )      # [addrBase + 0x40] = pattern0
loop.append( Inst.SH(_addrBase, _pattern1, 0x42) )      # [addrBase + 0x42] = pattern1
loop.append( Inst.SH(_addrBase, _pattern2, 0x44) )      # [addrBase + 0x44] = pattern2
loop.append( Inst.SH(_addrBase, _pattern3, 0x46) )      # [addrBase + 0x46] = pattern3

# ボールの左端反射
loop.append( Inst.BNE(_posX, _num2, 8) )                # if posX == 2
loop.append( Inst.BNE(_posY, _barY1, 4) )               #   if posY == barY1
loop.append( Inst.SUB(_velX, 0, _velX) )                #     velX = 0 - velX

# ボールの右端反射
loop.append( Inst.BNE(_posX, _num13, 8) )               # if posX == 13
loop.append( Inst.BNE(_posY, _barY2, 4) )               #   if posY == barY2
loop.append( Inst.SUB(_velX, 0, _velX) )                #     velX = 0 - velX

# ボールの上反射
loop.append( Inst.BNE(_posY, _num0, 4) )                # if posY == 0
loop.append( Inst.SUB(_velY, 0, _velY) )

# ボールの下反射
loop.append( Inst.BNE(_posY, _num3, 4) )                # if posY == 3
loop.append( Inst.SUB(_velY, 0, _velY) )

# ボールの移動
loop.append( Inst.ADD(_posX, _posX, _velX) )
loop.append( Inst.ADD(_posY, _posY, _velY) )

# バーの座標設定
loop.append( Inst.LB(_input, _addrBase, 0x48) )
loop.append( Inst.ANDI(_input, _input, 0b0001_0000) )
loop.append( Inst.BEQ(_input, 0, 4) )
loop.append( Inst.SUB(_barY2, _barY2, _num1) )

loop.append( Inst.LB(_input, _addrBase, 0x4b) )
loop.append( Inst.ANDI(_input, _input, 0b0001_0000) )
loop.append( Inst.BEQ(_input, 0, 4) )
loop.append( Inst.ADD(_barY2, _barY2, _num1) )

loop.append( Inst.LB(_input, _addrBase, 0x48) )
loop.append( Inst.ANDI(_input, _input, 0b0000_0001) )
loop.append( Inst.BEQ(_input, 0, 4) )
loop.append( Inst.SUB(_barY1, _barY1, _num1) )

loop.append( Inst.LB(_input, _addrBase, 0x4b) )
loop.append( Inst.ANDI(_input, _input, 0b0000_0001) )
loop.append( Inst.BEQ(_input, 0, 4) )
loop.append( Inst.ADD(_barY1, _barY1, _num1) )

# ループの先頭に戻る
finalize.append( Inst.JAL(0, -4 * ( len(loop) + 2 ) ) )

program = initialize + loop + finalize

# generate assembly
#print('')
print('sample program 3')
for i in program :
    print('{:08x} | {}'.format(i.gen_code(), i.gen_mnemonic()))

# generate intel hex format
with open(filename, 'w', encoding='utf-8') as file:
    for offset, inst in enumerate(program) :
        file.write(inst.gen_HEX(offset))
        file.write("\n")
    file.write(':00000001FF\n')
