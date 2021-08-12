from PIL import ImageDraw, Image, ImageFont

class Book:
        def __init__(self, width, height, bg):
                self.width= width
                self.height= height
                self.book= Image.new("RGB",(width,height),bg)
                self.draw= ImageDraw.Draw(self.book)
                self.cRect((0,0,self.width,int((20*height)/100)),(31,91,141))
                self.Text()
                self.img("imgs/OrthoAligner.png",-7,center= ["c",-60])
                self.book.save("12.png")
        def cRect(self,coords,bg):
                self.draw.rectangle(coords,fill=bg)
        def Text(self):
                fonte= ImageFont.truetype("fonts/Helvetica.ttf")
                self.teste= self.draw.text((50,300),"Teste",fill=(0,0,0),font=fonte)
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
k = Book(1104,1700,(255,255,255))
