#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here
from ghidra.program.model.listing import CodeUnitFormat, CodeUnitFormatOptions
from ghidra.program.model.symbol import RefType
codeUnitFormat = CodeUnitFormat(CodeUnitFormatOptions(CodeUnitFormatOptions.ShowBlockName.ALWAYS,CodeUnitFormatOptions.ShowNamespace.ALWAYS,"",True,True,True,True,True,True,True))
addr = currentAddress

limiter = 0
instruction = currentProgram.getListing().getInstructionAt(addr)
head=str(instruction)[0:4]

if(head=="CALL"):
	dest_addr = toAddr(int(str(instruction)[7:],16)) #Go to call's location
	sym = currentProgram.symbolTable.getPrimarySymbol(dest_addr)
	print("Call Detected for {}\n".format(str(sym)))
	instruction = currentProgram.getListing().getInstructionAt(dest_addr)
	print(instruction)
	while(str(instruction)[0:3]!="RET"):
		instruction = instruction.getNext()
		print(instruction)
	print("program done")

else:print("Not a Call---->Cannot Expand")
