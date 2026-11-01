
def add(x, y, op):
    if op == "+":
        return x + y


if __name__ == "__main__":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    op = input("Enter operator: ")

    print(add(x, y, op))
