from tkinter import Label,StringVar,OptionMenu,Button
import numpy as np
from PIL import ImageTk
from location_loader import LocLoader
from map_maker import MapMaker

class UI():
    def __init__(self,window):
        self.window=window

        self.initial_created_map=np.zeros((512,512,3), dtype=np.uint8)+50
        self.map_image=MapMaker().make_image(self.initial_created_map)
        self.img = ImageTk.PhotoImage(self.map_image)
        self.imglabel = Label(self.window, image=self.img)
        self.imglabel.image=self.img
        self.imglabel.pack(side="left")

        self.communities=LocLoader().location_loader()

        self.startCityMenu = StringVar()
        self.startCityMenu.set("Start at")
        startMenu = OptionMenu(self.window, self.startCityMenu,*self.communities.index.tolist())
        startMenu.place(x=550,y=100)

        self.endCityMenu = StringVar()
        self.endCityMenu.set("End at")
        endMenu = OptionMenu(self.window, self.endCityMenu,*self.communities.index.tolist())
        endMenu.place(x=650,y=100)

        design_button=Button(self.window, text='Design', command=self.design, width=10)
        design_button.place(x=550,y=180)

    def design(self):
        startCityMenu=str(self.startCityMenu.get())
        endCityMenu=str(self.endCityMenu.get())

        created_map,c_on_map=MapMaker().make_map(startCityMenu,endCityMenu,self.communities.copy())

        map_image=MapMaker().make_image(created_map)
        self.img = ImageTk.PhotoImage(map_image)
        self.imglabel.configure(image=self.img)
        self.imglabel.image=self.img
    