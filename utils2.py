from PIL import ImageDraw, Image, ImageFont
import textwrap
import os
import re
import tkinter as tt
from tkinter import Tk, Text, Button, END
import main
import Capture

class Book(main.PyReport):
        def __init__(self, width, height, bg, padx):
                super().__init__("14")
                self.width= width
                self.Y= 400
                self.tam= 35
                self.fonte= ImageFont.truetype("fonts/Arial.ttf",self.tam)
                self.padx= padx
                self.height= height
                if("a" in self.comment):
                		height= 2300
                		self.comment= self.comment.replace("\n"," <break> ")
                self.book= Image.new("RGB",(width,height),bg)
                self.draw= ImageDraw.Draw(self.book)
                self.cRect((0,0,self.width,int(340)),(31,91,141))
                self.Textc("Resumo Setup Virtual",(255,255,255),["c",230], 60)
                self.img("imgs/OrthoAligner.png",-7,center= ["c",-60])
                texto= "O Setup Virtual para < {paciente} > foi planejado conforme suas instruções."
                if("a" in self.comment):
                	texto += " <break> <break> " + self.comment + " <break> "
                texto += " <break> <break> Para realizar a etapa do presente planejamento, serão necessários: "
                texto += "<break> <break> Alinhadores Superiores: < {sup} > "
                texto += "<break> Alinhadores Inferiores: < {inf} > "
                texto += "<break> <break> Total de Alinhadores: < {total}({extenso}) > <break> <break>"
                if("Fase" in self.pacote or "Refino" in self.pacote):
                		texto += " < "
                if(self.pacote == "Fase II"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I"
                elif(self.pacote == "Fase III"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II"
                elif(self.pacote == "Fase IV"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II, III"
                elif(self.pacote == "Fase V"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II, III, IV"
                elif(self.pacote == "Fase VI"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II, III, IV, V"
                if(self.pacote == "Refino II"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I"
                elif(self.pacote == "Refino III"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II"
                elif(self.pacote == "Refino IV"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II, III"
                elif(self.pacote == "Refino V"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II, III, IV"
                elif(self.pacote == "Refino VI"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II, III, IV, V"
                texto += " > <break> O caso será tratado com um < OrthoAligner {pacote} > <break>"
                validade= "Ilimitado ate agosto/2022"
                if("Fase" in self.pacote or "Refino" in self.pacote):
                		texto += " < " + validade + " > "
                texto= texto.replace("|"," <break> ")
                texto= texto.format(paciente=self.paciente,sup=str(self.sup) + self.supatt,inf=str(self.inf) + self.infatt,total=int(self.sup) + int(self.inf), extenso=self.extenso(str(int(self.sup) + int(self.inf))),pacote= self.pacote)
                self.Paragraph(texto)
                self.cRect((0,height-100,width,height),bg=(31,91,141))
                self.Textc("Consulte as informações completas na Ficha de Instruções",(255,255,255),["c",height-70], 40)
                self.book.save(self.path + "/" + "12.png")
                path= self.path
                capture= Capture.CaptureView(path)
                capture.capture()
        def cRect(self,coords,bg):
                self.draw.rectangle(coords,fill=bg)
        def Paragraph(self,txt):
        		temp= " "
        		cont= 40
        		txt= re.split(" ",txt)
        		print(txt)
        		cursor= self.padx
        		for i in txt:
        				try:
        						cursor= self.get_text_dimensions(i, self.fonte)
        				except Exception:
        						pass
        				if(cont >= self.width - (self.padx * 2) - 130):
        						cont= self.padx
        						self.Y += 37
        				if(i == "<break>" or i == "\n"):
        						print("entrei")
        						cont= self.padx
        						self.Y += 37
        						i = i.replace("<break>","")
        						print(i)
        				elif(i == "<"):
        						self.fonte= ImageFont.truetype("fonts/Arial-Bold.ttf",self.tam)
        				elif(i == ">"):
        						self.fonte= ImageFont.truetype("fonts/Arial.ttf",self.tam)
        				else:
        						self.draw.text((cont, self.Y),i,fill= (0,0,0),font= self.fonte)
        						print(cont, cursor)
        						cont= cont + cursor[0] + 10
        def Textc(self,txt,color,c,tam):
                fonte= ImageFont.truetype("fonts/Arial.ttf",tam)
                if("c" in c):
                	x= self.draw.textlength(txt, font= fonte)
                	self.draw.text((int((self.width-x)/2),c[1]),txt,fill=color,font=fonte)
        def get_text_dimensions(self,text_string, font):
        		# https://stackoverflow.com/a/46220683/9263761
        		ascent, descent = font.getmetrics()
        		text_width = font.getmask(text_string).getbbox()[2]
        		text_height = font.getmask(text_string).getbbox()[3] + descent
        		return [text_width, text_height]
        def img(self,fp,scale,center):
                img= Image.open(fp)
                if(scale >= 1):
                        img= img.resize((img.size[0]*scale,img.size[1]*scale))
                else:
                        scale *= -1
                        img= img.resize((int(img.size[0]/scale),int(img.size[1]/scale)))
                if("c" in center):
                        self.book.paste(img,(int((self.width - img.size[0])/2),center[1]),mask=img)
                else:
                        self.book.paste(img,center[0],center[1],mask=img)
k = Book(1104,1700,(255,255,255),40)
