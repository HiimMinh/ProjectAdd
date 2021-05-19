
class Medicine:
    def __init__(self ,driver, mname, mquantity):
        self.mname = mname
        self.mquantity = mquantity

    # Get methods
    def get_mname(self):
        return self.mname
    def get_mquantity(self): 
        return self.mquantity

    # Set methods
    def set_mname(self, mname):
        self.mname = mname
    def set_mquantity(self, mquantity):
        self.mquantity = mquantity

   