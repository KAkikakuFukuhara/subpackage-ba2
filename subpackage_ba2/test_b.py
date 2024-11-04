from subpackage_a.testA import TestA

class TestB:
    def __init__(self):
        self.b = 2
        self.a = TestA().a

if __name__ == "__main__":
    b = TestB()
    print(b.b)
    print(b.a)