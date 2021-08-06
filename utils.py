from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
from reportlab.rl_config import defaultPageSize
import os

class auxtools(object):
    def __init__(self, pdfname):
        self.width= 596
        self.height= 842
        try:
            os.mkdir("output")
        except Exception:
            pass
        self.pdf= canvas.Canvas("output/" + pdfname + ".pdf", verbosity= 1, bottomup= 0)
        self.pdf.setPageSize((596,842))
        self.pdf.setTitle(pdfname)
        self.Header()
        self.body()
        self.pdf.save()
    def Center(self, ref):
        return (self.width - ref)/2
    def Header(self):
        self.pdf.setFillColorRGB(31/255,91/255,141/255)
        self.pdf.setStrokeColorRGB(31/255,91/255,141/255)
        self.pdf.rect(0,0,827,180, fill=1)
        img= ImageReader("OrthoAligner.png")
        self.pdf.scale(1,-1)
        imgw= 250
        self.pdf.drawImage(img,self.Center(imgw),-150, width= imgw, height= 200, mask='auto', preserveAspectRatio= True, anchor="c")
        self.pdf.scale(1,-1)
        self.pdf.setFillColorRGB(1,1,1)
        self.pdf.setFont("Helvetica",26)
        self.pdf.setStrokeColorRGB(0,0,0)
        self.pdf.drawCentredString(self.width/2,130,"Relatório de Setup Virtual")
    def body(self):
        self.pdf.setFont("Helvetica",13)
        self.bl1= self.pdf.beginText()
        x= "sdajd sdajs das dsda sdas dasdasdasdasdas dasd as dasdasd asd asd asd asd asdasd sad sd ad adasd asd asd asdasd ds asdasdasd asd as"
        self.bl1.setTextOrigin(45,250)
        for line in x:
            (x,y) = self.bl1.getCursor()
            if(x >= 551):
                self.bl1.setTextOrigin(45,y)
                self.bl1.textLine(line)
            self.bl1.textOut(line)
        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.drawText(self.bl1)
        
        print(x,y)
        os.system("pause")
