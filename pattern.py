n=int(input("Enter radius "))

for each in range(n):
    str='*' * (each+1)
    str=str+ ' ' * (2*(n-each-1))
    str=str+'*'*(each+1)
    print(str)

for each in range(n-1):
    str='*' * (n-each-1)
    str=str+' ' *(2*(each+1))
    str=str+'*' * (n-each-1)
    print(str)
     
