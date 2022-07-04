#This works like a re-pattern to search for strings
#@author Jinyao Xu
#@category _NEW_
#@keybinding 
#@menupath Tools.Misc.Find_String
#@toolbar 


#TODO Add User Code Here

search = askString("Text Search", "Enter search string: ");
addr = find(search);
if addr != None:
	print("Search match found at {}".format(str(addr)))
	goTo(addr)
else:
	print("No search matched found.")
