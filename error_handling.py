from globalss import *
# error handling after .data directive
def error_handling():
    WORDS = ['add', 'and', 'or', 'sll', 'slt', 'sra', 'srl', 'sub', 'xor', 'mul', 'div', 'rem','addi', 'andi', 'ori', 'lb', 'lh', 'lw', 'jalr' ,'beq', 'bne', 'bge', 'blt' , 'sb', 'sw', 'sd', 'sh', 'auipc', 'lui' ,'jal']
    
    Words1=['add', 'and', 'or', 'sll', 'slt', 'sra', 'srl', 'sub', 'xor', 'mul', 'div', 'rem']
    Words2=['beq', 'bne', 'bge', 'blt']
    BracWords = ['sb', 'sw', 'sd', 'sh', 'lb', 'lh', 'lw', 'jalr']
    Words3=['addi', 'andi', 'ori']
    Words4=['auipc', 'lui']
    Words5=['jal']
    
    Labels=[]
    Labels = name_label #make labels list before generating .mc file
    Labelss = []
    for x in Labels:
        Labelss.append(x+':')
       
    validArg = ['x0','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16','x17','x18','x19','x20','x21','x22','x23','x24','x25','x26','x27','x28','x29','x30','x31']
    
    bracArg = ['(x0)', '(x1)', '(x2)', '(x3)', '(x4)', '(x5)', '(x6)', '(x7)', '(x8)', '(x9)', '(x10)', '(x11)', '(x12)', '(x13)', '(x14)', '(x15)', '(x16)', '(x17)', '(x18)', '(x19)', '(x20)', '(x21)', '(x22)', '(x23)', '(x24)', '(x25)', '(x26)', '(x27)', '(x28)', '(x29)', '(x30)', '(x31)' ]

    
    # s = "lw x1 0(x2)"
    # l = s.split()
    # print(l[2] in validArg)
    
    f = open("assembly.txt", "r")
    f2=0
    for x in f:
      lis = x.split()
      if len(lis)==0:
            continue
      ins = lis[0]
      if ins== '.data':
          f2=1
          continue
      if ins=='.text':
          f2=0
          continue
      if f2==1:
          continue
      if ins in Labelss:
            continue 
      if ins not in WORDS:
           print(ins + " instruction is not supported")
           return 1
    
      # 1 format
      if ins in Words1:
            if lis[1] not in validArg or lis[2] not in validArg or lis[3] not in validArg:
                    print(ins + " in incorrect format")
                    return 1
      # 2 format
      if ins in Words2:
            if lis[1] not in validArg or lis[2] not in validArg or lis[3] not in Labels:
                    print(ins + " in incorrect format (" + lis[3]+ " not defined)")
                    return 1
    
      # Brac format
      if ins in BracWords:
            if lis[1] not in validArg or lis[2] in validArg or lis[2] in bracArg:
                    print(ins + " in incorrect format (No offset given)")
                    return 1
    
      # 3 format
      if ins in Words3:
            if lis[1] not in validArg or lis[2] not in validArg or lis[3] in validArg:
                    print(ins +" in incorrect format ")
                    return 1
    
      # 4 format
      if ins in Words4:
            if lis[1] not in validArg or lis[2] in validArg:
                    print(ins + " in incorrect format")
                    return 1
    
      # 5 format
      if ins in Words5:
            if lis[1] not in validArg or lis[2] not in Labels :
                    print(ins + " in incorrect format")        
                    return 1
    
      
    f.close()
    return 0
    
