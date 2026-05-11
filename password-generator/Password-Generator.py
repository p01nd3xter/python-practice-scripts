import random
import string

while True:
    try:

        length = int(input("Введите длину пароля: "))

        chars = string.ascii_letters + string.digits + "!@$&*"

        password = "".join(random.choice(chars) for _ in range(length))

        print(password)

    except ValueError:
        pass
