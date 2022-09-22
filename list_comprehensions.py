sqr = []
def run():
    #sqr_list()
    sqr = [number**2 for number in range(101) if number % 3 != 0]
    reto = [number for number in range(100000) if number % 4 == 0 and number % 6 == 0 and number % 9 == 0]
    print(reto)

def sqr_list():
    for number in range(101):
        if number % 3 == 0:
            sqr.append(number**2)

    print(sqr)

if __name__ == '__main__':
    run()