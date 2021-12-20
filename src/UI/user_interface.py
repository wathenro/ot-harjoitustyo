from tkinter import Label,StringVar,OptionMenu,Button,Entry
from PIL import Image,ImageTk
from loaders.location_loader import LocLoader
from loaders.map_maker import MapMaker
from loaders.report_maker import ReportMaker
from optimizers.optimizer import Optimizer

class UI():
    """User interface for the Railroad designer
    
    Attributes:
        window: tkinter main window
    """
    def __init__(self,window):
        """UI constructor
    
        Args:
            window: tkinter main window
        """
        self.window=window
        self.window.title("Railroad Designer")
        self.window.geometry("768x512")
        #Photo by Brian Suman on Unsplash
        try:
            self.train_img = ImageTk.PhotoImage(Image.open("src/data/train.jpg"))
        except FileNotFoundError:
            self.train_img = ImageTk.PhotoImage(Image.open("data/train.jpg"))
        self.train_imglabel = Label(self.window, image=self.train_img)
        self.train_imglabel.place(x=512,y=0)
        
        try:
            self.img = ImageTk.PhotoImage(Image.open("src/data/rataverkko.jpg"))
        except FileNotFoundError:
            self.img = ImageTk.PhotoImage(Image.open("data/rataverkko.jpg"))
        self.imglabel = Label(self.window, image=self.img)
        self.imglabel.image=self.img
        self.imglabel.pack(side="left")

        self.communities=LocLoader().location_loader()

        self.label_choose=Label(self.window,text="Choose start and end stations:")
        self.label_choose.place(x=550,y=150)

        self.startCityMenu = StringVar()
        self.startCityMenu.set("Helsinki")
        startMenu = OptionMenu(self.window, self.startCityMenu,*self.communities.index.tolist())
        startMenu.config(bg="GREEN")
        startMenu.place(x=550,y=175)

        self.endCityMenu = StringVar()
        self.endCityMenu.set("Porvoo")
        endMenu = OptionMenu(self.window, self.endCityMenu,*self.communities.index.tolist())
        endMenu.config(bg="RED")
        endMenu.place(x=650,y=175)

        self.sign_max_track=Label(self.window,text="Type max track length and click Design")
        self.sign_max_track.place(x=550,y=215)

        self.max_track_box=Entry(self.window)
        self.max_track_box.insert(0, 1000)
        self.max_track_box.place(x=550,y=240)

        design_button=Button(self.window, text='Design', command=self.design, width=10)
        design_button.config(bg="BLUE")
        design_button.place(x=550,y=265)

        self.result_label=Label(self.window,text="RESULTS:")
        self.result_label.place(x=550,y=310)        


        self.opt_max_track=Label(self.window,text="Optimized track length")
        self.opt_max_track.place(x=550,y=325)

        self.opt_track_length=0 
        self.opt_track_box=Entry(self.window)
        self.opt_track_box.insert(0, self.opt_track_length)
        self.opt_track_box.place(x=550,y=350)

        self.opt_pop_label=Label(self.window,text="Optimized max population")
        self.opt_pop_label.place(x=550,y=375)

        self.opt_pop=0 
        self.opt_pop_box=Entry(self.window)
        self.opt_pop_box.insert(0, self.opt_pop)
        self.opt_pop_box.place(x=550,y=400)

        self.make_report_button=Button(self.window, text='Make report', command=self.make_report, width=10)
        self.make_report_button.config(bg="YELLOW")
        self.make_report_button.place(x=550,y=440)
 
    def make_report(self):
        """Calls make_pdf_report
        
        """
        self.map_image.save("temp_track_pic.jpg")
        ReportMaker().make_pdf_report(self.track,self.opt_pop,self.opt_track_length)

    def design(self):
        """Calls mapmaker,then optimizer, then image maker
        
        """
        startCityMenu=str(self.startCityMenu.get())
        endCityMenu=str(self.endCityMenu.get())
        try:
            max_track=int(self.max_track_box.get())
        except:
            max_track=10000

        created_map,c_on_map=MapMaker().make_map(startCityMenu,endCityMenu,self.communities.copy())

        created_map,c_on_map,self.opt_track_length,self.opt_pop,self.track=Optimizer().\
            optimizer(startCityMenu,endCityMenu,created_map,c_on_map,max_track)
        
        self.opt_track_box.delete(0,40)
        self.opt_track_box.insert(0, self.opt_track_length)
        
        self.opt_pop_box.delete(0,40)
        self.opt_pop_box.insert(0, self.opt_pop)
        print(self.track)
        self.window.title("Railroad Designer "+self.track)

        self.make_image(created_map)
    
    def make_image(self,created_map):
        """Makes image from numpy-array and renders it
        
        Args:
            created_map: A numpy array with cities and track
        """
        self.map_image=Image.fromarray(created_map,mode="RGB")
        self.img = ImageTk.PhotoImage(self.map_image)
        self.imglabel.configure(image=self.img)
        self.imglabel.image=self.img
         