
class Doctor:
    def __init__(self, driver, dname, dmajor, dage):
        self.dname = dname
        self.dmajor = dmajor
        self.dage = dage

    # Get methods
    def get_dname(self):
        return self.dname
    def get_dmajor(self): 
        return self.dmajor
    def get_dage(self):
        return self.dage

    # Set methods
    def set_dname(self, dname):
        self.dname = dname
    def set_dmajor(self, dmajor):
        self.dmajor = dmajor
    def set_dage(self, dage):
        self.dage = dage
    