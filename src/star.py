try:

    def printstar():
        val1=int(input("Enter the number of lines "))
        for i in range(1,val1+1):
            print(i*"x")


    printstar()

except SyntaxError:
    print("Invalid syntax")