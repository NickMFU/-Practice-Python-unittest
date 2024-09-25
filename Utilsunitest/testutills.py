import Utilsunitest.utils as utils 
#Create test function
# Test Case - 1 : Test Total Function
def test_total():
    actual_value = utils.total(3,5)
    expected_value = 8
    assert actual_value == expected_value

# Test Case - 2 : Test Total Function
def test_multiply():
    actual_value = utils.multiply(3,5)
    expected_value = 15
    assert actual_value == expected_value

# Test Case - 3 : Test Total Function
def test_total_string():
    actual_value = utils.total("3","5")
    expected_value = '35'
    assert actual_value == expected_value