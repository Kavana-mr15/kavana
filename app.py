def div(a,b):
  return a/b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
class TestCalculator(unittest.TestCase):

  def  test_div(self):
    self.assertEqual(div(20,20),40)
  def test_subtract(self):
    self.assertEqual(subtract(20,10),10)
  def test_multiply(self):
    self.assertEqual(multiply(6,4),24)

if __name__=="__main__":
  print("student calculator application")
  print("division:", div(20,20))
  print("subtraction:", subtract(20,10))
  print("multiplication:", multiply(5,4))

 print("\n executing automated tests...\n")
unittest.main(argv=['first-arg-is-ignored'],
              exit=False)
