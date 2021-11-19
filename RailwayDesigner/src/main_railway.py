import tkinter as tk
from PIL import ImageTk,Image 


class MapLoader():
    def __init__(self):
        self.load_successful=False

    def map_loader(self,map_to_load="defaultmap.jpg"):
        try:
            self.load_successful=True
        except:
            pass
def main():
    window = tk.Tk()
    window.title("Railroad Designer")
    window.geometry("800x400")
    
    img = ImageTk.PhotoImage(Image.open(f"kartta.jpg"))
    imglabel = tk.Label(window, image=img).grid(row=1, column=1)
    window.mainloop()
    print("Train is coming!")




if __name__ == '__main__':
    main()


