def run():
    my_list = [1, "Hello", True, 4.5]
    my_dic = {"first_name": "Facundo","lastname": "Garcia"}


    super_list = [
        {"first_name": "Facundo","last_name": "Garcia"},
        {"first_name": "Luis","last_name": "Rios"},
        {"first_name": "Samuel","last_name": "Rios"},
        {"first_name": "Diego","last_name": "Jaque"},
    
    ]

    super_dic ={
        "natural_num": [1,2,3,4,5],
        "integer_num": [-1,-2,0,1,2],
        "floating_num":[1.1,4.5,6.43],
    }

    # for key,value in super_dic.items(): #--- This will show how to print a diccionary with lists.
    #     print(key," -",value)

    for i in super_list:
        print(i["first_name"],"-",i["last_name"])    #--This will show how to print a list with diccionaries.

if __name__ == '__main__':
    run()