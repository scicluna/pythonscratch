def main():
    n = getNumber()
    meow(n)

def meow(number):
    for _ in range(number):
        print("MEOW")

def getNumber():
    while True:
        n = int(input("How many meows? "))
        if n>0:
            return n

main()

