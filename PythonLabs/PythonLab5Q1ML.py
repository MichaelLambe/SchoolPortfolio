



class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def perimeter(self) -> int:
        return (self.height + self.width) * 2

    def area(self) -> int:
        return self.height * self.width

    def __str__(self) -> str:
        square = ""
        top_and_bottom = "* " * self.width + "\n"  # first line
        square += top_and_bottom
        for i in range(self.height - 2):
            square += "* "
            square += "  " * (self.width - 2)
            square += "* \n"
        square += top_and_bottom
        return square

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        

def main():
    print("Rectangle calculator")
    print()
    while True:
        choice = input("Rectangle or square? (r/s): ")
        if choice == "r":
            print()
            h = input(f"{'Enter a height: ':20}")
            w = input(f"{'Enter a width: ':20}")

            rect = Rectangle(int(h), int(w))

            print(f"{'Perimeter:':10} {rect.perimeter()}")
            print(f"{'Area:':10} {rect.area()}")
            print(rect)
            print()
        elif choice == "s":
            print()
            l = input(f"{'Length: ':10} ")
            
            squa = Square(int(l))
            print(f"{'Perimeter:':10} {squa.perimeter()}")
            print(f"{'Area:':10} {squa.area()}")
            print(squa)
            print()
        else:
            print("Invalid choice please try again")
            print()
        again = input("Continue (y/n): ")
        print()    
        if again != 'y':
            break


if __name__ == "__main__":
    main()