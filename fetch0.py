import globalss


def fetch(each):
    li = "{0:08b}".format(int(each[1], 16))

    length = len(li)
    i = 32 - length
    lii = ''
    while i > 0:
        lii = lii + '0'
        i = i - 1
    lii = lii + li
    # our lii contain binary string of length 32
    if lii[25:32] == '1100111' or lii[25:32] == '1100011' or lii[25:32] == '1101111':
        return lii
    globalss.PC_execution = globalss.PC_execution + 4
    return lii
