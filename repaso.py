from random import randint, random


def run():
    rand_list = []
    for num in range(101):
        rand_list.append(randint(0,100))
    even = list(filter(lambda num:num%2==0,rand_list))
    print(even)
    #filter(rand_list)
    #list = [num for num in rand_list if num%2 == 0]
    #print (list)
    
#def filter(list):
    
    
    
    

if __name__ == '__main__':
    run()
    