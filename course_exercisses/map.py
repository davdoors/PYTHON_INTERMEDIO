def run():
    #challenge()

    #chalenge but using map
    sqr = list(map(lambda num:num**2,range(1,6)))
    print(sqr)

#"hacer una lista con el cuadrado de los numeros del 1 al 5"
def challenge():
    sqr = [num**2 for num in range(1,6)]
    print(sqr)

if __name__ == '__main__':
    run()