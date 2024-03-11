def extendbit(bin , digit):
    len = 0
    binary = ""
    for i in bin :
        len+=1

    for i in range (digit - len):
        binary += "0"

    binary += bin
    return binary

def two_compli(binary):
    length = len(binary)
    inverted = ''
    for bit in binary:
        inverted += '1' if bit == '0' else '0'

    carry = True
    result = ''
    for i in range(length - 1, -1, -1):
        if carry:
            if inverted[i] == '1':
                result = '0' + result
            else:
                result = '1' + result
                carry = False
        else:
            result = inverted[i] + result
    
    return result

def signed_binary(imm , digit):
    if imm < 0:
        num = imm * (-1)
        bi = bin(num)[2:]
        y = extendbit(bi , digit)
        x = two_compli(y)
        return '1' + x[1:]
    else :
        bi = bin(imm)[2:]
        y = extendbit(bi , digit)
        return '0' + y[1:]    

def Find_parts(s):
    L = []
    st = 0
    for i in range(len(s)):
        if s[i] == " " or s[i] == "," or s[i] == "(" or s[i] == ")":
            L.append(s[st:i])
            st = i+1
        if i==len(s)-1:
            L.append(s[st:i+1])
    return L

def lw(imm,rd,rs1):
    convert = signed_binary(imm,12)
    print(convert + rs1 + "010" + rd + "0000011")


def addi(imm,rd,rs1):
    convert = signed_binary(imm,12)
    print(convert + rs1 + "000" + rd + "0010011")

def sltiu(imm,rd,rs1):
    convert = signed_binary(imm,12)
    print(convert + rs1 + "011" + rd + "0010011")

def jalr(imm,rd,rs1):
    convert = signed_binary(imm,12)
    print(convert + rs1 + "000" + rd + "1100111")


def lui(imm,rd):
    convert = signed_binary(imm,20)
    print(convert + rd + "0110111")

def auipc(imm,rd):
    convert = signed_binary(imm,20)
    print(convert + rd + "0010111")

def beq(imm,rs1,rs2):
    num = signed_binary(imm,7)
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print(num + rs2 + rs1 + "000" + num + "1100011")

def bne(imm,rs1,rs2):
    num = signed_binary(imm,7)
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b') 
    print(num + rs2 + rs1 + "001" + num + "1100011")

def blt(imm,rs1,rs2):
    num = signed_binary(imm,7)
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print(num + rs2 + rs1 + "100" + num + "1100011")

def bge(imm,rs1,rs2):
    num = signed_binary(imm,7)
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print(num + rs2 + rs1 + "101" + num + "1100011")

def bltu(imm,rs1,rs2):
    num = signed_binary(imm,7)
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print(num + rs2 + rs1 + "110" + num + "1100011")

def bgeu(imm,rs1,rs2):
    num = signed_binary(imm,7)
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print(num + rs2 + rs1 + "111" + num + "1100011")    
            
def add(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "000" + rd + "0110011")

def sub(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b') 
    print("0100000" + rs2 + rs1 + "000" + rd + "0110011")

def sll(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "001" + rd + "0110011")

def slt(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "010" + rd + "0110011")

def sltu(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "011" + rd + "0110011")

def xor(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "100" + rd + "0110011")

def srl(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "101" + rd + "0110011")

def instruc_or(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "110" + rd + "0110011")
def instruc_and(rd,rs1,rs2):
    rd = format(int(parts[1][1:]),'05b')
    rs1 = format(int(parts[2][1:]),'05b')
    rs2 = format(int(parts[3][1:]),'05b')
    print("0000000" + rs2 + rs1 + "111" + rd + "0110011")     

def jal(imm,rd):
    num = signed_binary(imm,12)
    rd = format(int(parts[2][1:]),'05b')
    print(num + rd + "1101111")

def s(imm, rs2, rs1):
    imm = signed_binary(imm, 12)
    print(imm + rs2 + rs1 + "010" + "0000011" + imm[11:])

registers = {'zero': '0', 'ra': '00001', 'sp': '00010', "gp": '00011', 'tp': '00100', 't0':'00101', 't1': '00110', 't2': '00111','s0': '01000', 'fp': '01000', 's1': '01001', 'a0': '01010', 'a1': '01011','a2':'01100', 'a3':'01101','a4':'01110', 'a5':'01111', 'a6':'10000',  'a7':'10001', 's2': '10010', 's3': '10011', 's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011', 't3': '11100', 't4': '11101', 't5':'11110', 't6': '11111'}

f = open("C:\\Users\LENOVO\Desktop\CO GP\p_test_cases.txt", "r")
for l in f:
    parts = Find_parts(l)
    if parts[0]=="lw":
        lw(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="addi":
        addi(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))
    elif parts[0]=="sltiu":
        sltiu(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))
    elif parts[0]=="jalr":
        jalr(int(parts[3]),registers.get(parts[1]),registers.get(parts[2])) #till here for i type
    elif parts[0]=="lui":
        lui(int(parts[2]),registers.get(parts[1]))    
    elif parts[0]=="auipc":
        lui(int(parts[2]),registers.get(parts[1]))        # till here for u type     
    elif parts[0]=="beq":
        beq(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="bne":
        bne(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="blt":
        blt(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="bge":
        bge(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="bltu":
        bltu(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))
    elif parts[0]=="bgeu":
        bgeu(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))    #till b type
    elif parts[0]=="add":
        add(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="sub":
        sub(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="sll":
        sll(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="slt":
        slt(int(parts[2]),registers.get(parts[1]),registers.get(parts[3]))
    elif parts[0]=="sltu":
        sltu(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))
    elif parts[0]=="xor":
        xor(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))
    elif parts[0]=="srl":
        srl(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))
    elif parts[0]=="or":
        instruc_or(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))
    elif parts[0]=="and":
        instruc_and(int(parts[3]),registers.get(parts[1]),registers.get(parts[2]))    # till r type
    elif parts[0]=="jal":
        jal(int(parts[2]),registers.get(parts[1]),registers.get(parts[3])) # till j type
    elif parts[0]=="s":
        s(int(parts[2]), registers.get(parts[1]), registers.get(parts[3]))
    else:
        print("Error")                                                         








    

