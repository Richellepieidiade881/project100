class Atm(object):
    def __init__(pincode,bank,money,self):
        self.money= money
        self.pincode = pincode
        self.bank = bank
        
         

    def pin(self):
        print("pin")

    def bank(self):
        print("bank")

    def accelerate(self):
        print("accelerated")   

richelle=Atm("code","pin" ,"bank",60)
richelle.start()