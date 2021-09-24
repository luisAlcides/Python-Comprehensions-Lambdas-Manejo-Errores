
def run():
    my_list = [1,"hello", True, 4.5]
    my_dict = {"firstname": "Morel", "lastName" : "Garcia"}


    #Lista que almacena diccionarios
    super_list = [
        {"firstname": "Morel", "lastName" : "Garcia"},
        {"firstname": "Miguel", "lastName" : "Garcia"},
        {"firstname": "Susan", "lastName" : "Garcia"}
        
    ]


    #Diccionario que almacena listas
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()