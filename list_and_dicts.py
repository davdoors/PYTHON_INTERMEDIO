def run():
    my_list = [1, "hello", 4.5]
    my_dict = {"firstname": "David", "lastname": "Dorado"}

    super_list = [
        {"firstname": "David", "lastname": "Dorado"},
        {"firstname": "Francisco", "lastname": "Sevilla"},
        {"firstname": "Jose", "lastname": "Garcia"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums":[1.45,3.544,23.029]
    }

    for key, value in super_dict.items():
        print(key, " ", value)

    for person in super_list:
        print(person["firstname"], person["lastname"])


if __name__ == '__main__':
    run()