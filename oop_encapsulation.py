#Encapsulation
class Card:
    def __init__(self, fullname, age, country, address, gender, userid):
        self.fullname = fullname
        self.age = age
        self.country = country
        self.address = address
        self.gender = gender
        self.__userid = userid  # __userid is private | encapsulation

    def __get_id(self):
        return f"id:{self.__userid}"


passport = Card("nurbek", 16, "Uzb", "tashkent", "male", "AD123456")
print(passport.get_id())

