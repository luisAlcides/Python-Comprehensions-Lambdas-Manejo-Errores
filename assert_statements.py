def divisors(num):
    divisors = []
    for i in range(1, num +1):
        # Debe ser igual a 0
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")
    print("Debes ingresar un número")


if __name__ == '__main__':
    run()
    