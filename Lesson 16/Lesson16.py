#OOP

class Test:
	pass

class GermanCars:
	model = ""
	engine = 0.0
	mark = ""

	def SetData(self, m, e, mk):
		self.model = m
		self.engine = e
		self.mark = mk


	def GetData(self):
		return self.mark, self.engine, self.model


car1 = GermanCars()
car1.SetData("E39", 3.0, "BMW")

print(car1.GetData())


