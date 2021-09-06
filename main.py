from tablePrint import *

# basic class to test class ptinting table
class project:

    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.arr = [1,2,3]


# main function for examples
def main():

    intArray = [12, 11, 125, 9, 9182]

    floatArray = [12.012, 1246.3783, 1378, 17.09]

    stringArray = ["123", "Hello World !", "Coucou"]

    dictArray = [
        {'rec' : 2, 'Hello' : 3}, 
        {'rec' : 2, 'Hello' : 3, 'test' : "testing"}, 
        {'rec' : 2, 'Hello' : "Hallo", 'test' : "testing"}
    ]

    classArray = [
        project("title1", "desc1"),
        project("title2", "desc2"),
        project("title3", "desc3"),
        project("title4", "desc4"),
    ]

    tablePrint(intArray)
    tablePrint(floatArray)
    tablePrint(stringArray)
    tablePrint(dictArray)
    tablePrint(classArray)


if __name__ == "__main__":
    main()