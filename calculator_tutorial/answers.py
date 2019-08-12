class Calculator:
    
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        return a/b
    
    def pow(self, a, b):
        return a**b
    
    def add_multiple(self, *args):
        result = 0
        for arg in args:
            result += arg
        return result