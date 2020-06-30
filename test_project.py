#Ntombekazi Sibetyu Lotto challenge mini project
#import the TestCase
from unittest import TestCase

#importing the functions from the mini_project module
from mini_project import verify_age,assign_prize,count_

#class that will test the functions in module mini_project
class TestProject(TestCase):

    #testing the function that verifies the user's age
    def test_verify_age(self):
        self.assertEqual(verify_age(18),"True","Should be True")
        self.assertEqual(verify_age(17),"False","Should be False")

    def test_assign_prize(self):
        self.assertEqual(assign_prize(4),"You won R2,384")
        self.assertEqual(assign_prize(1),"Sorry you did not win anything")
