from urllib.parse import urldefrag


userinput = int(input("enter a number : "))
if userinput < 0:
    print(userinput, "Negetive value not facttorial")
elif userinput < 1:
    print(1)
else:
    mul = 1
    for x in range(1, userinput+1):
            mul = mul*x
    print(mul)