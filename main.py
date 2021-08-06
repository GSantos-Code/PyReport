import utils
import sys
from tkinter import *

class PyReport(utils.auxtools):
        def __init__(self, pdfname):
                self.i= Tk()
                self.i.config(bg="orange")
                self.frame= Frame(self.i, bg="orange")
                self.frame.pack(pady="10px", padx="10px")
                self.lb1= Label(self.frame, bg="orange",fg="white", text="Nome do paciente", font= "Arial 18 bold")
                self.lb1.pack()
                self.entrada1= Entry(self.frame, font="Arial 15", justify="center", fg= "orange")
                self.entrada1.pack(pady="10px")
                self.i.mainloop()
                super().__init__(pdfname)
                
x= PyReport("TESTE")
