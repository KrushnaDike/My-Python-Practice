class Dad:
    football = 1

class Son(Dad):
    dance = 1
    football = 9
    def isdance(self):
        return f"Yes I Dance {self.dance} no of times"

class Grandson(Son):
    guitar = 1
    dance = 6

    def isdance(self):
        return f"Jackson yeah!" \
               f"Yes I Dance very awesomely {self.dance} no of times"


darry = Dad()
larry = Son()
harry = Grandson()

# print(harry.football)

# Electronic Device
# Pocket Gadget
# Phone

class Electroni_Device:
    features = 1
    
class Pocket_Gadget(Electroni_Device):
    features = 10
    calling = 1
    # def isshow(self):
    #     return f"I have {self.features}"
    
class Phone(Pocket_Gadget):
    features = 100
    calling = 10
    # def isshow(self):
    #     return f"I have {self.features}"
    
television = Electroni_Device()
digitalwatch = Pocket_Gadget()
m31s = Phone()

# print(m31s.features)


class electronic_device():
    power_consumption = ("100w")


class pocket_gadget(electronic_device):
    power_consumption = ("50w")

    def mobile(self):
        return (f"This uses a rechargable battery which is of {self.name}")

class phone(pocket_gadget):
    # power_consumption = ("5-6w")
    power = 30

    # def mobile(self):
    #     return (f"This uses a rechargable battery which is of {self.name}")


battery = phone()
battery.name = "2500 mAh"

print(battery.mobile())
print(battery.power_consumption)