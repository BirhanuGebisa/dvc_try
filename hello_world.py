print("Hello world of python")
class person:
    def __init__(self, name, age, rank):
        self.name= name
        self.age=age
        self.rank=rank
    def get_data(self):
        print("Hello my name is " + self.name + "i am " + str(self.age) + " years old. " + "i have msc in " + self.rank)
coll=person("Birhanu Gebisa ", 26 , "Computer science and engineering")
coll.get_data()