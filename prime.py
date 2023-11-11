def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
    start = int(input("enter he start index"))
    end = int(input("enter the end index:"))
    print(f"prime numbers between {start} and {end} are:")
    for i in range(start,end +1):
        if is_prime(i):
            print(i)
