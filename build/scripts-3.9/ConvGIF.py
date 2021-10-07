import cv2
import time
from PIL import Image
import subprocess
import imageio
import os

class ConvGIF:
    def __init__(self,video,name, pgs, update, end= 1000000000000000000000000000):
        frames = []
        progress= pgs
        self.progress= pgs
        self.name= name
        self.update= update
        self.video= video
        if(int(end) < 10000):
            end = int(end) * 15
        cap= cv2.VideoCapture(self.video)
        image_count = 0
        progress["text"]= "Processando video..."
        update()
        while True:
            ret, frame = cap.read()
            if(ret == 1):
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image_count += 1
                frames.append(rgb_frame)
                update()
                if(image_count == int(end) + 8):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        progress["text"]= "Salvando GIF..."
        update()
        with imageio.get_writer(self.name, mode="I", fps=30) as writer:
            for idx, frame in enumerate(frames):
                writer.append_data(frame)
                update()
        self.Optimize()
    def Optimize(self):
        self.progress["text"]= "Otimizando GIF..."
        self.update()
        gifsicle= r"C:\Program Files\PyReport-1600X900\build\exe.win-amd64-3.9\tools\gifsicle.exe"
        DETACHED_PROCESS = 0x00000008
        subprocess.call(f'"{gifsicle}" -i "{self.name}" -O3 --colors 256 -o "{self.name}"', creationflags=DETACHED_PROCESS)
