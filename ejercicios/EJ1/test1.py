import unittest
import ev3ej1 as ej1

class testej1(unittest.TestCase):
    def test_hanoi(self):
        
        for y in range(25):
            source = []
            for x in range(y,0,-1):
                source.append(y)


            target = []
            helper = []
            hanoi(len(source),target,helper)


if __name__ = "__main__":
    unittest.main()