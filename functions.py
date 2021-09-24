import settings as s
import pyautogui as p
import time as t
from tkinter import *
import os

class functions(s.settings):
    def __init__(self):
        super().__init__()
        p.PAUSE= 0.05
    def Sobrepos(self,btn):
        if(btn == "on"):
            p.click(1854,224)
        else:
            p.click(1778,224)
    def Transp(self,btn):
        t.sleep(1)
        if(btn == "on"):
            p.click(1852,143)
        else:
            p.click(1778,225)
    def IPR(self, btn):
        self.DownMenu()
        if(btn == "on"):
            p.PAUSE=0.5
            p.click(44,502, clicks=4)
            p.click(235,611)
            t.sleep(3)
            self.Transp("on")
            self.Dist("on")
        else:
            p.PAUSE=0.5
            p.click(44,502, clicks=4)
            p.click(236,611)
            t.sleep(3)
            self.Dist("off")
            
    def Dist(self,btn):
        if(btn == "off"):
            p.click(39,543)
            p.click(58,630)
        else:
            p.click(39,543)
            p.click(206,631)
    def DownMenu(self):
        #p.moveTo(255,735)
        #p.click(255,735, clicks=2)
        pass
    def Photo(self,text):
        p.click(1888,640)
        p.write(text)
        p.press(["tab","tab","tab"])
        p.press("enter")
    def SobreposPhoto(self,op):
        if(op == "sup"):
            p.alert(title="Atenção", text="Você tem 5 segundos para marcar sobreposição")
            t.sleep(5)
            self.Photo("Vista Oclusal Superior com Sobreposicao")
        else:
            p.alert(title="Atenção", text="Você tem 5 segundos para marcar sobreposição")
            t.sleep(5)
            self.Photo("Vista Oclusal Inferior com Sobreposicao")
    def question(self):
        x= p.confirm(title="Tem IPR?",text="",buttons=["SIM","NAO"])
        return x
    def IPRPhoto(self,op):
        p.PAUSE= 0.2
        if(op == "sup"):
            p.alert(title="Atenção", text="Você tem 13 segundos para marcar o IPR")
            t.sleep(13)
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Superior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Superior sem indicacao IPR")
        else:
            p.alert(title="Atenção", text="Você tem 13 segundos para marcar o IPR")
            t.sleep(13)
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Inferior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Inferior sem indicacao IPR")
    def Menu(self,btn):
        if(btn == "Otop"):
            p.click(1890,345)
        elif(btn == "Oinf"):
            p.click(1890,311)
        elif(btn == "Right"):
            p.click(1890,238)
        elif(btn == "Left"):
            p.click(1890,275)
        elif(btn == "Front"):
            p.click(1890,166)
        elif(btn == "Post"):
            p.click(1890,202)
        
    def Mand(self,btn):
        if(btn == "off"):
            p.click(1778,115)
        else:
            p.click(1851,115)
    def Max(self,btn):
        if(btn == "off"):
            p.click(1778,92)
        else:
            p.click(1851,88)
    def captFront(self):
        p.click(1890,417)
        p.alert(title="Atenção", text="Ajuste a posição inicial")
        t.sleep(3)
        self.Photo("Vista Oclusal Anterior")
    def captBack(self):
        p.moveTo(700,321)
        p.mouseDown(button="RIGHT")
        p.moveTo(1067,321)
        p.mouseUp(button="LEFT")
        self.Photo("Vista Oclusal Posterior")
    def captLeft90(self):
        p.moveTo(700,321)
        p.mouseDown(button="RIGHT")
        p.moveTo(511,321)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Direita 90°")
    def captLeft45(self):
        p.moveTo(700,321)
        p.mouseDown(button="RIGHT")
        p.moveTo(593,321)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Direita 45°")
    def captRight90(self):
        p.moveTo(700,321)
        p.mouseDown(button="RIGHT")
        p.moveTo(480,321)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Esquerda 90°")
    def captRight45(self):
        p.moveTo(700,321)
        p.mouseDown(button="RIGHT")
        p.moveTo(795,321)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Esquerda 45°")
    def captOclSup(self,op):
        p.PAUSE= 0.2
        if(op == "sup"):
            self.Menu("Otop")
            self.Mand("off")
            p.alert(title="Atenção", text="Ajuste a posição superior")
            t.sleep(2)
            self.Photo("Vista Oclusal Superior")
        elif(op == "sob"):
            self.Sobrepos("on")
            self.SobreposPhoto("sup")
        else:
            self.Sobrepos("off")
            self.Transp("on")
            self.IPR("on")
            self.IPRPhoto("sup")
    def captOclInf(self,op):
        if(op == "inf"):
            t.sleep(3)
            self.IPR("off")
            self.Menu("Oinf")
            self.Max("off")
            self.Mand("on")
            p.alert(title="Atenção", text="Ajuste a posição inferior")
            t.sleep(3)
            self.Photo("Vista Oclusal Inferior")
        elif(op == "sob"):
            self.Sobrepos("on")
            self.SobreposPhoto("inf")
        else:
            self.Sobrepos("off")
            #p.click(39,501)
            #p.click(256,156)
            self.DownMenu()
            self.IPR("on")
            self.IPRPhoto("inf")
    
        
