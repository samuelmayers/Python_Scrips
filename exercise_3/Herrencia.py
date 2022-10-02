class Animal:
  def __init__(self,name,legs):
    self.name = name
    self.legs = legs

class dog(Animal):
  def sound(self):
    print("Woof")

yoki=dog("yoki",4)
print(yoki.name)
print(yoki.legs)
yoki.sound()
