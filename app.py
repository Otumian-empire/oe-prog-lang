import unittest

class ArithC:
    def __init__(self) -> None:
        pass


class TestArithC(unittest.TestCase):
    
    def test_is_type(self):
        a = ArithC()

        self.assertIsInstance(a, ArithC)

    def test_int_is_not_ArithC(self):
        a = 12

        self.assertNotIsInstance(a, ArithC)


class Number(ArithC):
    def __init__(self, num: int) -> None:
        self.num = num


class TestNumber(unittest.TestCase):
    
    def test_is_type_number(self):
        a = Number(3)

        self.assertIsInstance(a, Number)

    def test_is_not_type_number(self):
        a = 3

        self.assertNotIsInstance(a, Number)

    def test_property_is_int(self):
        a = Number(3)

        self.assertIsInstance(a.num, int)
    



class Plus(ArithC):
    def __init__(self, l:ArithC, r: ArithC) -> None:
        self.l = l
        self.r = r


class Mult(ArithC):
    def __init__(self, l:ArithC, r: ArithC) -> None:
        self.l = l
        self.r = r








class TestPlus:
    pass


class TestMult:
    pass




class Interp:
    def __init__(self, e: ArithC)-> None:
        self.e = e

    def exec(self):
        if type(self.e) == Number:
            return self.e
        elif type(self.e) == Plus:
            return Interp(self.e.l) + Interp(self.e.r)
        elif type(self.e) == Mult:
            return Interp(self.e.l) * Interp(self.e.r)
        else:
            raise Exception("Invalid operation or operand")





class TestBinaryExpressions:
    pass