import linecache
import sys

from converttomachinecode1 import *
from decode1 import *
from error_handling import *
from execute0 import *
from fetch0 import *
from memoryaccess1 import *
from registerupdate1 import *


def myFunc():
    assign_labelled_instruction()
    globalss.assign_register()
    a = error_handling()
    if a == 1:
        print('not passed')
        sys.exit()
    print('passed')
    convert_to_machinecode()
    globalss.assign_memory()
    globalss.assign_stack()

    file2 = open('machinecode.txt', 'r')
    i = 1
    each = str(linecache.getline('machinecode.txt', i))  # Execution will be done now
    while each != '':
        print((each))
        global reg
        each = each.split()
        PC_Seq.append(globalss.PC_execution)  # new
        if (len(each) == 1):
            reg_step.append(register.tolist())  # new
            memory_step.append(memory_array.tolist())  # new
            globalss.PC_execution = globalss.PC_execution + 4
            i = int(globalss.PC_execution / 4) + 1
            each = (linecache.getline('machinecode.txt', i))
            continue
        lii = fetch(each)

        reg = decode(lii)
        reg = determine_exact_instruction(lii,
                                          reg)  # now exact instruction name will be appended #reg[rd,rs1,rs2,imm,type,oriname]

        reg = execute(reg)
        reg = memoryaccess(reg)  # a new value has been appended. We will use this value in regsiter update
        # reg[rd,rs1,rs2,imm,type,oriname,execute_result,memoryaccessreult]
        registerupdate(reg)

        print(reg)
        i = int(globalss.PC_execution / 4) + 1
        print(i)
        each = (linecache.getline('machinecode.txt', i))
        reg.clear()
        # print("Current register")
        # print(globalss.register)
        # print("Current memory")
        # print(globalss.memory_array)

        reg_step.append(register.tolist())  # new
        memory_step.append(memory_array.tolist())  # new
        # globalss.reg_step.append(globalss.register)
        # globalss.memory_step.append(globalss.memory_array)
        globalss.register[0] = 0
    file2.close()
    print(globalss.memory_array)
    print("$$$$$$$$$$$$$")
    print(PC_Seq)
    print(register)
    print("^^^^^^")
    print(reg_step)
    # print(memory_step)


if __name__ == '__main__':
    myFunc()
