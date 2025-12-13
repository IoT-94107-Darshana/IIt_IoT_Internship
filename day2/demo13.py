def fib(num):

    prev=0
    next=1
    print(f"terms of fibonacci series={prev}")
        
    i=0
    while(i<num):
        print(prev,end=" ")
        prev,next=next,prev+next
        i+=1
        
        
num=int(input("enter a number of term for fibonacci:"))     

fib(num)