while True:
    try:
        #The first step is as expected, to take two integer values from the user
        a = int(input("Please gibe a number as 1st variable: "))
        b = int(input("Please gibe a number as 2nd variable: "))

        # The most direkt way to solve swap problem is to establish a third helping variable 
        # to hold one of the variables's value as follows:
        # c = a
        # a = b
        # b = c

        # However this aproach is not allowed here so the alternative approach is simply as follows:
        # We need to make one of the variables hold the the information of the both 
        # here since the variables are intgers the operation would be to add them.
        a = a + b
        # After that the swap operation start with making the 2nd variable hold the value of the 1st
        # this would be done by subtraction
        b = a - b
        # Finally the 2nd variable is to be made eqaul to the 1st again with subtraction 
        a = a - b

        print(f"The value of the 1st: {a}")
        print(f"The value of the 2nd: {b}")
    except:
        print("Please inter valid integer numbers !")
