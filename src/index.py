from tkinter import Tk
from UI.user_interface import UI

def main():

    window = Tk()
    UI(window)
    window.mainloop()
    print("Train is coming!")

if __name__ == '__main__':
    main()
