try:
    

    def primenumbers(val):
        for i in range(1,val):
            if(i%2 == 0):
                continue
            else:
                pr=1
                for j in range(3,i):
                    if(i%j == 0):
                        pr=0
                        break
                    else:
                        continue
            if(pr==1):
                print(i)



    

    val=int(input("Enter the number range - "))
    primenumbers(val)

except SyntaxError:
    print("Invalid syntax")