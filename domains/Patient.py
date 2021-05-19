
class Patient:
    def __init__(self, driver, patname, patage, patill, bed):
        self.patname = patname
        self.patage = patage
        self.patill = patill
        self.bed = bed
    # Get methods
    def get_patname(self):
        return self.patname
    def get_patage(self):
        return self.patage
    def get_patill(self):
        return self.patill
    def get_bed(self):
        return self.bed

    # Set methods
    def set_patname(self, patname):
        self.patname = patname
    def set_patage(self, patage):
        self.patage = patage
    def set_patill(self, patill):
        self.patill = patill
    def set_bed(self, bed):
        self.bed = bed
    


        