

class Room:
    def __init__(self, driver, rname, rid, bquantity):
        self.rname = rname
        self.rid = rid
        self.bquantity = bquantity

    # Get methods
    def get_rname(self):
        return self.rname
    def get_rid(self):
        return self.rid
    def get_bquantity(self):
        return self.bquantity

    # Set methods
    def set_rname(self, rname):
        self.rname = rname
    def set_rid(self, rid):
        self.rid = rid
    def set_bquantity(self, bquantity):
        self.bquantity = bquantity