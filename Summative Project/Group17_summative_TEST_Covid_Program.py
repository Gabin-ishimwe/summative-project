import unittest
from Group17_summative_Covid_Program import *


class Test(unittest.TestCase):
    # in this first method we tested to see if the name(entity) inputted is equal to the argument provided
    # we also tried other test scenarios where the name(entity) is not equal to the argument provided, so that we can be more sure about it
    def test_enter(self):
        self.assertEqual(security.namelist[0], "clinic")
        self.assertNotEqual(security.namelist[0], "CLINIC")
        self.assertNotEqual(security.namelist[0], "Clinic")
        self.assertNotEqual(security.namelist[0], "CLINICS")
        self.assertNotEqual(security.namelist[0], "clinics")

    # in this second method we tested to see if the password inputted is equal to the argument provided
    # we also provided other test scenarios where it is not equal to other arguments provided, so that we can be more sure about it
    def test_password(self):
        self.assertEqual(security.passwordlist[0], "covid data storage")
        self.assertNotEqual(security.passwordlist[0], "COVID data storage")
        self.assertNotEqual(security.passwordlist[0], "Covid storage")
        self.assertNotEqual(security.passwordlist[0], "storage")
        self.assertNotEqual(security.passwordlist[0], "data storage")

    # we tested the gender input field with every possible true input using assertEqual method
    # you can also test for other user input on gender field(entry), uncomment on each assertion
    def test_genderfield_input(self):
        self.assertEqual(Password.global_testGender, "M")
        # self.assertEqual(Password.global_testGender, "Male")
        # self.assertEqual(Password.global_testGender, "F")
        # self.assertEqual(Password.global_testGender, "Female")

    # we tested on the date of birth field to check if the datatype inputs are correct
    # though they have expection handling errors to show that you have to input integers, testing is also need to be sure
    def test_DOBfield_input(self):
        self.assertIs(type(Password.global_testDate), int)
        self.assertIs(type(Password.global_testMonth), int)
        self.assertIs(type(Password.global_testYear), int)

    # we tested on the age and contact field to check if the datatype inputs are correct
    # though they have expection handling errors to show that you have to input integers, testing is also need to be sure
    def test_age_contact_field(self):
        self.assertIs(type(Password.global_testAge), int)
        self.assertIs(type(Password.global_testContact), int)

    # in this program we can't test our exception handling because we they raise, the program create messageboxed for the user
    # to recognize where he made an input error, and the user can not proceed or submit anything with first solving that issue(error)
    # testing this exception can not be possible because the program will allow the user to input correct answers or inputs!!


if __name__ == "__main__":
    unittest.main()
