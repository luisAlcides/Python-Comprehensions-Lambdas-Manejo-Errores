def divisors(num):
    divisors = []
    for i in range(1, num +1):
        # Debe ser igual a 0
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == '__main__':
    run()
    