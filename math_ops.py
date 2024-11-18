# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    try:
        return a / b  # Potential division by zero error
    except ZeroDivisionError:
        print("Cannot divide by 0")
def add(a,b):
    return a+b

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    result2 = add(3,4)
    print(f"The result of division is: {result}")
    print(f"The result of additionis: {result2}")
