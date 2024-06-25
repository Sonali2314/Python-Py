def digitize(n):
    rev=[]
    if(n==0):
        rev=[0]
        return rev
    while n>0:
        rev.append(n%10)
        n//=10
    return rev
number=int(input("Enter the number : "))
print(digitize(number))
