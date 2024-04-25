
def printNumbers(N):
    if N==0:
        print('')
    elif N==1:
        print(N,end='')
    else:
        printNumbers(N-1)
        print(N,end='')

if __name__ == "__main__":

    N = int(input("Enter A number\n"))
    printNumbers(N)
    res = (i in range  (100))