def run():
    def divisors(num): return [
        i for i in range(1, num+1) if (num % i) == 0]
        
    num = input("Ingrese un numero: ")
    assert num.isnumeric() and int(num) > 0, "Solo puede ingresar numeros positivos"
    print(divisors(int(num)))


if __name__ == '__main__':
    run()
