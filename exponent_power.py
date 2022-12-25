def power(b, n, i):
   
    if n == 0:
        return 1
    else:
        if n % 2 != 0: # n is odd
            i = i + 1
            print(i,"power: ", b, n-1)
            a = power(b, n - 1, i)
            return a * b
        else:
            i = i + 1
            print(i,"power: ", b, n/2)
            a = power(b, n/2, i)
            return a * a
        
def main():
    power(5, 127, 0)
    
    
    
main()