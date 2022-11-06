def write():
    pass

def read():
    numbers = []
    with open("./files/numbers.txt", "r") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)

def run():
    read()

if __name__ == "__main__":
    run()