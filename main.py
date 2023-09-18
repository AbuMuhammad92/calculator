def calculator():
    while True:
        try:
            # Ввод чисел и операции пользователем
            num1 = float(input("Введите первое число: "))
            operation = input("Введите операцию (+, -, *, /) или 'q' для выхода: ")

            # Проверка на выход из программы
            if operation == 'q':
                print("Выход из программы.")
                break

            num2 = float(input("Введите второе число: "))

            # Проверка и выполнение операции
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Неверная операция.")
                continue

            # Проверка, является ли результат целым числом
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            print(f"Результат: {result}")

        except ValueError:
            print("Введенное значение не является числом. Попробуйте еще раз.")


calculator()
