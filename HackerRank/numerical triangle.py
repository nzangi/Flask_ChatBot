# length = int(input("Enter the size of the string : "))
#
# for i in range(1,length+1):
#     print(str(i)*i)

for i in range(1,int(input())):
    print(i*(10**i-1)//9)