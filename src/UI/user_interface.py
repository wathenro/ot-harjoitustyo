from tkinter import Label,StringVar,OptionMenu,Button,Entry
from PIL import Image,ImageTk
from loaders.location_loader import LocLoader
from loaders.map_maker import MapMaker
from optimizers.optimizer import Optimizer

class UI():
    def __init__(self,window):
        self.window=window
        self.window.title("Railroad Designer")
        self.window.geometry("768x512")
        #Photo by Brian Suman on Unsplash
        try:
            self.train_img = ImageTk.PhotoImage(Image.open("src/data/train.jpg"))
        except:
            self.train_img = ImageTk.PhotoImage(Image.open("data/train.jpg"))
        self.train_imglabel = Label(self.window, image=self.train_img)
        self.train_imglabel.place(x=512,y=0)
        
        try:
            self.img = ImageTk.PhotoImage(Image.open("src/data/rataverkko.jpg"))
        except:
            self.img = ImageTk.PhotoImage(Image.open("data/rataverkko.jpg"))
        self.imglabel = Label(self.window, image=self.img)
        self.imglabel.image=self.img
        self.imglabel.pack(side="left")

        self.communities=LocLoader().location_loader()

        self.startCityMenu = StringVar()
        self.startCityMenu.set("Hanko")
        startMenu = OptionMenu(self.window, self.startCityMenu,*self.communities.index.tolist())
        startMenu.place(x=550,y=100)

        self.endCityMenu = StringVar()
        self.endCityMenu.set("Sodankylä")
        endMenu = OptionMenu(self.window, self.endCityMenu,*self.communities.index.tolist())
        endMenu.place(x=650,y=100)

        self.sign_max_track=Label(self.window,text="Maximum track length")
        self.sign_max_track.place(x=550,y=150)

        self.max_track_box=Entry(self.window)
        self.max_track_box.insert(0, 1000)
        self.max_track_box.place(x=550,y=175)

        design_button=Button(self.window, text='Design', command=self.design, width=10)
        design_button.place(x=550,y=200)
        
        self.opt_max_track=Label(self.window,text="Optimized track length")
        self.opt_max_track.place(x=550,y=225)

        self.opt_track_length=0 
        self.opt_track_box=Entry(self.window)
        self.opt_track_box.insert(0, self.opt_track_length)
        self.opt_track_box.place(x=550,y=250)

        self.save_track_button=Button(self.window, text='Save track', command=self.design, width=10)
        self.save_track_button.place(x=550,y=300)

        self.load_track_button=Button(self.window, text='Load track', command=self.design, width=10)
        self.load_track_button.place(x=650,y=300)

        self.make_report_button=Button(self.window, text='Make report', command=self.design, width=10)
        self.make_report_button.place(x=550,y=330)

    def design(self):
        startCityMenu=str(self.startCityMenu.get())
        endCityMenu=str(self.endCityMenu.get())
        try:
            max_track=int(self.max_track_box.get())
        except:
            max_track=10000

        created_map,c_on_map=MapMaker().make_map(startCityMenu,endCityMenu,self.communities.copy())

        created_map,c_on_map,self.opt_track_length=Optimizer().optimizer(created_map,c_on_map,max_track)
        
        self.opt_track_box.delete(0,40)
        self.opt_track_box.insert(0, self.opt_track_length)

        self.make_image(created_map)
    
    def make_image(self,created_map):
        map_image=Image.fromarray(created_map,"RGB")
        self.img = ImageTk.PhotoImage(map_image)
        self.imglabel.configure(image=self.img)
        self.imglabel.image=self.img
         