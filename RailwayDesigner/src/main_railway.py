import tkinter as tk
from PIL import ImageTk,Image 
from location_loader import LocLoader
from map_maker import MapMaker



def main():
    
    communities=LocLoader().location_loader()
    map_image,com_in_map=MapMaker().make_map("Helsinki","Tampere",communities)
    
    window = tk.Tk()
    window.title("Railroad Designer")
    window.geometry("800x600")
    
    #img = ImageTk.PhotoImage(Image.open(f"./src/kartta.jpg"))
    img = ImageTk.PhotoImage(map_image)
    imglabel = tk.Label(window, image=img).grid(row=1, column=1)
    window.mainloop()
    print("Train is coming!")




if __name__ == '__main__':
    main()


