

class Room:
    def __init__(self, driver, rname, rid, rstatus):
        self.rstatus = rstatus
        self.rid = rid
        self.rname = rname

    # Get methods
    def get_rname(self):
        return self.rname
    def get_rid(self):
        return self.rid
    def get_rstatus(self):
        return self.rstatus

    # Set methods
    def set_rname(self, rname):
        self.rname = rname
    def set_rid(self, rid):
        self.rid = rid
    def set_rstatus(self, rstatus):
        self.rstatus = rstatus