from random import randint


def run():
    rand_list = []

    for num in range(1,11):
        rand_list.append(randint(1,100))

    filter_list = list(filter(lambda num:num%2==0,rand_list))
    print("sin filtrar")
    print(rand_list)
    print("filtrada:")
    print(filter_list)


if __name__ == '__main__':
    run()