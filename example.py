def add(a, b):
    res = a + b
    return res

def greet(user_name):
    # конкатенация строк вместо !f-string! и нет проверки типа user_name
    greeting_message = "Hello, " + user_name + " welcome!"
    print(greeting_message)
    return greeting_message

def calculate_square(number):
                     # квадрат числа
    return number * number

if __name__ == "__main__":
    print(f"Square of 5 is: {calculate_square(5)}")
    greet("Developer")
