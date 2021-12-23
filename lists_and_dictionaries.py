def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname": "garcia"},
        {"firstname": "Santiago", "lastname": "Arias"},
        {"firstname": "Facundo", "lastname": "Acuña"},
        {"firstname": "Bruno", "lastname": "Puggioni"},
        {"firstname": "Lucas", "lastname": "Pane"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    def print_dictionary(dictionary):
        for key, value in dictionary.items():
            print(key, "-", value)

    def print_list(list):
        for i in list:
            name = ""
            for key, value in i.items():
                if name == "":
                    name = value
                else:
                    name = name + " - " + value
            print(f'{name}')
    # print_dictionary(super_dict)
    # print_list(super_list)


if __name__ == '__main__':
    run()
