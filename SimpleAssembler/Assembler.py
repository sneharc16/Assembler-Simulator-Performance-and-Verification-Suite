import sys
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 Assembler.py <input_assembly_code_file_path> <output_machine_code_file_path>")
        return

    inputFilePath = sys.argv[1]
    outputFilePath = sys.argv[2]

    if not os.path.exists(inputFilePath):
        print(f"Error: Input file '{inputFilePath}' not found.")
        return

    isaDesc = {
        "add" : {"type":"R" , "bin": "0110011", "funct3" : "000", "funct7" : "0000000"},
        "sub" : {"type":"R" , "bin": "0110011", "funct3" : "000", "funct7" : "0100000"},
        "sll" : {"type":"R" , "bin": "0110011", "funct3" : "001", "funct7" : "0000000"},
        "slt" : {"type":"R" , "bin": "0110011", "funct3" : "010", "funct7" : "0000000"},
        "sltu" : {"type":"R" , "bin": "0110011", "funct3" : "011", "funct7" : "0000000"},
        "xor" : {"type":"R" , "bin": "0110011", "funct3" : "100", "funct7" : "0000000"},
        "srl" : {"type":"R" , "bin": "0110011", "funct3" : "101", "funct7" : "0000000"},
        "or" : {"type":"R" , "bin": "0110011", "funct3" : "110", "funct7" : "0000000"},
        "and" : {"type":"R" , "bin": "0110011", "funct3" : "111", "funct7" : "0000000"},

        "lw" : {"type":"I" , "bin": "0000011", "funct3" : "010"},
        "addi" : {"type":"I" , "bin": "0010011", "funct3" : "000"},
        "sltiu" : {"type":"I" , "bin": "0010011", "funct3" : "011"},
        "jalr" : {"type":"I" , "bin": "1100111", "funct3" : "000"},

        "sw" : {"type":"S" , "bin": "0100011", "funct3" : "010"},

        "beq" : {"type":"B" , "bin": "1100011", "funct3" : "000"},
        "bne" : {"type":"B" , "bin": "1100011", "funct3" : "001"},
        "blt" : {"type":"B" , "bin": "1100011", "funct3" : "100"},
        "bge" : {"type":"B" , "bin": "1100011", "funct3" : "101"},
        "bltu" : {"type":"B" , "bin": "1100011", "funct3" : "110"},
        "bgeu" : {"type":"B" , "bin": "1100011", "funct3" : "111"},

        "lui" : {"type":"U" , "bin": "0110111"},
        "auipc" : {"type":"U" , "bin": "0010111"},

        "jal" : {"type":"J" , "bin": "1101111"},

        "mul" : {"type":"E", "bin": "1000001", "funct3" : "000", "funct7" : "0000000"},

        "rst" : {"type":"F", "bin": "1000010"},
        "halt": {"type":"F", "bin": "1000011"},

        "rvrs": {"type":"G", "bin": "1000100", "funct3": "000", "funct7" : "0000000"}
        
    }

    regDesc={ 
        "zero": "00000", 
        "ra": "00001",
        "sp": "00010",
        "gp": "00011",
        "tp": "00100",
        "t0": "00101",
        "t1": "00110",
        "t2": "00111",
        "s0": "01000",
        "fp": "01000",
        "s1": "01001",
        "a0": "01010",
        "a1": "01011",
        "a2": "01100",
        "a3": "01101",
        "a4": "01110",
        "a5": "01111",
        "a6": "10000",
        "a7": "10001",
        "s2": "10010",
        "s3": "10011",
        "s4": "10100",
        "s5": "10101",
        "s6": "10110",
        "s7": "10111",
        "s8": "11000",
        "s9": "11001",
        "s10": "11010",
        "s11": "11011",
        "t3": "11100",
        "t4": "11101",
        "t5": "11110",
        "t6": "11111",

    }
    def readFile():
        file = open(inputFilePath,"r")
        f = file.readlines()
        for each in f:
            if(each[-1] == "\n"):
                each = each[0:(len(each)-1)]
            commands.append(each)
        file.close()


    def DecimalToBinary(num,k):
        n=num
        if num<0:
            n=num*(-1)
        s=""
        while n>=1:
            s+=str(n%2)
            n=n//2
        s=s[::-1]
        l=len(s)
        if l<=k:
            str1="0"*(k-l)
            s=str1+s
            l= k

            str2=""
            if num<0:
                for i in range(l):
                    if s[i]=="0":
                        str2+="1"
                    else:
                        str2+="0"
                temp=list(str2)
                for i in range(len(temp)-1,-1,-1):
                    if str2[i]=="1":
                        temp[i]="0"
                    else:
                        temp[i]="1"
                        break
                s=""
                for i in temp:
                    s+=i
            return s 
        
        else:
            return "FLAG"

    def splitBracket(n):
        count=0
        for i in range(len(n)):
            count+=1
            if n[i]== "(":
                index=count
                break
        str1= n[:index-1]
        str2= n[index:-1]
        
        return (str1,str2)


    commands = []
    readFile()
    ProgramCounter = 0
    labelDict = {}
    ifHalt = 0
    errorFlag = 0
    HaltFlag=0
    finalBinList = []
    #print(commands)

    for i in commands:

        SplitCommands = i.strip()
        
        if len(SplitCommands) == 0:
            continue
        
        SplitCommands = i.split(",")
        for j in range(len(SplitCommands)):
            SplitCommands[j] = SplitCommands[j].strip()
        CheckVal = SplitCommands[0]
        CheckVal = CheckVal.split(" ")

        if len(CheckVal) == 3:
            labelDict[(CheckVal[0][0:-1])] = ProgramCounter

    for i in commands:
        SplitCommands = i.strip()
        
        if len(SplitCommands) == 0:
            continue
        
        SplitCommands = i.split(",")
        for j in range(len(SplitCommands)):
            SplitCommands[j] = SplitCommands[j].strip()
        CheckVal = SplitCommands[0]
        CheckVal = CheckVal.split(" ")

        if len(CheckVal) == 3:
            CheckVal.pop(0)

        if len(CheckVal) > 1:
            FirstValue = CheckVal[1]           # first instruction parameter
            FinalParamList = [FirstValue]
            for k in range(len(SplitCommands)-1):
                FinalParamList.append(SplitCommands[k+1])

        InstructionVal = CheckVal[0]       #Instruction for Command : Example add, sub, mul etc.
        
        if InstructionVal not in isaDesc.keys():
            errorFlag=1
            return ("Error in Instruction Name in line ", ProgramCounter+1)
            
        
        #print(InstructionVal)
        #print(FinalParamList)

        for j in range(len(isaDesc.keys())):
            if list(isaDesc.keys())[j] == InstructionVal:
                valDict = list(isaDesc.values())[j]     # Puts Instruction Details in a new dictionary
                break

        finalBin = ""
        
        if valDict["type"] == "R":
            if FinalParamList[0] not in regDesc.keys() or FinalParamList[1] not in regDesc.keys() or FinalParamList[2] not in regDesc.keys():
                errorFlag=1
                return ("Error in Register Name in line ", ProgramCounter+1)
                
            
            opcode = valDict["bin"]
            funct3 = valDict["funct3"]
            funct7 = valDict["funct7"]
            rd = regDesc[FinalParamList[0]]
            rs1 = regDesc[FinalParamList[1]]
            rs2 = regDesc[FinalParamList[2]]

            finalBin = funct7 + rs2 + rs1 + funct3 + rd + opcode

        if valDict["type"] == "I":

            if valDict["funct3"] == "010":

                immediateVal, rstemp = splitBracket(FinalParamList[1])

                if rstemp not in regDesc.keys() or FinalParamList[0] not in regDesc.keys():
                    errorFlag=1
                    return ("Error in Register Name in line ", ProgramCounter+1)
                    
                
                else:
                    rs = regDesc[rstemp]
                    binNumtemp = DecimalToBinary(int(immediateVal),12)

                
                
            else:

                if FinalParamList[0] not in regDesc.keys() or FinalParamList[1] not in regDesc.keys():
                    errorFlag=1
                    return ("Error in Register Name in line ", ProgramCounter+1)
                    


                binNumtemp = DecimalToBinary(int(FinalParamList[2]),12)   # sign extension needs to be done and two's complement if negative.
                rs = regDesc[FinalParamList[1]]

            opcode = valDict["bin"]
            funct3 = valDict["funct3"]
            rd = regDesc[FinalParamList[0]]
            
            
            if binNumtemp == "FLAG":
                errorFlag = 1
                return ("Illegal Action: Immediate length out of bound on line:", commands.index(i)+1)
                
        
            finalBin = binNumtemp + rs + funct3 + rd + opcode
            
        if valDict["type"]=="S":
            
            
            immediateVal, rstemp = splitBracket(FinalParamList[1])

            if FinalParamList[0] not in regDesc.keys() or rstemp not in regDesc.keys():
                errorFlag=1
                return ("Error in Register Name in line ", ProgramCounter+1)
                

            else:
                rs1 = regDesc[rstemp]
                binNumtemp = DecimalToBinary(int(immediateVal),12)
            
            str1=str(binNumtemp)
            a=""
            b=""
            for j in range(7):
                a+=str1[j]
            for j in range(7,12):
                b+=str1[j]
            
            opcode = valDict["bin"]
            funct3 = valDict["funct3"]
            rs2 = regDesc[FinalParamList[0]]
            
            if binNumtemp == "FLAG":
                errorFlag = 1
                return ("Illegal Action: Immediate length out of bound on line:", commands.index(i)+1)
                
            
            finalBin = a + rs2 + rs1 + funct3 + b + opcode
            
        if valDict["type"]=="U":
            
            opcode = valDict["bin"]
            rd = regDesc[FinalParamList[0]]
            binNumtemp = DecimalToBinary(int(FinalParamList[1]),32)
            
            str1 = str(binNumtemp)
            a=""
            for j in range(0,20):
                a+=str1[j]
            
            if FinalParamList[0] not in regDesc.keys():
                errorFlag=1
                return ("Error in Register Name in line ", ProgramCounter+1)
                
            
            finalBin = a + rd + opcode

        
        if valDict["type"]=="J":
            
            if FinalParamList[0] not in regDesc.keys():
                errorFlag=1
                return ("Error in Register Name in line ", ProgramCounter+1)
                
            
            tempVal = FinalParamList[1]
            asciiFlag = 0
            for i in range(len(tempVal)):
                if tempVal[i] == "-":
                    asciiFlag += 1
                asciiVal = ord(tempVal[i])
                if asciiVal >= 48 and asciiVal <= 57:
                    asciiFlag += 1

            if FinalParamList[1] not in labelDict.keys() and asciiFlag == len(tempVal):
                binNumtemp = DecimalToBinary(int(FinalParamList[1]),20)
            
            elif tempVal in labelDict.keys():
                tempVal = FinalParamList[1]
                labelPos = labelDict[tempVal]
                labelPos = int(labelPos)
                newProgCount = ProgramCounter - labelPos
            
                binNumtemp = DecimalToBinary(newProgCount, 20)
            
            else:
                errorFlag = 1
                return ("Label Name is Incorrect in Line:", ProgramCounter+1)
                


            if binNumtemp == "FLAG":
                    errorFlag = 1
                    return ("Illegal Action: Immediate length out of bound on line:", commands.index(i)+1)
                    
            

            c = binNumtemp[0]
            b=binNumtemp[9:19]
            a = binNumtemp[11]
            d=binNumtemp[0:8]

            rd = regDesc[FinalParamList[0]]
            opcode = valDict["bin"]
            
            finalBin = c + b + a + d + rd + opcode


        if valDict["type"]=="B":
            
            if FinalParamList[0] not in regDesc.keys() or FinalParamList[1] not in regDesc.keys():
                errorFlag=1
                return ("Error in Register Name in line ", ProgramCounter+1)
                

            

            rs1=regDesc[FinalParamList[0]]
            rs2=regDesc[FinalParamList[1]]
            tempVal = FinalParamList[2]

            if InstructionVal == "beq" and rs1 == "00000" and rs2 == "00000" and tempVal == "0":
                opcode = valDict["bin"]
                funct3 = valDict["funct3"]
                b = "0"
                c = "0"
                a = "0"*6
                d = "0"*4

                if ProgramCounter!=len(commands)-1 and errorFlag==0:
                    errorFlag=1
                    return ("Assembly Code doesn't have Virtual Halt Instruction as the last instruction")
                    

                finalBin = b + a + rs2 + rs1 + funct3 + d + c + opcode
                finalBinList.append(finalBin)

                ifHalt = 1
                break

            asciiFlag = 0
            for i in range(len(tempVal)):
                if tempVal[i] == "-":
                    asciiFlag += 1
                asciiVal = ord(tempVal[i])
                if asciiVal >= 48 and asciiVal <= 57:
                    asciiFlag += 1

            if tempVal not in labelDict.keys() and asciiFlag == len(tempVal) :
                binNumtemp = DecimalToBinary(int(tempVal), 12)


            elif tempVal in labelDict.keys():
                labelPos = labelDict[tempVal]
                labelPos = int(labelPos)
                newProgCount = ProgramCounter - labelPos
                
                binNumtemp = DecimalToBinary(newProgCount, 12)
            
            else:
                errorFlag = 1
                return ("Label Name is Incorrect in Line:", ProgramCounter+1)
                
            
            

            opcode = valDict["bin"]
            funct3 = valDict["funct3"]

            # binNumtemp = DecimalToBinary(int(FinalParamList[2]),13)

            a=binNumtemp[1:7]
            b=binNumtemp[0]
            c=binNumtemp[1]
            d=binNumtemp[7:11]
            
            if binNumtemp == "FLAG":
                errorFlag = 1
                return ("Illegal Action: Immediate length out of bound on line:", commands.index(i)+1)
                

            finalBin = b + a + rs2 + rs1 + funct3 + d + c + opcode

        if valDict["type"] == "E":
            
            if FinalParamList[0] not in regDesc.keys() or FinalParamList[1] not in regDesc.keys() or FinalParamList[2] not in regDesc.keys():
                errorFlag=1
                return ("Error in Register Name in line ", ProgramCounter+1)
                
            
            opcode = valDict["bin"]
            funct3 = valDict["funct3"]
            funct7 = valDict["funct7"]
            rd = regDesc[FinalParamList[0]]
            rs1 = regDesc[FinalParamList[1]]
            rs2 = regDesc[FinalParamList[2]]

            finalBin = funct7 + rs2 + rs1 + funct3 + rd + opcode
        
        if valDict["type"] == "F":
            opcode = valDict["bin"]
            restBin = "0"*25

            finalBin = restBin + opcode

        if valDict["type"] == "G":
            
            if FinalParamList[0] not in regDesc.keys() or FinalParamList[1] not in regDesc.keys():
                errorFlag=1
                return ("Error in Register Name in line ", ProgramCounter+1)
            
            opcode = valDict["bin"]
            funct3 = valDict["funct3"]
            funct7 = valDict["funct7"]
            rd = regDesc[FinalParamList[0]]
            rs1 = regDesc[FinalParamList[1]]
            restBin = "0"*5

            finalBin = funct7 + restBin + rs1 + funct3 + rd + opcode
        
        
        finalBinList.append(finalBin)

        ProgramCounter += 1


    f = open(outputFilePath, "w")
    for i in finalBinList:
        f.write(i + "\n")
    f.close()

    if ifHalt == 0 and errorFlag == 0:
        return ("Assembly Code Missing Virtual Halt Instruction")



main()
