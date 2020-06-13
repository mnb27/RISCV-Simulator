def binary12(num):
    li = []
    if num >= 0:

        for i in range(0, 12):
            li.insert(0, int(num % 2))
            num = int(num / 2)
    else:
        num3 = 4096 + num
        for i in range(0, 12):
            li.insert(0, int(num3 % 2))
            num3 = int(num3 / 2)
    return li


def binary5(num):
    li = []
    for i in range(0, 5):
        li.insert(0, int(num % 2))
        num = int(num / 2)

    return li


def addi(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []
    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(0)
    li.append(0)
    li.append(0)

    li[20:24] = s3
    # insert opcode
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)

    return li


def ori(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []

    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(1)
    li.append(1)
    li.append(0)
    li[20:24] = s3
    # insert opcode
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)

    return li


def andi(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []
    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(1)
    li.append(1)
    li.append(1)

    li[20:24] = s3
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)

    # insert opcode
    return li


def ld(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []
    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(0)
    li.append(1)
    li.append(1)

    li[20:24] = s3
    # insert opcode
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)

    return li


def lb(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []
    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(0)
    li.append(0)
    li.append(0)

    li[20:24] = s3
    # insert opcode
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)
    return li


def lh(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []
    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(0)
    li.append(0)
    li.append(1)

    li[20:24] = s3
    # insert opcode
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)
    return li


def lw(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []
    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(0)
    li.append(1)
    li.append(0)

    li[20:24] = s3
    # insert opcode
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)
    return li


def jalr(rd, rs1, imm):
    s1 = binary5(rs1)
    s2 = binary12(imm)
    s3 = binary5(rd)
    li = []
    # insert funct3
    li[0:11] = s2
    li[12:16] = s1
    li.append(0)
    li.append(0)
    li.append(0)

    li[20:24] = s3
    # insert opcode
    li.append(1)
    li.append(1)
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)
    li.append(1)

    return li
