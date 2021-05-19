
class Patient:
    def __init__(self, driver, patname, patage, patill, bedid, roomid, roomname):
        self.patname = patname
        self.patage = patage
        self.patill = patill
        self.bedid = bedid
        self.roomid = roomid
        self.roomname = roomname

    # Get methods
    def get_patname(self):
        return self.patname
    def get_patage(self):
        return self.patage
    def get_patill(self):
        return self.patill
    def get_roomid(self):
        return self.roomid
    def get_bedid(self):
        return self.bedid
    def get_roomname(self):
        return self.roomname

    # Set methods
    def set_patname(self, patname):
        self.patname = patname
    def set_patage(self, patage):
        self.patage = patage
    def set_patill(self, patill):
        self.patill = patill
    def set_roomid(self,roomid):
        self.roomid = roomid
    def set_bedid(self, bedid):
        self.bedid = bedid
    def set_roomname(self, roomname):
        self.roomname = roomname

    


        