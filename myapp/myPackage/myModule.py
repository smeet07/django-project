class MyMath:

    # create addNumbers static method
    @staticmethod
    def power(x, y):
        return x**y

    @staticmethod
    def fact(x):
        factorial = 1
        if x < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif x== 0:
            return 1
        else:
            for i in range(1, x + 1):
                factorial = factorial * i
            return factorial