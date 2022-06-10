class bike(object):
    def __init__(self,model,company,topspeed,color):
        self.model=model
        self.company=company
        self.topspeed=topspeed
        self.color=color 

    def display(self):
        print("Hi")
        return("Hello")

    def show(self):
        print("how are you")

c1 = bike("sport","harley davidson","250km/h", "black")
print(c1.topspeed)
print(c1.display())