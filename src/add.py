try:


    def convertme():
        unit=input("Enter (F) or (C) = ")
        val1=input("Enter the value to be converted ")
        if(unit.upper()== "F"):
            print("You are now converting {:.2f} F into C ")

            final=(float(val1)-32)*5/9
            print("Celcius value = {:.2f}".format(final))

        else:
            print("You are now converting {:.2f} C into F ")
            final=(val1*9/5)+32
            print("Farenheit value = {.2f}".format(final))

        
    def subme():
        val1=float(input("Enter the first integer - "))
        val2=float(input("Enter the second integer - "))
        
        if (val1 > val2):
            addout=float(val1-val2)
        else:
            addout=float(val2-val1)
        
        return addout



    def addme():
        val1=float(input("Enter the first integer - "))
        val2=float(input("Enter the second integer - "))
        
        addout=float(val1+val2)
        return addout

    def mulme():
        val1=float(input("Enter the first integer - "))
        val2=float(input("Enter the second integer - "))
        
        addout=float(val1*val2)
        return addout

    def divme():
        val1=float(input("Enter the first integer - "))
        val2=float(input("Enter the second integer - "))
        
        addout=float(val1/val2)
        return addout

    op=input("Enter the operation (A or S or M or D or C) = ")
    if(op.upper() == "A"):
        val3=addme()
        print("The sum of the numbers {:.2f}".format(val3))
    if(op.upper() == "S"):
        val3=subme()

        print("The difference between the numbers {:.2f}".format(val3))
    if(op.upper() == "M"):
        val3=mulme()
        print("The product of the numbers {:.2f}".format(val3))
    if(op.upper() == "D"):
        val3=mulme()
        print("The division of the numbers {:.2f}".format(val3))
    if(op.upper() == "C"):
        val3=convertme()
        
except KeyError:
    print("Invalid option chosen")