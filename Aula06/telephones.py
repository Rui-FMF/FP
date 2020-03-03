
# Convert a telephone number into corresponding name, if on list.
# (If not on list, just return the number itself.)
def telToName(tel, telList, nameList):
	if tel in telList:
		name = nameList[telList.index(tel)]
		return name
	return tel


# Return list of telephone numbers corresponding to names containing partName.
def nameToTels(partName, telList, nameList):
	tels = []
	for x in nameList:
		if partName in x:
			tels.append(telList[nameList.index(x)])
	return tels


# Lists of telephone numbers and names
telList = ['975318642', '234000111', '777888333', '911911911']
nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']
print(telList["911911911"])

# Test telToName:
tel = input("Tel number? ")
print( telToName(tel, telList, nameList) )
print( telToName('234000111', telList, nameList) == "Brad" )
print( telToName('222333444', telList, nameList) == "222333444" )

# Test nameToTels:
name = input("Name? ")
print( nameToTels(name, telList, nameList) )
print( nameToTels('Clau', telList, nameList) == ['777888333'] )
print( nameToTels('Br', telList, nameList) == ['234000111', '911911911'] )

