def factorial(a):
    if a==1:
        return 1
    else:
        return a*(factorial(a-1))
if __name__=="__main__":
    x=int(input("Enter the number : "))
    ans = factorial(x)
    print(f"{x}! = {ans}")
