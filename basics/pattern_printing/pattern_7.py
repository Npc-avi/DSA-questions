class pattern:
    def pattern_1(self, x):
        for i in range(x):
            for j in range(x-i-1):
                print(" ",end=" ")
            for j in range(2*i+1):
                print("*",end=" ")
            for j in range(x-i-1):
                print(" ",end=" ")
            print()
        for i in range(x):
            for j in range(i):
                print(" ",end=" ")
            for j in range(2*(x-i)-1):
                print("*",end=" ")
            for j in range(i):
                print(" ",end=" ")
            print()
    def pattern_2(self , x):
        for i in range(x):
            for j in range(i+1):
                print("*",end=" ")
            for j in range(x-1):
                print(" ",end=" ")
            print()
        for i in range(x):
            for j in range(x-i-1):
                print("*",end=" ")
            print()
    def pattern_3(self , x):
        for i in range(x):
            for j in range(i+1):
                z = i+j
                if z%2==0:
                    print("1",end=" ")
                else:
                    print("0",end=" ")
            print()
    def pattern_4(self , x):
        for i in range(x):
            for j in range(i):
                print(j+1,end=" ")
            for j in range(x-2*i+3):
                print(" ",end=" ")
            for j in range(i,0,-1):
                print(j,end=" ")
            print()
    def pattern_5(self, x):
        for i in range(x):
            for j in range(x-i):
                print("*",end=" ")
            for j in range(x+(2*i)-5):
                print(" ",end=" ")
            for j in range(x-i):
                print("*",end=" ")
            print()
        for i in range(x):
            for j in range(i+1):
                print("*",end=" ")
            for j in range(x-(2*i)+3):
                print(" ",end=" ")
            for j in range(i+1):
                print("*",end=" ")
            print()
    def pattern_6(self, x):
        for i in range(x):
            for j in range(i+1):
                print("*",end=" ")
            for j in range(x-(2*i)+3):
                print(" ",end=" ")
            for j in range(i+1):
                print("*",end=" ")
            print()
        for i in range(x):
            for j in range(x-i):
                print("*",end=" ")
            for j in range((2*i)-5):
                print(" ",end=" ")
            for j in range(x-i):
                print("*",end=" ")
            print()
            

pattern = pattern()

x = int(input("enter the number of rows: "))

y = int(input("enter the pattern number: "))

match y:
    case 1:
        pattern.pattern_1(x)
    case 2:
        pattern.pattern_2(x)
    case 3:
        pattern.pattern_3(x)
    case 4:
        pattern.pattern_4(x)
    case 5:
        pattern.pattern_5(x)
    case 6:
        pattern.pattern_6(x)
    case _:
        print("Invalid pattern number")

