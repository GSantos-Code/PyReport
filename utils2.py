from PIL import ImageDraw, Image, ImageFont
import textwrap
from ConvGIF import ConvGIF as GIFcv
import os
import shutil
from datetime import date
import zipfile
import time
import datetime
import re
import subprocess
import tkinter as tt
from tkinter import ttk
from tkinter import Tk, Text, Button, END, Label
import main
import Capture
import sys

class Book(main.PyReport):
        def __init__(self, width, height, bg, padx):
                self.data= datetime.date.today()
                self.data= str(self.data.day) + "-" + str(self.data.month) + "-" + str(self.data.year)
                self.log= open("status.log","a+")
                try:
                        super().__init__("14")
                except Exception:
                        self.Reg("Erro no Formulário\n")
                self.calc= 1
                auxv= 0
                self.width= width
                self.Y= 400
                self.tam= 35
                self.fonte= ImageFont.truetype("C:\\Program Files\\PyReport-1600x900\\build\\exe.win-amd64-3.9\\fonts\\Arial.ttf",self.tam)
                self.padx= padx
                self.height= height
                auxdent= self.dentista.split(" ")
                try:
                        dentista= auxdent[0] + " " + auxdent[1]
                except Exception:
                        dentista= self.dentista
                if("a" in self.comment):
                		self.comment= self.comment.replace("\n"," <break> <break> ")
                		self.comment= "Prezado(a) " + dentista + " <break> " + self.comment
                for k in self.comment.split(" "):
                        auxv += 1
                        if(k == "<break>"):
                                self.calc += 1
                        if(auxv % 7 == 0):
                                self.calc += 1
                height= height + (self.calc * 40) - 200
                self.book= Image.new("RGB",(width,height),bg)
                self.draw= ImageDraw.Draw(self.book)
                self.cRect((0,0,self.width,int(340)),(31,91,141))
                self.Textc("Resumo Setup Virtual",(255,255,255),["c",230], 60)
                self.img("C:\\Program Files\\PyReport-1600X900\\build\\exe.win-amd64-3.9\\imgs\\OrthoAligner.png",-7,center= ["c",-60])
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
                if("Fase" in self.pacote or "Refino" in self.pacote):
                		texto += " < " + self.validade + " > "
                texto= texto.replace("|"," <break> ")
                sup= self.sup
                inf= self.inf
                if(self.sup == "0"):
                        sup= "-"
                if(self.inf == "0"):
                        inf= "-"
                self.supp= sup
                self.inff= inf
                texto= texto.format(paciente=self.paciente,sup=sup + self.supatt,inf=inf + self.infatt,total=int(self.sup) + int(self.inf) + int(self.att), extenso=self.extenso(str(int(self.sup) + int(self.inf) + int(self.att))),pacote= self.pacote)
                self.Paragraph(texto)
                self.cRect((0,height-100,width,height),bg=(31,91,141))
                self.Textc("Consulte as informações completas na Ficha de Instruções",(255,255,255),["c",height-70], 40)
                self.book.save(self.path + f"\\12 - Resumo de {self.tsetup} - {self.paciente}.png")
                path= self.path
                self.disp= Tk()
                self.pathc= path
                self.disp.title("O que vamos fazer?")
                self.btn= Button(self.disp, bg="red", text="Capturas", fg="white", relief="flat", font="Arial 15", command= self.Capturas)
                self.btn.pack(pady="3px")
                self.btn1= Button(self.disp, bg="purple", text="Converter GIFs", fg="white", relief="flat", font="Arial 15", command= self.OtAVI)
                self.btn1.pack(pady="3px")
                self.btn2= Button(self.disp, bg="green", text="Otimizar STLs", fg="white", relief="flat", font="Arial 15", command= self.OtSTL)
                self.btn2.pack(pady="3px")
                self.btn3= Button(self.disp, bg="pink", text="Padrão", fg="white", relief="flat", font="Arial 15", command= self.Padrao)
                self.btn3.pack(pady="3px")
                self.disp.config(bg="orange",padx="50px", pady="20px")
                self.disp.mainloop()
                self.log.close()
        def Capturas(self):
                self.disp.destroy()
                try:
                        capture= Capture.CaptureView(self.pathc, self)
                except Exception:
                        self.Reg("Capture error")
        def OtAVI(self):
                self.disp.destroy()
                try:
                        self.conv= ConvGIF(self)
                except Exception:
                        self.Reg("Error in convert GIFS")
        def OtSTL(self):
                self.disp.destroy()
                try:
                        self.convertstls= ConvertSTLs(self)
                except Exception:
                        self.Reg("Error in convert STLs")
        def Padrao(self):
                self.disp.destroy()
                try:
                        capture= Capture.CaptureView(self.pathc, self)
                except Exception:
                        self.Reg("Capture error")
                try:
                        self.conv= ConvGIF(self)
                except Exception:
                        self.Reg("Error in convert GIFS")
                try:
                        self.convertstls= ConvertSTLs(self)
                except Exception:
                        self.Reg("Error in convert STLs")
        def cRect(self,coords,bg):
                self.draw.rectangle(coords,fill=bg)
        def Reg(self,text):
                self.log.write(self.data + " - " + text)
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
        						self.fonte= ImageFont.truetype("C:\\Program Files\\PyReport-1600X900\\build\\exe.win-amd64-3.9\\fonts\\Arial-Bold.ttf",self.tam)
        				elif(i == ">"):
        						self.fonte= ImageFont.truetype("C:\\Program Files\\PyReport-1600X900\\build\\exe.win-amd64-3.9\\fonts\\Arial.ttf",self.tam)
        				else:
        						self.draw.text((cont, self.Y),i,fill= (0,0,0),font= self.fonte)
        						print(cont, cursor)
        						cont= cont + cursor[0] + 10
        def Textc(self,txt,color,c,tam):
                fonte= ImageFont.truetype("C:\\Program Files\\PyReport-1600X900\\build\\exe.win-amd64-3.9\\fonts\\Arial.ttf",tam)
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
                        
class ConvGIF:
        def __init__(self, master):
                self.temp= Tk()
                self.temp.title("Todos os vídeos estão na pasta?")
                self.temp.config(bg="orange", padx="100px", pady="30px")
                btn= Button(self.temp, text="Sim", command= self.go, bg="green", fg="white", relief="flat", font="Arial 18")
                btn.pack(pady="10px")
                self.temp.mainloop()
                self.display= Tk()
                self.display.title("PyReport")
                self.lbl= tt.Label(self.display, text="Verificando vídeos... 0%", fg="white", bg="orange", font="Arial 18")
                self.lbl.pack(pady="10px")
                self.progress= ttk.Progressbar(self.display, mode="determinate", orient="horizontal", length= 100)
                self.progress.pack(pady="10px")
                self.display.config(bg="orange", padx= "30px", pady="30px")
                self.infff= 0
                self.setup= master.path.split("\\")
                self.setup= self.setup[len(self.setup) - 1]
                self.master= master
                self.VerifyFiles()
                self.display.mainloop()
        def go(self):
                self.temp.destroy()
        def StatusBar(self, text, value):
                self.display.update()
                self.lbl["text"]= text
                self.progress["value"] = value
                self.display.update()
        def VerifyFiles(self):
                self.display.update()
                main= self.master.path + "/"
                file1,file2, file3, file4, file8= main + "1.avi", main + "2.avi", main + "3.avi", main + "4.avi", main + "8.avi"
                print(self.master.inff != "-" or self.master.inff != "")
                if(self.master.supp != "-" and self.master.inff != "-"):
                        print(1)
                        while True:
                                if(os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(file3) and os.path.isfile(file4) and os.path.isfile(file8)):
                                        break
                                else:
                                        self.display.update()
                                        time.sleep(2)
                elif(self.master.supp == "-" or self.master.supp == ""):
                        print(2)
                        while True:
                                if(os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(file3) and os.path.isfile(file8)):
                                        break
                                else:
                                        self.display.update()
                                        time.sleep(2)
                elif(self.master.inff == "-" or self.master.inff == ""):
                        print(3)
                        while True:
                                if(os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(file3) and os.path.isfile(file4)):
                                        break
                                else:
                                        self.display.update()
                                        time.sleep(2)
                self.StatusBar("Convertendo vídeos... 40%", 30) 
                self.CFiles("1","Video Vista Lateral Direita")
                self.StatusBar("Convertendo vídeos... 60%", 40)
                self.CFiles("2","Video Vista Frontal")
                self.StatusBar("Convertendo vídeos... 80%", 80)
                self.CFiles("3","Video Vista Lateral Esquerda")
                if("D" in self.master.vest or "D" in self.master.lin or "D" in self.master.ocl):
                        self.CFiles("4","Video Vista Oclusal Superior")
                        self.CFiles("8","Video Vista Oclusal Inferior")
                        self.StatusBar("Convertendo vídeos... 100%", 100)
                        self.display.destroy()
                        return 0;       
                if(self.master.inff == "-" or self.master.inff == ""):
                        self.master.inff= 0
                        self.infff= "-"
                if(self.master.supp != "-" and self.master.supp != ""):
                        if(int(self.master.supp) > int(self.master.inff)):
                                self.CFiles("4","Video Vista Oclusal Superior")
                        else:
                                self.SubFiles("4","Video Vista Oclusal Superior",self.master.supp)
                else:
                        self.master.supp= 0
                if(self.infff == "-"):
                        self.master.inff = self.infff
                if(self.master.inff != "-" and self.master.inff != ""):
                        if(int(self.master.inff) > int(self.master.supp)):
                                self.CFiles("8","Video Vista Oclusal Inferior")
                        else:
                                self.SubFiles("8","Video Vista Oclusal Inferior",self.master.inff)
                else:
                        self.master.inff= 0
                self.StatusBar("Convertendo vídeos... 100%", 100)
                self.display.destroy()
        def CFiles(self,video,name):
                self.video1= GIFcv(f"{self.master.path}\\{video}.avi", f"{self.master.path}\\0{video} - {name} - {self.setup}.gif", pgs=self.lbl, update= self.display.update)
                os.rename(f"{self.master.path}\\{video}.avi",f"{self.master.path}\\0{video} - {name} - {self.setup}.avi")
        def SubFiles(self,video,name, endx):
                self.video1= GIFcv(f"{self.master.path}\\{video}.avi", f"{self.master.path}\\0{video} - {name} - {self.setup}.gif", end= endx, pgs= self.lbl, update= self.display.update)
                os.rename(f"{self.master.path}\\{video}.avi",f"{self.master.path}\\0{video} - {name} - {self.setup}.avi")

class ConvertSTLs:
        def __init__(self, master):
                self.master= master
                self.temp= Tk()
                self.temp.title("Todos os arquivos estão na pasta?")
                self.temp.config(bg="orange", padx="100px", pady="30px")
                self.btn= Button(self.temp, text="Sim", command= self.go, bg="green", fg="white", relief="flat", font="Arial 18")
                self.btn.pack(pady="10px")
                self.temp.mainloop()
        def go(self):
                self.temp.title("Tem IPR?")
                self.btn["command"]= self.yes
                self.btn2= Button(self.temp, text="Não", command= self.no, bg="green", fg="white", relief="flat", font="Arial 18")
                self.btn2.pack()
        def yes(self):
                self.op= "Y"
                self.rename()
        def no(self):
                self.op= "N"
                self.rename()
        def rename(self):
                self.btn.pack_forget()
                self.btn2.pack_forget()
                self.lbl= Label(self.temp, text="Renomeando e convertendo STLs... 0%", bg="orange", fg="white", font="Arial 15")
                self.lbl.pack(pady="10px")
                self.progress= ttk.Progressbar(self.temp, mode="determinate", orient="horizontal", length= 100)
                self.progress.pack(pady="10px")
                try:
                        os.rename(self.master.path + "\\5.jpg",self.master.path + f"\\05 - Sobreposicao {self.master.tsetup} Superior - {self.master.paciente}.jpg")
                except Exception:
                        pass
                try:
                        os.rename(self.master.path + "\\6.jpg",self.master.path + f"\\06 - Sobreposicao {self.master.tsetup} Inferior - {self.master.paciente}.jpg")
                except Exception:
                        pass
                try:
                        os.rename(self.master.path + "\\13.pdf",self.master.path + f"\\13 - Relatorio de {self.master.tsetup} - {self.master.paciente}.pdf")
                except Exception:
                        pass
                if(self.op == "Y"):
                        try:
                                os.rename(self.master.path + "\\7.png",self.master.path + f"\\07 - Relatorio de IPR {self.master.tsetup} - {self.master.paciente}.png")
                        except Exception:
                                try:
                                        os.rename(self.master.path + "\\7.jpg",self.master.path + f"\\07 - Relatorio de IPR {self.master.tsetup} - {self.master.paciente}.jpg")                
                                except Exception:
                                        pass
                else:
                        try:
                                os.rename(self.master.path + "\\7.png",self.master.path + f"\\07 - Vista Frontal - {self.master.tsetup}.png")
                        except Exception:
                                try:
                                        os.rename(self.master.path + "\\7.jpg",self.master.path + f"\\07 - Vista Frontal - {self.master.tsetup}.jpg")
                                except Exception:
                                        pass
                self.lbl["text"]= "Renomeando e convertendo STLs... 20%"
                self.progress["value"]= 20
                self.temp.update()
                time.sleep(1)
                self.processSTL()
        def getSTL(self, model):
                if(not(os.path.exists(f"{os.environ['USERPROFILE']}\\Documents\\Convert"))):
                        os.mkdir(f"{os.environ['USERPROFILE']}\\Documents\\Convert")
                self.localdoc= f"{os.environ['USERPROFILE']}\\Documents\\Convert"
                shutil.move(f"{self.master.path}\\{model}",f"{self.localdoc}\\{model}")
                return f'"C:\Program Files\VCG\MeshLab\meshlabserver.exe" -i "{self.localdoc}\{model}" -o "{self.localdoc}\{model}" -s C:\multimeshscripting\scripts\simple_script.mlx -om vc fq wn'
        def processSTL(self):
                DETACHED_PROCESS = 0x00000008
                script= self.getSTL("15.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\15.stl", self.master.path + f"\\15 - Modelo Original Superior - {self.master.paciente}.stl")
                except Exception:
                        pass
                script= self.getSTL("16.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\16.stl", self.master.path + f"\\16 - Modelo Original Inferior - {self.master.paciente}.stl")
                except Exception:
                        pass
                script= self.getSTL("17.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\17.stl", self.master.path + f"\\17 - Modelo {self.master.tsetup} Superior - {self.master.paciente}.stl")
                except Exception:
                        pass
                script= self.getSTL("18.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\18.stl", self.master.path + f"\\18 - Modelo {self.master.tsetup} Inferior - {self.master.paciente}.stl")
                except Exception:
                        pass
                filestozip= []
                self.lbl["text"]= "Renomeando e convertendo STLs... 70%"
                self.progress["value"]= 70
                self.temp.update()
                time.sleep(1)
                
                self.lbl["text"]= "Compactando arquivos... 90%"
                self.progress["value"]= 90
                self.temp.update()
                time.sleep(1)
                for i in os.listdir(self.master.path):
                        if(".avi" in i):
                                continue
                        else:
                                filestozip.append(self.master.path + "\\" + i)

                dtsetup= date.today()
                self.ttsetup= self.master.tsetup.replace(" ","_")
                dtsetup= self.ttsetup + f"_{dtsetup.day}_{dtsetup.month}_{dtsetup.year}"
                
                filezip= zipfile.ZipFile(self.master.path + f"\\{dtsetup}.zip", 'w')

                for f in filestozip:
                        k= f.split("\\")
                        fname= k[len(k) - 1]
                        filezip.write(f,fname, compress_type = zipfile.ZIP_DEFLATED)
                filezip.close()
                self.temp.destroy()
                
                
                
k = Book(1104,1600,(255,255,255),40)



