class Arithmetic:

    def __init__(self, varA=1, varB=1):
        self.varA = varA
        self.varB = varB

    def add(self, a,b):
        if a or b:
            return a+b
        return self.varA + self.varB

    def mul(self):
        return self.varA * self.varB

    def sqpow(self):
        return self.varA**2


if __name__ == "__main__":
    arith = Arithmetic(3,5)
    result  = arith.add()
    print(result)

