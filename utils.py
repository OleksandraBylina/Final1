def prostota(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        else:
            pass
    return True


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

<<<<<<< Updated upstream
=======
def pyatirka(n):
    if n%5!=0:
        return False
    while n%5==0:
        n=n/5
    if n%5!=0 and n!=1:
        return False
    else:
        return True

def dva(n):
    if n%2!=0:
        return False
    while n%2==0:
        n=n/2
    if n%2!=0 and n!=1:
        return False
    else:
        return True

>>>>>>> Stashed changes

