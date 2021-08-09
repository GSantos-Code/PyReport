from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
from reportlab.rl_config import defaultPageSize
import os

class auxtools(object):
    def __init__(self, pdfname):
        self.width= 596
        self.enter= 0
        self.aux= 0
        self.qp= 0
        self.aux2= ""
        self.pagebreak= 0
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
        self.pdf.rect(0,0,827,160, fill=1)
        img= ImageReader("OrthoAligner.png")
        self.pdf.scale(1,-1)
        imgw= 250
        self.pdf.drawImage(img,self.Center(imgw),-150, width= imgw, height= 200, mask='auto', preserveAspectRatio= True, anchor="c")
        self.pdf.scale(1,-1)
        self.pdf.setFillColorRGB(1,1,1)
        self.pdf.setFont("Helvetica",26)
        self.pdf.setStrokeColorRGB(0,0,0)
        self.pdf.drawCentredString(self.width/2,130,"Relatório de Setup Virtual")
    def write(self,texto):
        if(self.enter == 1):
            self.bl2= self.pdf.beginText()
            self.bl2.setTextOrigin(40,50)
        for line in texto:
            (x,y) = self.bl2.getCursor()
            if(self.pagebreak == 1):
                self.aux2 += line
            elif(line == "|"):
                self.bl2.setTextOrigin(40,y)
                self.bl2.textLine()
            elif(x >= 512 and line == " "):
                self.bl2.setTextOrigin(40,y)
                self.bl2.textLine(line)  
            else:
                if(line == "<"):
                    self.bl2.setFont("Helvetica-Bold",13)
                elif(line == ">"):
                    self.bl2.setFont("Helvetica",13)
                elif(line == "%"):
                    self.bl2.textLine()
                    (x,y) = self.bl2.getCursor()
                    if(y + 200 >= 744):
                        self.aux2= ""
                        self.enter= 1
                        self.pdf.drawText(self.bl2)
                        self.pdf.showPage()
                        x= 40
                        y= 50
                        self.pagebreak= 1
                    self.pdf.setFillColorRGB(219/255,229/255,241/255)
                    self.pdf.setStrokeColorRGB(75/255,172/255,198/255)
                    self.pdf.rect(x,y,width=512,height= 200, fill=1)
                    self.pdf.setFillColorRGB(1/255,64/255,191/255)
                    self.pdf.setFont("Helvetica-Bold",18)
                    self.pdf.drawCentredString(552/2,y+30,"   Casos OrthoAligner ONE e PRO")
                    self.pdf.line(x,y+45,x+512,y+45)
                    self.pdf.setFont("Helvetica",13)
                    txt= "Se o seu tratamento se encaixou em um pacote ONE e PRO, você receberá | somente até a etapa 10, para acompanharmos com você a evolução do caso.||"
                    txt += "Por isso, quando estiver finalizando essa fase e o tratamento estiver avançando |conforme o planejado, você deve solicitar o restante dos alinhadores através do |e-mail:|| &contato@compass3d.com.br# "
                    bl3= self.pdf.beginText()
                    xcp= x+20
                    ycp= y+70
                    bl3.setTextOrigin(xcp,ycp)
                    bl3.setFillColorRGB(0,0,0)
                    for i in range(0,16):
                        self.bl2.textLine()
                    for pp in txt:
                        (k,l) = bl3.getCursor()
                        if(pp == "|"):
                            bl3.setTextOrigin(xcp,l)
                            bl3.textLine()
                        elif(x >= 512 and line == " "):
                            bl3.setTextOrigin(xcp,l)
                            bl3.textLine(line)
                        elif(pp == "&"):
                            bl3.setTextOrigin(((512-xcp)/2)-20,l)
                            bl3.setFont("Helvetica",14)
                            self.coords[0]= k
                            self.coords[1]= l
                            bl3.setFillColorRGB(0,0,0.4)
                        elif(pp == "#"):
                            self.coords[2]= k
                            self.coords[3]= l
                            bl3.setFillColorRGB(0,0,0)
                            bl3.setFont("Helvetica",13)
                        else:
                            bl3.textOut(pp)
                    (k,l) = bl3.getCursor()
                    self.pdf.drawText(bl3)
                    self.pdf.linkURL("mailto:contato@compass3d.com.br",self.coords, relative=1)
                    self.pdf.setFont("Helvetica",13)
                    self.pdf.setStrokeColorRGB(1,1,1)
                elif(line == "&"):
                    self.coords[0]= x
                    self.coords[1]= y
                    self.bl2.setFillColorRGB(0,0,0.4)
                elif(line == "#"):
                    self.coords[2]= x
                    self.coords[3]= y
                    self.bl2.setFillColorRGB(0,0,0)
                else:
                    if(y >= 744):
                        self.enter= 1
                        self.aux2= ""
                        self.pdf.drawText(self.bl2)
                        self.pdf.showPage()
                        self.pagebreak= 1
                        self.aux2 += line
                    self.bl2.textOut(line)
        if(self.pagebreak == 1):
            self.pagebreak= 0
            self.write(self.aux2)
            self.pdf.drawText(self.bl2)
        if(self.enter == 0):
            self.pdf.drawText(self.bl2)
    def rodape(self):
        self.pdf.setFillColorRGB(31/255,91/255,141/255)
        self.pdf.setStrokeColorRGB(31/255,91/255,141/255)
        self.pdf.rect(0,744,width= self.width, height= 300, fill=1)
    def body(self):
        self.pdf.setFont("Helvetica",13)
        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.drawString(40,200, "Prezado")
        self.pdf.setFont("Helvetica-Bold",13)
        self.pdf.drawString(96,200, "Dr(a) " + self.nome)
        x= 40
        y= 230
        '''if(self.comment != ""):
            self.bl1= self.pdf.beginText()
        '''
        texto0= "É importante tambem sadasd,samdsd ssadsad sadsadasdasdas dasdasd asd as asd asd asdas dsad  sad asde bom vc saber que terminei meudsfsdf||||||||||||||||||||||||| adasdasdasd ddas dasd as das d namoro agora vou ter que achar outra pessoa pra me fazer companhia me ajuda alguem da moral ai valeu falou ok blz okas masdmsa dmsd am msad msalientar que o caso do Matheus se trata de um caso bastante complexo então peço que reavalie as condições e veja se é isso mesmo que vc quer porque o risco do caso der um PRO é enorme, e se der e você tiver comprado um ONE teria que pagar placas extras o paciente não concordaria com tal questão e você teria que arcar com fundo da sua clinica Obrigado"
        texto0 += "||"
        '''    self.pdf.setFont("Helvetica",13)
            self.bl1.setTextOrigin(int(x),int(y))
            for line in texto0:
                (x,y) = self.bl1.getCursor()
                if(line == "|"):
                    self.bl1.setTextOrigin(x,y)
                    self.bl1.textLine("")
                elif(x >= 530 and line == " "):
                    self.bl1.setTextOrigin(40,y)
                    self.bl1.textLine(line)
                else:
                    self.bl1.textOut(line)
            self.pdf.drawText(self.bl1)
            self.bl1.textLine()
            (x,y) = self.bl1.getCursor()'''
        x= 40
        self.bl2= self.pdf.beginText()
        texto = "{comment}||"
        texto= texto + "O Setup Virtual para <{Paciente}> foi realizado conforme suas instruções.||Modelos virtuais anexados mostram o resultado do setup virtual e poderão ser visualizados no software gratuito 3Shape Viewer.||"
        texto= texto + "<Poderá ser necessário refinamento após o término da movimentação ortodôntica em virtude da característica de alguns movimentos dentários solicitados, da complexidade do caso, da resposta biológica de cada paciente, do uso correto e contínuo do aparelho, da condução do tratamento, entre outros.>||"
        texto= texto + "O refinamento deverá ser solicitado através do e-mail &contato@compass3d.com.br# e novos modelos (ambas as arcadas) deverão ser enviados. Se optar por realizar nova moldagem, haverá necessidade de retirada dos attachments presentes para não ocorrer distorções nos modelos em gesso. Caso a opção seja o escaneamento intraoral, não há necessidade da retirada dos attachments.||"
        texto= texto + "Para realizar a etapa inicial do presente planejamento, serão necessários:||Alinhadores Superiores: <{sup}>|Alinhadores Inferiores: <{inf}>||"
        texto= texto + "Está indicado uso de attachments para maior controle do movimento dentário, para os elementos identificados abaixo:||"
        texto= texto + "Face Vestibular: {v}|Face Lingual: {l}|Face Oclusal: {o}||"
        texto= texto + "Os attachments deverão ser instalados com o guia correspondente para cada arcada, confeccionado em placa de acetato 0,3mm enviada para este fim, antes de iniciar o uso do primeiro alinhador OrthoAligner."
        texto= texto + "Isto implica em mais {att} modelos prototipados (identificados como “0”) e os respectivos guias para instalação dos attachments.||Total de alinhadores: <{quant}({extenso})>.||O caso será tratado com um <OrthoAligner {pacote}>.||"
        texto= texto + "Você poderá escolher o tipo de placa utilizada para o tratamento entre <Ultimate> e <FLX>.|As placas <Ultimate> são mais finas, mais confortáveis e mais resistentes a manchas.|As placas <FLX> possuem maior resistência, flexibilidade e forças mais constantes||."
        texto= texto + "Além disso, você também pode optar pelo <recorte padrão> (corte reto, 2mm acima da margem gengival) ou <recorte cervical> com contorno gengival.||"
        texto= texto + "Lembrando que a escolha das placas e do recorte deve ser baseada na experiência do profissional e em especial no caso a ser tratado.||"
        texto= texto + "<Verifique com o seu consultor com relação aos custos do pacote indicado, placas e recorte escolhido.>||%"
        texto= texto + "Está indicado a realização de ajuste oclusal durante e após a movimentação dentária sugerida neste setup.||A situação periodontal do paciente deve ser mantida sob controle, como em todo tratamento ortodôntico.||"
        texto= texto + "Em geral, os alinhadores ortodônticos devem ser utilizados em tempo integral, dia e noite e devem ser retirados para a mastigação e higiene bucal.||"
        texto= texto + "A substituição dos alinhadores Ortho Aligner deve ocorrer a intervalos de quinze a vinte dias, observadas as características de cada paciente, tais como idade, saúde geral, bucal e periodontal, ou ainda a critério do profissional responsável pelo tratamento.||"
        texto= texto + "Em casos com indicação de desgastes interproximais (Stripping/IPR), a quantidade e locais a serem feitos esses desgastes estão assinalados no arquivo PDF anexo. Os desgastes interproximais deverão ser iniciados já na instalação dos primeiros alinhadores e prosseguir a taxa de 0,1mm por etapa subsequente.||"
        texto= texto + "A contenção pós tratamento deverá ser instalada após o uso do último alinhador.||"
        texto= texto + "<Informamos que caso seja solicitada a alteração do setup, iremos acrescentar mais (2) dois dias úteis no prazo de entrega do planejamento para o envio do mesmo.>||"
        texto= texto + "<{ortodont}>|Compass3D"
        texto= texto.format(comment= texto0,Paciente= self.nome,sup=5,inf=5,v="-",l="-",o="-",att="dois",quant="10",extenso="dez",pacote="FULL",ortodont="Diogo Frazão")
        self.bl2.setTextOrigin(int(x),int(y))
        self.coords = [0,0,0,0]
        self.write(texto)
        self.rodape()
        self.pdf.linkURL('mailto:contato@compass3d.com.br', self.coords, relative=1)
