#try / except loops.

def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    compute(var1,var2)

"""
create the compute function that getInfo calls.
getinfo gives the parameters var1 and var2 to compute as arguements
"""
def compute(var1, var2):
    try:
        var3 = int(var1)+ int(var2)
        print("{} + {} = {}".format(var1, var2, var3))
    # "as e" will allow the .format to enter the internal error, not necessary
    except ValueError as e:
        print("{}: /n You did not provide a numeric value!".format(e))
    except:
        print("Ooops, you provided invalid input, program will close now!")
    #finally will happen no matter what, may be a good place to define default values
    finally:
        print("Moving on...")



#SECOND VERSION 
def getInfo2():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return var1,var2


def compute2():
    go = True
    while go:
        #valuable catch method.
        var1,var2 = getInfo2()
        try:
            var3 = int(var1)+ int(var2)
            go = False
        # "as e" will allow the .format to enter the internal error, not necessary
        except ValueError as e:
            print("{}: /n You did not provide a numeric value!".format(e))
        except:
            print("Ooops, you provided invalid input, program will close now!")
    print("{} + {} = {}".format(var1, var2, var3))


if __name__ == "__main__":
    compute2()



