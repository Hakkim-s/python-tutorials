class car():
    def __init__(self,model_name,yearm,price):
        self.model_name = model_name
        self.yearm = yearm
        self.price = price

audi=car("A3",2015,3000000)
audi.cc = 8500
print(audi.__dict__)

porches = car('w5',2016,6000000)
#porches.cc = 16000
print(porches.__dict__)


class farming():
    def __init__(self,no_of_farmers,acre,cultivation_type,profit):
        self.no_of_farmers = no_of_farmers
        self.acre = acre
        self.cultivation_type = cultivation_type
        self.seed_colors = "black" + " and " + "brown"
        self.profit = profit
        #self.quantity = quantity
    def profit_inc(self):
            self.profit = int(self.profit * 5.15)
            self.quantity = (self.quantity * 500)
#wheat
wheat = farming(500,50,'regular',16000)
wheat.quantity = 500
#rice
rice = farming(1000,25,"part time",85000)

print(rice.__dict__)
print(wheat.__dict__)
print(wheat.profit)
print(wheat.quantity)
wheat.profit_inc()
print(" Profit After increase",wheat.profit)
print(" Quantity After increase",wheat.quantity)

'''
#inheritance
class superfarming(farming):
    def __init__(self,no_of_farmers,acre,cultivation_type,profit,quantity):
        super.__init__(no_of_farmers,acre,cultivation_type,profit,quantity)

wheat = superfarming(500,50,'regular',16000,500)

print(wheat.acre)
#print(help(wheat))
print(wheat) '''