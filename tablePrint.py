
# funcion to print basic element like int, string, etc..
# not including dict and classes
def tablePrintBasic(array, splitter = "|"):
    maxLength = 0
    string = ""

    # get the max length from values
    for a in array:
        if len(str(a)) > maxLength:
            maxLength = len(str(a))

    # creating the header from the type
    header = str(type(array[0])).split("'")[1]

    # if length of the header greater than values
    # it becomes the longer one
    if len(header) > maxLength:
        maxLength = len(header)

    # printing the header section
    string += printLine(maxLength+2)
    string += splitter + " " + printHeaderCol(header, maxLength) + " " + splitter + "\n"
    string += printLine(maxLength+2)
    
    # printing each line of the array
    for a in array:
        string += splitter + " " + printHeaderCol(str(a), maxLength) + " " + splitter + "\n"

    # closing the array 
    string += printLine(maxLength+2)
    print(string)


# function to print dictionnary elements
# all dictionnary can have different keys
def tablePrintDict(array, splitter = "|"):
    keys = []
    lengthKeys = {}
    string = ""
    
    # getting the total list of different keys 
    # from all the elements
    for a in array:
        for k in a.keys():
            if not k in keys:
                keys.append(k)

    # for each key of the list we are getting
    # the maximum length of the values
    for k in keys:
        # we are adding the key in length key dictionnary
        if k not in lengthKeys:
            lengthKeys[k] = 0
        # we are checking if the length of the value is 
        # greater than the actual max length for the key
        for a in array:
            if len(str(a.get(k, ''))) > lengthKeys[k]:
                lengthKeys[k] = len(str(a.get(k, '')))

    # for each key we are checking that the key name
    # is longer or not from de maximum length of the values
    for k in lengthKeys:
        if len(str(k)) > lengthKeys[k]:
            lengthKeys[k] = len(str(k))

    # we are summing the length to have the full lie length 
    # for the table
    total = 0
    for k in lengthKeys:
        total += lengthKeys[k] + 2
    total += len(keys)-1

    # printing the header section
    string += printLine(total)
    for k in lengthKeys:
        string += splitter + " " + printHeaderCol(str(k), lengthKeys[k]) + " "
    string += splitter + "\n"
    string += printLine(total)

    # printing each line of the array
    for a in array:
        for k in lengthKeys:
            string += splitter + " " + printHeaderCol(str(a.get(k, '')), lengthKeys[k]) + " "
        string += splitter
        string += "\n"

    # closing the table
    string += printLine(total)
    print(string)

# function to print class Elements
def tablePrintClass(array, spliter = "|"):
    dictArray = []

    # converting the object class into dictionnary
    # the make the table printing easier
    for a in array:
        dictArray.append(a.__dict__)
    
    # printing the dictionnary obtained
    tablePrintDict(dictArray, spliter)

# function to print the line section with size in parameter
def printLine(nb):
    return "+" + (nb) * "-" + "+\n"

# function to print one column element based on the max length
def printHeaderCol(text, nb):
    return text + ' ' * (nb - len(text))

# function to print table from aray
# using different function based on the type 
# of the first element
def tablePrint(array, spliter = "|"):
    a = array[0]

    # checking if it is a dictionnary
    if isinstance(a, dict):
        tablePrintDict(array, spliter)

    # checking if it is a bsic element type
    elif isinstance(a, (int, float, str, list)):
        tablePrintBasic(array, spliter)

    # by default it would be a class to print
    else:
        tablePrintClass(array, spliter)