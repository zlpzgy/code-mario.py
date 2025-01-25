def main():
    height = get_height()
    for i in range(1, height + 1):
        # Left pyramid
        print(" " * (height - i) + "#" * i, end="  ")
        # Right pyramid
        print("#" * i)

def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass
        print("Please enter a positive integer between 1 and 8.")

if __name__ == "__main__":
    main()
