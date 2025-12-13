num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd numbaer:"))
print(f"num1={num1}, num2={num2}")
if(num2==0):
    print("error:divider by zero(hint divider must be non zero)")
else:
    div=num1/num2
    print(f"div={div}")