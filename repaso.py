def run():
    list = [num**2 for num in range(101) if num % 3 == 0]
    dict = {num : num**0.5 for num in range(101) if num % 3 == 0} 
    print(list)
    print( "     ")
    print(dict)

if __name__ == '__main__':
    run()
    