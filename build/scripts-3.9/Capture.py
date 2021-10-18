import functions as f
import pyautogui as p
import sys

class CaptureView(f.functions):
    def __init__(self,path,master):
        self.path= path
        self.master= master
        super().__init__()
        self.capture()
    def capture(self):
        arcs= p.confirm(title="Escolha as arcadas", text="", buttons=["Superior","Inferior","Ambas"])
        while True:
            self.captFront()
            self.captBack()
            self.captLeft90()
            self.captLeft45()
            self.captRight90()
            self.captRight45()
            op= p.confirm(title="Deu tudo certo?", text="", buttons=["Sim","Não"])
            if(op == "Sim"):
                break
        if(arcs == "Superior" or arcs == "Ambas"):
            self.captOclSup("sup")
            self.captOclSup("sob")
            self.captOclSup("ipr")
        if(arcs == "Inferior" or arcs == "Ambas"):
            self.captOclInf("inf")
            self.captOclInf("sob")
            self.captOclInf("ipr")
        quest= p.confirm(title="Tem Estagiamento?", text="", buttons=["SIM","NAO"])
        self.estCapt(quest,arcs)

