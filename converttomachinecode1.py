# importing files
import globalss
from I_format import *
from R_format import *
from SSBU_format import *
from UJ_format import *


# fuctions
def getline():
    for each in file:
        return each


def ReservedWords(st):
    for each in globalss.RtypeWords:
        if each == st:
            return 1
    for each in globalss.ItypeWords:
        if each == st:
            return 2
    for each in globalss.StypeWords:
        if each == st:
            return 3
    for each in globalss.SBtypeWords:
        if each == st:
            return 4
    for each in globalss.UtypeWords:
        if each == st:
            return 5
    for each in globalss.UJtypeWords:
        if each == st:
            return 6
    if st == '.data':
        return 8
    elif st == '.text':
        return 7
    return -1


def R_Type_MC(each):
    rd = int(each[1][1:3])
    rs1 = int(each[2][1:3])
    rs2 = int(each[3][1:3])
    if each[0] == "add":
        li = add(rd, rs1, rs2)
    elif each[0] == "sub":
        li = sub(rd, rs1, rs2)
    elif each[0] == "sll":
        li = sll(rd, rs1, rs2)
    elif each[0] == "slt":
        li = slt(rd, rs1, rs2)
    elif each[0] == "xor":
        li = xoor(rd, rs1, rs2)
    elif each[0] == "srl":
        li = srl(rd, rs1, rs2)
    elif each[0] == "sra":
        li = sra(rd, rs1, rs2)
    elif each[0] == "or":
        li = oor(rd, rs1, rs2)
    elif each[0] == "and":
        li = aand(rd, rs1, rs2)
    elif each[0] == "mul":
        li = mul(rd, rs1, rs2)
    elif each[0] == "div":
        li = div(rd, rs1, rs2)
    elif each[0] == "rem":
        li = rem(rd, rs1, rs2)
    return li


def I_Type_MC(each):
    if each[0] == 'addi' or each[0] == 'ori' or each[0] == 'andi':
        rd = int(each[1][1:3])
        rs1 = int(each[2][1:3])
        imm = int(each[3])

        # for load and jalr instructions
    if each[0] == 'ld' or each[0] == 'lb' or each[0] == 'lh' or each[0] == 'lw' or each[0] == 'jalr':
        rd1 = int(each[1][1:3])
        i = 0
        imm1 = ''
        while each[2][i] != '(':
            imm1 = imm1 + each[2][i]
            i = i + 1
        i = 0
        while each[2][i] != 'x':
            i = i + 1
        i = i + 1
        rs11 = ''
        while each[2][i] != ')':
            rs11 = rs11 + each[2][i]
            i = i + 1
        rs11 = int(rs11)
        imm1 = int(imm1)

    if each[0] == "addi":
        li = addi(rd, rs1, imm)
    elif each[0] == "ori":
        li = ori(rd, rs1, imm)
    elif each[0] == "andi":
        li = andi(rd, rs1, imm)
    elif each[0] == "ld":
        li = ld(rd1, rs11, imm1)
    elif each[0] == "lb":
        li = lw(rd1, rs11, imm1)
    elif each[0] == "lh":
        li = lh(rd1, rs11, imm1)
    elif each[0] == "lw":
        li = lw(rd1, rs11, imm1)
    elif each[0] == "jalr":
        li = jalr(rd1, rs11, imm1)
    return li


def S_Type_MC(each):
    rs2 = each[1][1:3]
    i = 0
    imm = ''
    while each[2][i] != '(':
        imm = imm + each[2][i]
        i = i + 1
    i = 0
    while each[2][i] != 'x':
        i = i + 1
    i = i + 1
    rs1 = ''
    while each[2][i] != ')':
        rs1 = rs1 + each[2][i]
        i = i + 1
    rs1 = int(rs1)
    rs2 = int(rs2)
    imm = int(imm)
    if each[0] == "sb":
        li = sb(rs1, rs2, imm)
    elif each[0] == "sd":
        li = sd(rs1, rs2, imm)
    elif each[0] == "sh":
        li = sh(rs1, rs2, imm)
    elif each[0] == "sw":
        li = sw(rs1, rs2, imm)

    return li


def SB_Type_MC(each):
    rs1 = int(each[1][1:3])
    rs2 = int(each[2][1:3])
    i = 0
    imm = 0
    while i < len(globalss.name_label):
        if globalss.name_label[i] == str(each[3]):
            # print("yass is ")
            imm = int(globalss.PC_label[i]) - globalss.PC
            break
        i = i + 1
    imm = int(imm)
    # print('name is'+each[0])
    if each[0] == "beq":
        li = beq(rs1, rs2, imm)
    elif each[0] == "bne":
        li = bne(rs1, rs2, imm)
    elif each[0] == "blt":
        li = blt(rs1, rs2, imm)
    elif each[0] == "bge":
        li = bge(rs1, rs2, imm)
    return li


def U_Type_MC(each):
    if each[0] == 'auipc':
        if each[2][1] == 'x' or each[2][2] == 'x':  # to check if it is hex or not
            li = auipc(int(each[1][1:3]), int(each[2], 16))
        else:
            li = auipc(int(each[1][1:3]), each[2])
    elif each[0] == 'lui':
        rd = int(each[1][1:3])
        imm = int(each[2])
        # to check if it is hex or not
        li = lui(rd, imm)
    return li


def UJ_Type_MC(each):
    i = 0
    while i < len(globalss.name_label):
        if globalss.name_label[i] == each[2]:
            imm = globalss.PC_label[i]
            break
        i = i + 1
    imm = imm - globalss.PC
    li = jal(each[1][1:3], imm)
    return li


def memoryallocation(each):
    if each[1] == '.word':
        i = 2
        while (i < len(each)):
            globalss.memory_array.append(int(each[i]))
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            i = i + 1
        return
    elif each[1] == '.byte':
        i = 2
        while (i < len(each)):
            globalss.memory_array.append(int(each[i]))
            i = i + 1
        return
    elif each[1] == '.half':
        i = 2
        while (i < len(each)):
            globalss.memory_array.append(int(each[i]))
            globalss.memory_array.append(0)
            i = i + 1
        return
    elif each[1] == '.dword':
        i = 2
        while (i < len(each)):
            globalss.memory_array.append(int(each[i]))
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            globalss.memory_array.append(0)
            i = i + 1
        return
    elif each[1] == '.asciiz':
        i = 2
        string = ""
        while i < len(each):
            string = string + each[i]
            string = string + " "
            i = i + 1
        string = string[1:len(string) - 2]
        for i in string:
            globalss.memory_array.append(ord(i))
            # we have to load the complete ascii table which is to be done later
        return


def assign_labelled_instruction():
    file = open("assembly.txt", 'r')
    PC = 0
    flag = 0
    flag1 = 0
    for each in file:
        # print(each)
        each = each.split()
        if each[0] == '.text':
            flag1 = 0
            continue
        elif each[0] == '.data':
            flag1 = 1
            continue
        temp = ReservedWords(each[0])
        if temp == -1:
            if flag1 == 1:
                continue
            global PC_label
            global name_label
            globalss.PC_label.insert(0, PC)
            globalss.name_label.insert(0, each[0][0:len(each[0]) - 1])
        PC = PC + 4
    file.close()
    return


# main
def convert_to_machinecode():
    file = open("assembly.txt", 'r')
    file1 = open("machinecode.txt", 'w')
    flag = 0
    globalss.PC = 0

    for each in file:
        each = each.split();
        # print(each)
        # print(each)
        temp = ReservedWords(each[0])
        if temp == -1:
            if flag == 1:  # we have to allocate memory
                memoryallocation(each)
                continue
            file1.write(hex(int(globalss.PC)) + "\n")
            globalss.PC = globalss.PC + 4
            continue

            # it is a labeled instrution

            # it is R type instrution
        if temp == 1:
            li = R_Type_MC(each)
        elif temp == 2:
            li = I_Type_MC(each)
        elif temp == 3:
            li = S_Type_MC(each)
        elif temp == 4:
            li = SB_Type_MC(each)
        elif temp == 5:
            li = U_Type_MC(each)
        elif temp == 6:
            li = UJ_Type_MC(each)
        elif temp == 7:
            flag = 0  # if each[0] == .text
            continue
        elif temp == 8:  # if each[0]==.data
            flag = 1
            continue
        ans = ''
        for xx in li:
            ans = ans + str(xx)
        li = ans
        li = hex(int(li, 2))  # it contains the hex from of assembly instuction
        # print(li)
        file1.write(hex(int(globalss.PC)) + " " + li + "\n")

        globalss.PC = globalss.PC + 4
    file.close()
    file1.close()
