l=[]
ans=[]
while True:
        A=int(input("Enter value of A: "))
        if A>=0 and A<=1000:
            break
        else:
            print("Invalid input")
for a in range(1,A):
    for b in range (a+1,A):
        l=[]
        if a*a + b*b == A:
            l.extend([a,b])
            ans.append(l)
print("Answer is:",ans)
