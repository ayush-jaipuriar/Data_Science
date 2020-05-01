r = int(input("Enter the value of n"))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1): 
        if(a%i==0):	#check for factors
            k=k+1
    if(k<=0):		#for a prime number there should not be any factors beyond 2
        print(a)	#printing
