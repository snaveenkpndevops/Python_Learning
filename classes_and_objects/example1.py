class college:

    def __init__(self, dept, year, quote):
        self.dept=dept
        self.year=year
        self.quote=quote

    def quotes(self):
        print (f"We are from {self.dept} {self.year} batch and we are {self.quote}")


mech=college("Mechanical", "2016", "Royal Mech")
mech.quotes()                                        # o/p: We are from Mechanical 2016 batch and we are Royal Mech

it=college("IT", "2016", "Prime IT")
it.quotes()                                          # o/p: We are from IT 2016 batch and we are Prime IT