

from random import randint as r
from statistics import mean

class RandomIntList(list):
    def __init__(self, amount):
        for i in range(amount):
            n = r(1, 100)
            self.append(n)
        

def main():
    print("Random Integer List")
    print()
    while True:
        choice = int(input("How many integers should the list contain?: "))
        print()
        intlist = RandomIntList(choice)
        ##Convert the Int into a string to remove the brackets in the list
        strlist = str(intlist)[1:-1]
        total = sum(intlist)
        print("Random Integers")
        print("==============")
        print(f"{'Integers:':10} {strlist}")
        print(f"{'Count:':10} {choice}")
        print(f"{'Total:':10} {total}")
        print(f"{'Average:':10} {mean(intlist)}")
        print()
        again = input("Continue? (y/n): ")
        print()
        if again != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    main()