def run():
    # Sin list comprehensions
    # list = []
    # for i in range(1, 101):
    #     if (i % 3) != 0:
    #         list.append(i**2)

    # Con list comprehensions
    # list = [i**2 for i in range(1,101) if (i % 3) != 0]

    # Agregar numeros que son  multiplos de 4 6 y 9 a su vez
    list = [i for i in range(1, 100_000) if (
        (i % 4) == 0) and ((i % 6) == 0) and ((i % 9) == 0)]
    print(list)


if __name__ == '__main__':
    run()
