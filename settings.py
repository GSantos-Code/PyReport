import pyautogui as p
import time as t

class settings:
    def __init__(self):
        self.ortho= p.getWindowsWithTitle("OrthoAnalyzer")
        self.ortho[0].activate()
        self.ortho[0].maximize()
        self.chrome= p.getWindowsWithTitle("Google Chrome")
    def setupActive(self):
        p.click(26,237)
    def estCapt(self, op, arcs):
        p.click(716,37)
        t.sleep(2)
        path= self.path + "\\"
        p.click(254,167)
        t.sleep(3)
        p.click(227,239)
        t.sleep(1)
        if(op == "SIM"):
            p.click(1142,73)
            self.ortho[0].activate()
            p.click(486,12)
            t.sleep(1)
            if(arcs == "Superior" or arcs == "Ambas"):
                p.click(1144,75)
                t.sleep(2)
                p.screenshot(region=(253,50,871,369)).save(path + "9.png")
            if(arcs == "Inferior" or arcs == "Ambas"):
                p.click(1141,359)
                p.click(486,12)
                t.sleep(2)
                p.screenshot(region=(253,97,865,320)).save(path + "10.png")
        p.click(1134,12)
        p.click(354,71)
        t.sleep(4)
        p.screenshot(region=(3,32,1129,620)).save(path + "11.png")
        p.alert(title="Sucess", text="Script Executado com sucesso!")
    def modelAc(self):
        p.press("pagedown")
        p.press("enter", presses=3)
    def btnBack(self):
        p.click(67,55)
    def modelDefault(self):
        p.click(70,264, clicks=3)
    def report(self):
        t.sleep(3)
        self.ortho[0].activate()
        self.PAUSE= 2
        self.btnBack()
        p.click(185,304)
        p.click(102,274)
        p.click(900,275)
        t.sleep(5)
        p.press("tab")
        p.press("enter")                 
        self.chrome[0].activate()
        self.chrome[0].maximize()
        t.sleep(10)
        p.hotkey("ctrl","p")
        t.sleep(2)
        p.press("enter")
        t.sleep(6)
        p.write(self.path)
        p.press("enter")
        p.write("13")
        p.press("tab", presses=3)
        p.press("enter")
        p.PAUSE= 1
        self.ortho[0].activate()
        self.ortho[0].maximize()
        t.sleep(5)
        self.btnBack()
        self.btnMV()
        self.modelDefault()
        p.PAUSE= 2
        self.modelAc()
        self.setupActive()
        p.PAUSE= 1
    def btnMV(self):
        p.click(33,414)
        
