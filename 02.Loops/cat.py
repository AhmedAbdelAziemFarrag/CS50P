def main():
    n = get_number()
    mewo(n)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def mewo(n):
    for _ in range(n):
        print("mewo")


main()







