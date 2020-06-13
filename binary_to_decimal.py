def binary_2_decimal(imm):
    if imm[0] == '0':
        return int(imm, 2)
    n = len(imm)
    i = n - 1
    while (i >= 0):
        if (imm[i] == '1'):
            break
        i -= 1
    if (i == -1):
        return '1' + imm
    k = i - 1
    while (k >= 0):

        if (imm[k] == '1'):
            imm = list(imm)
            imm[k] = '0'
            imm = ''.join(imm)
        else:
            imm = list(imm)
            imm[k] = '1'
            imm = ''.join(imm)

        k -= 1
        ans = int(imm, 2)
    return -1 * ans
