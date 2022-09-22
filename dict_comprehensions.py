def run():
    #cube_dict()
    cubes = {number:number**3 for number in range(101) if number%3 == 0}
    #print(cubes)
    
    root_dict()


def cube_dict():
    cubes = {}
    for number in range(101):
        if number % 3 != 0: continue
        cubes[number] = number ** 3
    print(cubes)

def root_dict():
    root_dict = {number:round(number**0.5, 2) for number in range(1,1001) }
    print(root_dict)


if __name__ == '__main__':
    run()