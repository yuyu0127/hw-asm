#! /usr/bin/env python3

from inst import Inst

filename = 'program.hex'


_num0		= 0
_wr			= 1
_barY1u		= 2
_barY2u		= 3
_barY1d		= 4
_barY2d		= 5
_addrBase	= 6
_pattern0	= 7
_pattern1	= 8
_pattern2	= 9
_pattern3	= 10
_posX		= 11
_posY		= 12
_velX		= 13
_velY		= 14
_tmp		= 15

_score1		= 21
_score2		= 22
_counterX	= 23
_intervalX	= 24
_counterY	= 25
_intervalY	= 26

# 初期化部分
sys_init = [

Inst.LUI(_addrBase, 0x0400_0000),			# addrBase = [0x0400_0000]
Inst.ADDI(_wr, _num0, 1),					# wr = 1
Inst.SLLI(_wr, _wr, 14),					# wr <<= 14
Inst.ADDI(_barY1u, _num0, 1),				# barY1u = 1
Inst.ADDI(_barY1d, _num0, 2),				# barY1d = 2
Inst.ADDI(_barY2u, _num0, 1),				# barY2u = 1
Inst.ADDI(_barY2d, _num0, 2),				# barY2d = 2
Inst.ADDI(_velX, _num0, 1),					# velX = 1
Inst.ADDI(_velY, _num0, 1),					# velY = 1
Inst.ADDI(_score1, _num0, 0),				# score1 = 0
Inst.ADDI(_score2, _num0, 0),				# score2 = 0
Inst.ADDI(_counterX, _num0, 0),				# counterX = 0
Inst.ADDI(_counterY, _num0, 0),				# counterY = 0
Inst.ADDI(_intervalX, _num0, 1),	# interval = INIT_ITV
Inst.ADDI(_intervalY, _num0, 1),	# interval = INIT_ITV
]


game_init = [

Inst.ADDI(_posX, _num0, 7),					# posX = 7
Inst.ADDI(_posY, _num0, 1),					# posY = 1

]


# ループ部分
game_loop = [

# パターン初期化
Inst.ADDI(_pattern0, _num0, 0),				# pattern0 = 0
Inst.ADDI(_pattern1, _num0, 0),				# pattern1 = 0
Inst.ADDI(_pattern2, _num0, 0),				# pattern2 = 0
Inst.ADDI(_pattern3, _num0, 0),				# pattern3 = 0

# ボールがある列にボールを表示
Inst.ADDI(_tmp, _num0, 0),
Inst.BNE(_posY, _tmp, 8),					# if posY == 0
Inst.ORI(_pattern0, _num0, 1),				# 	pattern0 = 1
Inst.SLL(_pattern0, _pattern0, _posX),		# 	pattern0 <<= posX
Inst.ADDI(_tmp, _num0, 1),
Inst.BNE(_posY, _tmp, 8),					# if posY == 1
Inst.ORI(_pattern1, _num0, 1),				# 	pattern1 = 1
Inst.SLL(_pattern1, _pattern1, _posX),		# 	pattern1 <<= posX
Inst.ADDI(_tmp, _num0, 2),
Inst.BNE(_posY, _tmp, 8),					# if posY == 2
Inst.ORI(_pattern2, _num0, 1),				# 	pattern2 = 1
Inst.SLL(_pattern2, _pattern2, _posX),		# 	pattern2 <<= posX
Inst.ADDI(_tmp, _num0, 3),
Inst.BNE(_posY, _tmp, 8),					# if posY == 3
Inst.ORI(_pattern3, _num0, 1),				# 	pattern3 = 1
Inst.SLL(_pattern3, _pattern3, _posX),		# 	pattern3 <<= posX

# 左側のバーの表示
Inst.ADDI(_tmp, _num0, 0),
Inst.BNE(_barY1u, _tmp, 4),				# if barY1 == 0
Inst.ORI(_pattern0, _pattern0, 2),			# 	pattern0 += 2
Inst.ADDI(_tmp, _num0, 1),
Inst.BNE(_barY1u, _tmp, 4),				# if barY1 == 1
Inst.ORI(_pattern1, _pattern1, 2),			# 	pattern1 += 2
Inst.ADDI(_tmp, _num0, 2),
Inst.BNE(_barY1u, _tmp, 4),				# if barY1 == 2
Inst.ORI(_pattern2, _pattern2, 2),			# 	pattern2 += 2
Inst.ADDI(_tmp, _num0, 3),
Inst.BNE(_barY1u, _tmp, 4),				# if barY1 == 3
Inst.ORI(_pattern3, _pattern3, 2),			# 	pattern3 += 2

Inst.ADDI(_tmp, _num0, 0),
Inst.BNE(_barY1d, _tmp, 4),				# if barY1 == 0
Inst.ORI(_pattern0, _pattern0, 2),			# 	pattern0 += 2
Inst.ADDI(_tmp, _num0, 1),
Inst.BNE(_barY1d, _tmp, 4),				# if barY1 == 1
Inst.ORI(_pattern1, _pattern1, 2),			# 	pattern1 += 2
Inst.ADDI(_tmp, _num0, 2),
Inst.BNE(_barY1d, _tmp, 4),				# if barY1 == 2
Inst.ORI(_pattern2, _pattern2, 2),			# 	pattern2 += 2
Inst.ADDI(_tmp, _num0, 3),
Inst.BNE(_barY1d, _tmp, 4),				# if barY1 == 3
Inst.ORI(_pattern3, _pattern3, 2),			# 	pattern3 += 2

# 右側のバーの表示
Inst.ADDI(_tmp, _num0, 0),
Inst.BNE(_barY2u, _tmp, 4),				# if barY2 == 0
Inst.OR(_pattern0, _pattern0, _wr),			# 	pattern0 += wr
Inst.ADDI(_tmp, _num0, 1),
Inst.BNE(_barY2u, _tmp, 4),				# if barY2 == 1
Inst.OR(_pattern1, _pattern1, _wr),			# 	pattern1 += wr
Inst.ADDI(_tmp, _num0, 2),
Inst.BNE(_barY2u, _tmp, 4),				# if barY2 == 2
Inst.OR(_pattern2, _pattern2, _wr),			# 	pattern2 += wr
Inst.ADDI(_tmp, _num0, 3),
Inst.BNE(_barY2u, _tmp, 4),				# if barY2 == 3
Inst.OR(_pattern3, _pattern3, _wr),			# 	pattern3 += wr

Inst.ADDI(_tmp, _num0, 0),
Inst.BNE(_barY2d, _tmp, 4),				# if barY2 == 0
Inst.OR(_pattern0, _pattern0, _wr),			# 	pattern0 += wr
Inst.ADDI(_tmp, _num0, 1),
Inst.BNE(_barY2d, _tmp, 4),				# if barY2 == 1
Inst.OR(_pattern1, _pattern1, _wr),			# 	pattern1 += wr
Inst.ADDI(_tmp, _num0, 2),
Inst.BNE(_barY2d, _tmp, 4),				# if barY2 == 2
Inst.OR(_pattern2, _pattern2, _wr),			# 	pattern2 += wr
Inst.ADDI(_tmp, _num0, 3),
Inst.BNE(_barY2d, _tmp, 4),				# if barY2 == 3
Inst.OR(_pattern3, _pattern3, _wr),			# 	pattern3 += wr

# ドットマトリックスLEDの発光
Inst.SH(_addrBase, _pattern0, 0x40),		# [addrBase + 0x40] = pattern0
Inst.SH(_addrBase, _pattern1, 0x42),		# [addrBase + 0x42] = pattern1
Inst.SH(_addrBase, _pattern2, 0x44),		# [addrBase + 0x44] = pattern2
Inst.SH(_addrBase, _pattern3, 0x46),		# [addrBase + 0x46] = pattern3


# 得点処理
Inst.ADDI(_tmp, _num0, 0),
Inst.BNE(_posX, _tmp, 4 * 2),				# if posX == 0
Inst.ADDI(_score2, _score2, 1),				# 	score2 += 1
Inst.JAL(0, -4 * 79),										

Inst.ADDI(_tmp, _num0, 15),
Inst.BNE(_posX, _tmp, 4 * 2),				# if posX == 15
Inst.ADDI(_score1, _score1, 1),				# 	score1 += 1
Inst.JAL(0, -4 * 83),

Inst.ADDI(_counterX, _counterX, 1),
Inst.BNE(_counterX, _intervalX, 4 * 14),
Inst.ADDI(_counterX, _num0, 0),

# ボールの反射
# ボールの左バーでの反射
Inst.ADDI(_tmp, _num0, 2),
Inst.BNE(_posX, _tmp, 4 * 4),				# if posX == 2
Inst.BNE(_posY, _barY1u, 4),				# 	if posY == barY1
Inst.SUB(_velX, 0, _velX),					# 		velX = 0 - velX
Inst.BNE(_posY, _barY1d, 4),				# 	if posY == barY1
Inst.SUB(_velX, 0, _velX),					# 		velX = 0 - velX

# ボールの右バーでの反射
Inst.ADDI(_tmp, _num0, 13),
Inst.BNE(_posX, _tmp, 4 * 4),				# if posX == 13
Inst.BNE(_posY, _barY2u, 4),				# 	if posY == barY2
Inst.SUB(_velX, 0, _velX),					# 		velX = 0 - velX
Inst.BNE(_posY, _barY2d, 4),				# 	if posY == barY2
Inst.SUB(_velX, 0, _velX),					# 		velX = 0 - velX

# ボールの左右移動
Inst.ADD(_posX, _posX, _velX),				# posX += velX

Inst.ADDI(_counterY, _counterY, 1),
Inst.BNE(_counterY, _intervalY, 4 * 8),
Inst.ADDI(_counterY, _num0, 0),

# ボールの上反射
Inst.ADDI(_tmp, _num0, 0),
Inst.BNE(_posY, _tmp, 4),					# if posY == 0
Inst.SUB(_velY, 0, _velY),					# 	velY = 0 - velY

# ボールの下反射
Inst.ADDI(_tmp, _num0, 3),
Inst.BNE(_posY, _tmp, 4),				 	# if posY == 3
Inst.SUB(_velY, 0, _velY),					# 	velY = 0 - velY

Inst.ADD(_posY, _posY, _velY),				# posY += velY


# バーの座標設定
# 1P側上移動
Inst.LB(_tmp, _addrBase, 0x48),			# input = [addrBase + 0x48]
Inst.ANDI(_tmp, _tmp, 0b0000_0001),		# input &= 0b0000_0001
Inst.BEQ(_tmp, 0, 4 * 3),					# if input != 0
Inst.ADDI(_tmp, _num0, 1),
Inst.SUB(_barY1u, _barY1u, _tmp),			# 	barY1u -= num1
Inst.SUB(_barY1d, _barY1d, _tmp),			# 	barY1d -= num1

# 1P側上移動
Inst.LB(_tmp, _addrBase, 0x4b),			# input = [addrBase + 0x4b]
Inst.ANDI(_tmp, _tmp, 0b0000_0001),		# input &= 0b0000_0001
Inst.BEQ(_tmp, 0, 4 * 3),					# if input != 0
Inst.ADDI(_tmp, _num0, 1),
Inst.ADD(_barY1u, _barY1u, _tmp),			# 	barY1u += num1
Inst.ADD(_barY1d, _barY1d, _tmp),			# 	barY1d += num1

# 2P側上移動
Inst.LB(_tmp, _addrBase, 0x48),			# input = [addrBase + 0x48]
Inst.ANDI(_tmp, _tmp, 0b0001_0000),		# input &= 0b0001_0000
Inst.BEQ(_tmp, 0, 4 * 3),					# if input != 0
Inst.ADDI(_tmp, _num0, 1),
Inst.SUB(_barY2u, _barY2u, _tmp),			# 	barY2u -= num1
Inst.SUB(_barY2d, _barY2d, _tmp),			# 	barY2d -= num1

# 2P側下移動
Inst.LB(_tmp, _addrBase, 0x4b),			# input = [addrBase + 0x4b]
Inst.ANDI(_tmp, _tmp, 0b0001_0000),		# input &= 0b0001_0000
Inst.BEQ(_tmp, 0, 4 * 3),					# if input != 0
Inst.ADDI(_tmp, _num0, 1),
Inst.ADD(_barY2u, _barY2u, _tmp),			# 	barY2u += num1
Inst.ADD(_barY2d, _barY2d, _tmp),			# 	barY2d += num1

]


# 最後
finalize = [

# ループの先頭に戻る
Inst.JAL(0, -4 * ( len(game_loop) + 1 ) )

]


program = sys_init + game_init + game_loop + finalize

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
