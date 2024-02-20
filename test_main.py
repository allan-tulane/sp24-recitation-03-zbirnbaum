from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(1)) == 0*1
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1*1
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(4)) == 2*4
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(5)) == 5*5
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0*0
