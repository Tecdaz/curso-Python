def run():
    # Without dict comprenhensions
    # dict = {}
    # for i in range(1, 101):
    #     if (i % 3) != 0:
    #         dict[i] = i**3

    # With dict comprenhensions
    # dict = {i: i**3 for i in range(1, 101) if (i % 3) != 0}

    # Las llaves van a ser los primeros 1000 numeros naturales y los valores su raiz cuadrada
    dict = {i: round(i**(0.5), 2) for i in range(1, 1001)}
    print(dict)


if __name__ == '__main__':
    run()
