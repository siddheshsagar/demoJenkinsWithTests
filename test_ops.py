from ops import *

def test_add():
  assert add(4,6) == 10
 
def test_subtract():
  assert subtract(4,6) == -2
  
def test_multiply():
  assert multiply(4,6) == 25
  
def test_divide():
  assert divide(42,6) == 7
