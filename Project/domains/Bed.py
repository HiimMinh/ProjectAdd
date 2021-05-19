
class Bed:
    def __init__(self, driver, bid, bname, room):
        self.bid = bid
        self.bname = bname
        self.room = room

    # Get methods
    def get_bid(self):
        return self.bid
    def get_bname(self): 
        return self.bname
    def get_room(self):
        return self.room

    # Set methods
    def set_bid(self, bid):
        self.bid = bid
    def set_bname(self, bname):
        self.bname = bname
    def set_room(self, room):
        self.room = room