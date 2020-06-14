import globalss
from I_phase2 import *
from R_phase2 import *
from SSBU_phase2 import *


# from UJ_phase2 import *

def execute(reg):
    # reg[rd,rs1,rs2,imm,type,oriname]
    if reg[4] == 'R':
        if reg[5] == 'add':
            reg.append(addinst(reg[1], reg[2]))
        elif reg[5] == 'and':
            reg.append(andinst(reg[1], reg[2]))
        elif reg[5] == 'or':
            reg.append(orinst(reg[1], reg[2]))
        elif reg[5] == 'sll':
            reg.append(sllinst(reg[1], reg[2]))
        elif reg[5] == 'slt':
            reg.append(sltinst(reg[1], reg[2]))
        elif reg[5] == 'sra':
            reg.append(srainst(reg[1], reg[2]))
        elif reg[5] == 'srl':
            reg.append(srlinst(reg[1], reg[2]))
        elif reg[5] == 'sub':
            reg.append(subinst(reg[1], reg[2]))
        elif reg[5] == 'xor':
            reg.append(xorinst(reg[1], reg[2]))
        elif reg[5] == 'mul':
            reg.append(mulinst(reg[1], reg[2]))
        elif reg[5] == 'div':
            reg.append(divinst(reg[1], reg[2]))
        elif reg[5] == 'rem':
            reg.append(reminst(reg[1], reg[2]))

    elif reg[4] == 'I_1':
        if reg[5] == 'addi':
            reg.append(addiinst(reg[1], reg[3]))  # reg[3] is immediate
        elif reg[5] == 'andi':
            reg.append(andiinst(reg[1], reg[3]))
        elif reg[5] == 'ori':
            reg.append(oriinst(reg[1], reg[3]))

    elif reg[4] == 'I_2':
        if reg[5] == 'lb':
            reg.append(lbinst(reg[1], reg[3]))
        elif reg[5] == 'ld':
            reg.append(ldinst(reg[1], reg[3]))
        elif reg[5] == 'lh':
            reg.append(lhinst(reg[1], reg[3]))
        elif reg[5] == 'lw':
            reg.append(lwinst(reg[1], reg[3]))

    elif reg[4] == 'I_3':
        if reg[5] == 'jalr':
            reg.append(jalrinst(reg[1], reg[3]))
            globalss.PC_execution = reg[6]

    elif reg[4] == 'S':
        if reg[5] == 'sb':
            reg.append(sbinst(reg[1], reg[3]))  # sending rs1 and imm
        elif reg[5] == 'sw':
            reg.append(swinst(reg[1], reg[3]))
        elif reg[5] == 'sd':
            reg.append(sdinst(reg[1], reg[3]))
        elif reg[5] == 'sh':
            reg.append(shinst(reg[1], reg[3]))

    elif reg[4] == 'SB':
        if reg[5] == 'beq':
            reg.append(beqinst(reg[1], reg[2]))
        elif reg[5] == 'bne':
            reg.append(bneinst(reg[1], reg[2]))
        elif reg[5] == 'bge':
            reg.append(bgeinst(reg[1], reg[2]))
        elif reg[5] == 'blt':
            reg.append(bltinst(reg[1], reg[2]))
        if reg[6] == 1:
            globalss.PC_execution = globalss.PC_execution + reg[3]
        else:
            globalss.PC_execution = globalss.PC_execution + 4

    elif reg[4] == 'U_lui':
        if reg[5] == 'lui':
            reg.append(luiinst(reg[3]))  # it is incomplete

    elif reg[4] == 'U_auipc':
        if reg[5] == 'auipc':
            reg.append(auipcinst(reg[3]))


    elif reg[4] == 'UJ':
        if reg[5] == 'jal':
            reg.append(globalss.PC_execution + 4)
            globalss.PC_execution = globalss.PC_execution + reg[3]
            # it is incomplete
    return reg
