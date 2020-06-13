import array as arr

# GLOBAL VARIABLES

# for making .mc file
RtypeWords = ['add', 'and', 'or', 'sll', 'slt', 'sra', 'srl', 'sub', 'xor', 'mul', 'div', 'rem']
ItypeWords = ['addi', 'andi', 'ori', 'lb', 'ld', 'lh', 'lw', 'jalr']
StypeWords = ['sb', 'sw', 'sd', 'sh']
SBtypeWords = ['beq', 'bne', 'bge', 'blt']
UtypeWords = ['auipc', 'lui']
UJtypeWords = ['jal']
PC_label = []
name_label = []
PC = 0
PC_Seq = []
reg_step = []
memory_step = []

# buffer=-1
# register_file=-1
# particular_instruction=-1

memory_array = arr.array('i', [])
stack_array = arr.array('i', [])

stack_pointer = 10000

register = arr.array('i', [])
PC_execution = 0


def assign_register():
    q = 0
    while q < 32:
        register.append(0)
        q = q + 1
    return


def assign_memory():
    q = 0
    while q < 1000:  # -1 means that block of byte has not been used yet
        memory_array.append(-1)
        q = q + 1
    return


def assign_PC():
    PC_execution = 0
    return


def assign_stack():
    q = 0
    while q < 10001:
        stack_array.append(-1)
        q = q + 1
    return


# for reading .mc files

R = ['add', 'and', 'or', 'sll', 'slt', 'sra', 'srl', 'sub', 'xor', 'mul', 'div', 'rem']
I_1 = ['addi', 'andi', 'ori']
I_2 = ['lb', 'ld', 'lh', 'lw']
I_3 = ['jalr']
S = ['sb', 'sw', 'sd', 'sh']
SB = ['beq', 'bne', 'bge', 'blt']
U_lui = ['lui']
U_auipc = ['auipc']
UJ = ['jal']
reg = []

major_opcode_name = ['R', 'I_1', 'I_2', 'I_3', 'S', 'SB', 'U_lui', 'U_auipc', 'UJ']
major_opcode_value = ['0110011', '0010011', '0000011', '1100111', '0100011', '1100011', '0110111', '0010111', '1101111']

Rfun3 = ['000', '111', '110', '001', '010', '101', '101', '000', '100', '000', '100', '110']
Rfun7 = ['0000000', '0000000', '0000000', '0000000', '0000000', '0100000', '0000000', '0100000', '0000000', '0000001',
         '0000001', '0000001']

I_1fun3 = ['000', '111', '110']

I_2fun3 = ['000', '011', '001', '010']

Sfun3 = ['000', '010', '011', '001']

SBfun3 = ['000', '001', '101', '100']

# rough work
# import linecache
# line = linecache.getline('assembly.txt', 1)
# i=1
# while i<=16:
#   line = linecache.getline('assembly.txt', i)
#  print(line)
# i=i+1
