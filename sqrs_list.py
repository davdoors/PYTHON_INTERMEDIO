sqr = []
def run():
    #sqr_list()
    sqr = [number**2 for number in range(101) if number % 3 != 0]
    print(sqr)

def sqr_list():
    for number in range(101):
        if number % 3 == 0:
            sqr.append(number**2)

    print(sqr)

if __name__ == '__main__':
    run()