
class Pharmarcy:
    def __init__(self ,driver, pname, pquantity):
        self.pname = pname
        self.pquantity = pquantity

    # Get methods
    def get_pname(self):
        return self.pname
    def get_pquantity(self): 
        return self.pquantity

    # Set methods
    def set_pname(self, pname):
        self.pname = pname
    def set_pquantity(self, pquantity):
        self.pquantity = pquantity

   