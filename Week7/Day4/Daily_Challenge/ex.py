# Daily Challenge : Exceptions
def compute():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("you cannot divide by zero")

compute()