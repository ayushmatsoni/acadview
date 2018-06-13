
n=int(input("ENTER THE LIMIT"))
def fact(n):
    if n==1:
       return 1
    else :
        return (n * fact(n - 1))

dict={'number':n,'Factorial':fact(n)}
print(fact(n))
print(dict)