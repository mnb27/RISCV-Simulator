from binary_to_decimal import *
from globalss import *


def decode(lii):
    global reg
    # print(lii)
    i = 0
    typee = ''
    while i < len(major_opcode_value):
        if major_opcode_value[i] == str(lii[25:32]):
            typee = major_opcode_name[i]
        i = i + 1
    # print(typee)
    # typee has been obtained in typee        
    if typee == 'R':
        reg.append(int(lii[20:25], 2))
        reg.append(int(lii[12:17], 2))
        reg.append(int(lii[7:12], 2))
        reg.append(-1)
        reg.append('R')
    elif typee == 'I_1':
        reg.append(int(lii[20:25], 2))
        reg.append(int(lii[12:17], 2))
        reg.append(-1)
        reg.append(binary_2_decimal(lii[0:12]))
        reg.append('I_1')
    elif typee == 'I_2':
        reg.append(int(lii[20:25], 2))
        reg.append(int(lii[12:17], 2))
        reg.append(-1)
        reg.append(binary_2_decimal(lii[0:12]))
        reg.append('I_2')
    elif typee == 'I_3':
        reg.append(int(lii[20:25], 2))
        reg.append(int(lii[12:17], 2))
        reg.append(-1)
        reg.append(binary_2_decimal(lii[0:12]))
        reg.append('I_3')
    elif typee == 'S':
        reg.append(-1)
        reg.append(int(lii[12:17], 2))
        reg.append(int(lii[7:12], 2))
        reg.append(binary_2_decimal(lii[20:25] + lii[0:7]))
        reg.append('S')
    elif typee == 'SB':
        reg.append(-1)
        reg.append(int(lii[12:17], 2))
        reg.append(int(lii[7:12], 2))
        reg.append(2 * binary_2_decimal(lii[20:24] + lii[1:7] + lii[24:25] + lii[0:1]))
        reg.append('SB')
    elif typee == 'U_lui':
        reg.append(int(lii[20:25], 2))
        reg.append(-1)
        reg.append(-1)
        reg.append(lii[0:20])
        reg.append('U_lui')
    elif typee == 'U_auipc':
        reg.append(int(lii[20:25], 2))
        reg.append(-1)
        reg.append(-1)
        reg.append(binary_2_decimal(lii[0:20]))
        reg.append('U_auipc')
    elif typee == 'UJ':
        reg.append(int(lii[20:25], 2))
        reg.append(-1)
        reg.append(-1)
        reg.append(2 * binary_2_decimal(lii[0:20]))
        reg.append('UJ')
    return reg


def determine_exact_instruction(lii, reg):
    # reg=[rd,rs1,rs2,imm,type]
    i = 0
    if reg[4] == 'R':
        while i < len(R):
            if lii[17:20] == Rfun3[i] and lii[0:7] == Rfun7[i]:
                reg.append(R[i])
                break
            i = i + 1
    elif reg[4] == 'I_1':
        while i < len(I_1):
            if lii[17:20] == I_1fun3[i]:
                reg.append(I_1[i])
                break
            i = i + 1

    elif reg[4] == 'I_2':
        while i < len(I_2):
            if lii[17:20] == I_2fun3[i]:
                reg.append(I_2[i])
                break
            i = i + 1

    elif reg[4] == 'I_3':
        reg.append('jalr')

    elif reg[4] == 'S':
        while i < len(S):
            if lii[17:20] == Sfun3[i]:
                reg.append(S[i])
                break
            i = i + 1

    elif reg[4] == 'SB':
        while i < len(SB):
            if lii[17:20] == SBfun3[i]:
                reg.append(SB[i])
                break
            i = i + 1

    elif reg[4] == 'U_lui':
        reg.append('lui')

    elif reg[4] == 'U_auipc':
        reg.append('auipc')

    elif reg[4] == 'UJ':
        reg.append('jal')

    return reg
