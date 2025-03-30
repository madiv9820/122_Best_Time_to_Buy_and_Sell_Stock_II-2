from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {
            'Test Case 1: The Stock Market Ninja': ([7,1,5,3,6,4], 7),
            'Test Case 2: The Ultimate Glow-Up': ([1,2,3,4,5], 4),
            'Test Case 3: When the Market Breaks Your Heart': ([7,6,4,3,1], 0),
            'Test Case 4: The Rapid Fire Trader': ([1,2,1,2,1,2], 3),
            'Test Case 5: The Rollercoaster Ride': ([5,3,8,2,6,4,10], 15),
            'Test Case 6: The Empty Market (Edge Case)': ([], 0),
            'Test Case 7: The Single Day Wonder': ([100], 0),
            'Test Case 8: The Same Price Repeated': ([4,4,4,4,4], 0),
            'Test Case 9: The "Buy and Sell Same Day" Pro': ([3,8,3,8,3], 10),
        }
        self.__solution = Solution()
        return super().setUp()
    
    def test_case_1(self):
        prices, output = self.__testcases['Test Case 1: The Stock Market Ninja']
        self.assertEqual(self.__solution.maxProfit(prices), output)
    
    def test_case_2(self):
        prices, output = self.__testcases['Test Case 2: The Ultimate Glow-Up']
        self.assertEqual(self.__solution.maxProfit(prices), output)
    
    def test_case_3(self):
        prices, output = self.__testcases['Test Case 3: When the Market Breaks Your Heart']
        self.assertEqual(self.__solution.maxProfit(prices), output)

    def test_case_4(self):
        prices, output = self.__testcases['Test Case 4: The Rapid Fire Trader']
        self.assertEqual(self.__solution.maxProfit(prices), output)
    
    def test_case_5(self):
        prices, output = self.__testcases['Test Case 5: The Rollercoaster Ride']
        self.assertEqual(self.__solution.maxProfit(prices), output)

    def test_case_6(self):
        prices, output = self.__testcases['Test Case 6: The Empty Market (Edge Case)']
        self.assertEqual(self.__solution.maxProfit(prices), output)
    
    def test_case_7(self):
        prices, output = self.__testcases['Test Case 7: The Single Day Wonder']
        self.assertEqual(self.__solution.maxProfit(prices), output)
    
    def test_case_8(self):
        prices, output = self.__testcases['Test Case 8: The Same Price Repeated']
        self.assertEqual(self.__solution.maxProfit(prices), output)
    
    def test_case_9(self):
        prices, output = self.__testcases['Test Case 9: The "Buy and Sell Same Day" Pro']
        self.assertEqual(self.__solution.maxProfit(prices), output)

if __name__ == '__main__': unittest.main()