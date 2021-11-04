import settings as s
import pyautogui as p
import time as t
from tkinter import *
import os
import win32api
import win32gui

class functions(s.settings):
    def __init__(self):
        super().__init__()
        p.PAUSE= 0.05
    def Sobrepos(self,btn):
        if(btn == "on"):
            p.click(1300,225)
        else:
            p.click(1227,224)
    def Transp(self,btn):
        t.sleep(1)
        if(btn == "on"):
            p.click(1301,142)
        else:
            p.click(1224,225)
    def IPR(self, btn):
        self.DownMenu()
        if(btn == "on"):
            p.PAUSE=0.5
            p.click(40,285, clicks=4)
            p.click(237,408)
            t.sleep(3)
            self.Transp("on")
            self.Dist("on")
        else:
            p.PAUSE=0.5
            p.click(40,285, clicks=4)
            p.click(237,408)
            t.sleep(3)
            self.Dist("off")
            
    def Dist(self,btn):
        p.click(36,340)
        if(btn == "off"):
            p.click(61,418)
        else:
            p.click(203,418)
    def DownMenu(self):
        p.moveTo(256,154)
        p.click(256,599, clicks=2)
    def Photo(self,text):
        p.click(1340,636)
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
        aux= 0
        dc = win32gui.GetDC(0)
        if(op == "sup"):
            p.alert(title="Atenção", text="Você tem 13 segundos para marcar o IPR")
            t.sleep(13)
            p.alert(title="Ajuste a posição", text="Ajuste a posição para o Relatório de IPR(se houver)")
            while True:
                win32gui.MoveToEx(dc,0,85)
                win32gui.LineTo(dc,1366,85)
                win32gui.MoveToEx(dc,0,597)
                win32gui.LineTo(dc,1366,597)
                aux += 1
                print(aux)
                if(aux == 120):
                    break
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Superior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Superior sem indicacao IPR")
        else:
            p.alert(title="Atenção", text="Você tem 13 segundos para marcar o IPR")
            t.sleep(13)
            p.alert(title="Ajuste a posição", text="Ajuste a posição para o Relatório de IPR(se houver)")
            while True:
                win32gui.MoveToEx(dc,0,85)
                win32gui.LineTo(dc,1366,85)
                win32gui.MoveToEx(dc,0,597)
                win32gui.LineTo(dc,1366,597)
                aux += 1
                print(aux)
                if(aux == 120):
                    break
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Inferior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Inferior sem indicacao IPR")
    def Menu(self,btn):
        if(btn == "Otop"):
            p.click(1340,344)
        elif(btn == "Oinf"):
            p.click(1340,309)
        elif(btn == "Right"):
            p.click(1340,238)
        elif(btn == "Left"):
            p.click(1340,275)
        elif(btn == "Front"):
            p.click(1340,169)
        elif(btn == "Post"):
            p.click(1340,196)
        
    def Mand(self,btn):
        if(btn == "off"):
            p.click(1225,120)
        else:
            p.click(1298,120)
    def Max(self,btn):
        if(btn == "off"):
            p.click(1230,89)
        else:
            p.click(1301,89)
    def captFront(self):
        aux= 0
        dc = win32gui.GetDC(0)
        win32gui.MoveToEx(dc,0,0)
        win32gui.LineTo(dc,0,1366)
        p.click(1340,423)
        
        p.alert(title="Atenção", text="Ajuste a posição inicial, alinhe com a linha desenhada na tela")
        #Pega o contexto gráfico para o Desktop
        dc = win32gui.GetDC(0)
        #Desenha uma linha do ponto (0,0) até (1366,768)
        while True:
            win32gui.MoveToEx(dc,0,321)
            win32gui.LineTo(dc,1366,321)
            aux += 1
            print(aux)
            if(aux == 120):
                break
        t.sleep(3)
        self.Photo("Vista Oclusao Anterior")
    def captBack(self):
        p.moveTo(700,321)
        p.moveTo(700,321)
        p.moveTo(700,321)
        p.mouseDown(button="RIGHT")
        p.moveTo(1054,321)
        p.mouseUp(button="LEFT")
        self.Photo("Vista Oclusao Posterior")
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
    def captOclInf(self,op, arcs):
        if(op == "inf" and arcs == "Inferior"):
            t.sleep(3)
            self.Menu("Oinf")
            self.Max("off")
            self.Mand("on")
            p.alert(title="Atenção", text="Ajuste a posição inferior")
            t.sleep(3)
            self.Photo("Vista Oclusal Inferior")
        elif(op == "inf" and arcs == "Ambas"):
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
            p.click(39,434)
            p.click(256,156)
            self.DownMenu()
            self.IPR("on")
            self.IPRPhoto("inf")
    
        
