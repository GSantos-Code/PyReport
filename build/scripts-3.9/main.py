import utils
import sys
from tkinter import *

class PyReport(utils.auxtools):
        def __init__(self, pdfname):
                self.i= Tk()
                self.validade= ""
                self.supatt= ""
                self.infatt= ""
                self.i.config(bg="orange")
                self.i.title("PyReport")
                self.i.state("zoomed")
                self.frame= Frame(self.i, bg="orange")
                self.frame.pack(pady="50px", padx="10px")
                self.frame2= Frame(self.i, bg="orange")
                self.frame2.pack()
                self.lb1= Label(self.frame, bg="orange",fg="white", text="Nome do paciente", font= "Arial 25 bold")
                self.lb1.pack()
                self.entrada1= Entry(self.frame, font="Arial 20", justify="center", fg= "black", relief= FLAT)
                self.entrada1.pack(pady="30px")
                self.lb2= Label(self.frame, bg="orange",fg="white", text="Nome do Dentista", font= "Arial 25 bold")
                self.lb2.pack()
                self.entrada2= Entry(self.frame, font="Arial 20", justify="center", fg= "black", relief= FLAT)
                self.entrada2.pack(pady="30px")
                self.btn= Button(self.frame, relief= FLAT, text="Proximo" ,font="Arial 20", bg="green", fg="white" ,command=self.step0)
                self.btn.pack(pady="10px",side=BOTTOM)
                self.i.mainloop()
                super().__init__(self.path + f"/14 - Relatorio de Instrucoes {self.tsetup} - {self.paciente}")
        def clear(self):
                self.entrada1.delete(0,END)
                self.entrada2.delete(0,END)
        def step0(self):
                self.paciente= self.entrada1.get()
                self.dentista= self.entrada2.get()
                self.clear()
                self.lb1["text"]= "Digite o Caminho da Pasta"
                self.lb2.pack_forget()
                self.entrada2.pack_forget()
                self.btn["command"] = self.step2
        def step2(self):
                self.path= self.entrada1.get()
                self.tsetup= self.path.split("\\")
                self.tsetup= self.tsetup[len(self.tsetup) - 1]
                self.clear()
                self.lb1["text"]= "Nome do Ortodontista"
                self.lb2["text"]= "Face Vestibular"
                self.btn["command"]= self.step3
                self.btn.pack_forget()
                self.lb2.pack()
                self.entrada2.pack()
                self.btn.pack(pady="10px",side=BOTTOM)
        def step3(self):
                self.ortodont= self.entrada1.get()
                self.vest= self.entrada2.get()
                self.clear()
                self.lb1["text"]= "Face Lingual"
                self.lb2["text"]= "Face Oclusal"
                self.btn["command"]= self.step4
        def step4(self):
                self.att= 0
                self.lin= self.entrada1.get()
                self.ocl= self.entrada2.get()
                self.clear()
                sup= ["11","12","13","14","15","16","17","18","21","22","23","24","25","26","27","28"]
                inf= ["31","32","33","34","35","36","37","38","41","42","43","44","45","46","47","48"]
                for i in sup:
                        if(i in self.vest or i in self.lin or i in self.ocl):
                                self.att += 1
                                self.supatt= " + Attach"
                                break
                for i in inf:
                        if(i in self.vest or i in self.lin or i in self.ocl):
                                self.att += 1
                                self.infatt= " + Attach"
                                break
                if("D" in self.vest or "D" in self.lin or "D" in self.ocl):
                        self.att= 2
                        self.supatt= " + Attach"
                        self.infatt= " + Attach"
                        self.vest="-"
                        self.lin= "-"
                        self.ocl= "-"
                self.lb1["text"]= "Quant Sup"
                self.lb2["text"]= "Quant Inf"
                self.btn["command"]= self.step5
        def step5(self):
                self.sup= self.entrada1.get()
                self.inf= self.entrada2.get()
                self.clear()
                self.lb1["text"]= "Qual Pacote"
                self.lb2["text"]= "Comentário"
                self.lb2["pady"]= "30px"
                self.entrada2.pack_forget()
                S = Scrollbar(self.frame)
                T = Text(self.frame, height=7, width=100, wrap=WORD, relief= FLAT, font="Arial 15 bold")
                S.pack(side=RIGHT, fill=Y)
                T.pack(side=LEFT, fill=Y)
                S.config(command=T.yview)
                T.config(yscrollcommand=S.set)
                self.TextArea= T
                self.scroll= S
                self.btn.pack_forget()
                self.btn= Button(self.frame2, relief= FLAT, text="Gerar PDF" ,font="Arial 20", bg="green", fg="white" ,command=self.step6)
                self.btn.pack(pady="10px")
        def step6(self):
                self.pacote= self.entrada1.get()
                self.comment= self.TextArea.get("1.0",END)
                self.comment= self.comment.replace("\n","|")
                self.clear()
                if("Refino" in self.pacote or "Fase" in self.pacote):
                        self.TextArea.pack_forget()
                        self.scroll.pack_forget()
                        self.lb2.pack_forget()
                        self.lb1["text"] = "Texto da Validade"
                        self.btn["text"]= "Pronto"
                        self.btn["command"] = self.step7
                else:
                        self.i.destroy()
        def step7(self):
                self.validade= self.entrada1.get()
                self.i.destroy()
