import utils
import sys
from tkinter import *

class PyReport(utils.auxtools):
        def __init__(self, pdfname):
                self.i= Tk()
                self.i.config(bg="orange")
                self.frame= Frame(self.i, bg="orange")
                self.comment= "asd"
                self.nome= "Gabriel Henrique"
                self.frame.pack(pady="10px", padx="10px")
                self.lb1= Label(self.frame, bg="orange",fg="white", text="Nome do paciente", font= "Arial 18 bold")
                self.lb1.pack()
                self.entrada1= Entry(self.frame, font="Arial 15", justify="center", fg= "orange")
                self.entrada1.pack(pady="10px")
                self.lb2= Label(self.frame, bg="orange",fg="white", text="Nome do Dentista", font= "Arial 18 bold")
                self.lb2.pack()
                self.entrada2= Entry(self.frame, font="Arial 15", justify="center", fg= "orange")
                self.entrada2.pack(pady="10px")
                self.btn= Button(self.frame, text="Proximo" ,font="Arial 15", bg="green", fg="white" ,command=self.step2)
                self.btn.pack(pady="10px")
                self.i.mainloop()
                super().__init__(pdfname)
        def step2(self):
                self.paciente= self.entrada1.get()
                self.dentista= self.entrada2.get()
                self.lb1["text"]= "Nome do Ortodontista"
                self.lb2["text"]= "Face Vestibular"
                self.btn["command"]= self.step3
        def step3(self):
                self.ortodont= self.entrada1.get()
                self.vest= self.entrada2.get()
                self.lb1["text"]= "Face Lingual"
                self.lb2["text"]= "Face Oclusal"
                self.btn["command"]= self.step4
        def step4(self):
                self.att= 0
                self.lin= self.entrada1.get()
                self.ocl= self.entrada2.get()
                sup= ["11","12","13","14","15","16","17","18","21","22","23","24","25","26","27","28"]
                inf= ["31","32","33","34","35","36","37","38","41","42","43","44","45","46","47","48"]
                for i in sup:
                        if(i in self.vest or i in self.lin or i in self.ocl):
                                self.att= 1
                for i in inf:
                        if(i in self.vest or i in self.lin or i in self.ocl):
                                self.att= 2
                self.lb1["text"]= "Quant Sup"
                self.lb2["text"]= "Quant Inf"
                self.btn["command"]= self.step5
        def step5(self):
                self.sup= self.entrada1.get()
                self.inf= self.entrada2.get()
                self.lb1["text"]= "Qual Pacote"
                self.lb2["text"]= "Comentário"
                self.entrada2.pack_forget()
                S = Scrollbar(self.frame)
                T = Text(self.frame, height=4, width=50, wrap=WORD)
                S.pack(side=RIGHT, fill=Y)
                T.pack(side=LEFT, fill=Y)
                S.config(command=T.yview)
                T.config(yscrollcommand=S.set)
                self.TextArea= T
                self.btn["text"]= "Gerar PDF"
                self.btn["command"]= self.step6
                self.btn.pack_forget()
                self.btn.pack(pady="10px")
        def step6(self):
                self.pacote= self.entrada1.get()
                self.comment= self.TextArea.get("1.0",END)
                self.i.destroy()
x= PyReport("TESTE")
