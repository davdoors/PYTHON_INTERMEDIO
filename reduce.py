from functools import reduce


def run():
    #challenge()
    my_list = [1,4,6,7,9,8]
    result = reduce(lambda a,b:a*b, my_list) # a is the fir parameter of the list and b is the second parameter of the list
    print(result)

#given a list, multiply each list values to obtain one olny value
def challenge():
    my_list = [1,4,6,7,9,8]
    result = 1
    for num in my_list:
        result = result*num
    print(result)


if __name__ == '__main__':
    run()