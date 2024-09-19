class Build:

	__year = None
	__city = None

	def __init__(self, year, city):
		self.year = year
		self.city = city

	def getInfo(self):
		return self.year, self.city

class School(Build):

	pupils = None

	def __init__(self, year, city, pupils=500):
		super(School, self).__init__(year, city)
		self.pupils = pupils

	def getInfo(self):
		data = super().getInfo()
		return self.pupils, data


class House(Build):
	pass


class Shop(Build):
	pass


school = School(2000, "Kiev", 3000)
school.__year = 900
house = House(1990, "Miami")
shop = Shop(1800, "Khmelnitsky")
print(school.getInfo())