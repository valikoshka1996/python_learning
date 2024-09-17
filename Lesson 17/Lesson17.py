#Lesson 17

class Car:

	Mark = ""
	Model = ""
	Engine = 0.0

	def __init__(self, mk, md, en):
		self.setData(mk, md, en)
		


	def setData(self, mk, md, en = 0.0):
		self.Mark = mk
		self.Model = md
		self.Engine = en

	def getData(self):
		return self.Mark, self.Model, self.Engine



car1 = Car("E39", "BMW", 3.0)

print(car1.getData())


