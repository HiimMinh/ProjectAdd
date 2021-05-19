
# Create class Staff
# Att : name
#       work

class Staff:
    def __init__(self, driver, sname, swork):
        self.sname = sname
        self.swork = swork

    # Get methods
    def get_sname(self):
        return self.sname
    def get_swork(self): 
        return self.swork

    # Set methods
    def set_sname(self, sname):
        self.sname = sname
    def set_swork(self, swork):
        self.swork = swork

   