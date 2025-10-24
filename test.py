from calculator import addition
def test_add():
  assert add(2,4) == 5
  assert add(-3,3) == 0
  assert add(0,0) == 0
