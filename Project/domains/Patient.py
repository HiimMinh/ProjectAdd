
class Patient:
    def __init__(self, driver, patname, patage, patill, room):
        self.patname = patname
        self.patage = patage
        self.room = room
        self.patill = patill

    # Get methods
    def get_patname(self):
        return self.patname
    def get_patage(self):
        return self.patage
    def get_room(self):
        return self.room
    def get_patill(self):
        return self.patill

    # Set methods
    def set_patname(self, patname):
        self.patname = patname
    def set_patage(self, patage):
        self.patage = patage
    def set_room(self,):
        return self.room
    def get_patill(self):
        return self.patill
    


        