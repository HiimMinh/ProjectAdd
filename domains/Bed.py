
class Bed:
    def __init__(self, driver, bid, bstatus, room):
        self.bid = bid
        self.room = room
        self.bstatus = bstatus

    # Get methods
    def get_bid(self):
        return self.bid
    def get_room(self):
        return self.room
    def get_status(self):
        return self.bstatus

    # Set methods
    def set_bid(self, bid):
        self.bid = bid
    def set_bname(self, bstatus):
        self.bstatus = bstatus
    def set_room(self, room):
        self.room = room