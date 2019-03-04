#global declaration of "name" variable
name = "Python"


def getName():
    #local declaration of "name" variable. Run code uses C# instead of Python
    name = "C#"
    print("I am coding with {}".format(name))


getName()
