import functions as f
import pyautogui as p
import sys

class CaptureView(f.functions):
    def __init__(self,path):
        self.path= path
        super().__init__()
        self.capture()
    def capture(self):
        self.captFront()
        self.captBack()
        self.captLeft90()
        self.captLeft45()
        self.captRight90()
        self.captRight45()
        self.captOclSup("sup")
        self.captOclSup("sob")
        self.captOclSup("ipr")
        self.captOclInf("inf")
        self.captOclInf("sob")
        self.captOclInf("ipr")
        quest= p.confirm(title="Tem Estagiamento?", text="", buttons=["SIM","NAO"])
        self.estCapt(quest)
        sys.exit()

