import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_run(self):
        obj = runner.Runner('Test')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_walk(self):
        obj = runner.Runner('Test')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance,50)

    def test_challenge(self):
        obj1 = runner.Runner('Test1')
        obj2 = runner.Runner('Test2')
        for i in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)

if __name__ == '__main__':
    unittest.main()