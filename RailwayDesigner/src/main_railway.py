from tkinter import Tk
from user_interface import UI

def main():

    window = Tk()
    window.title("Railroad Designer")
    window.geometry("768x512")

    UI(window)
    window.mainloop()
    print("Train is coming!")

if __name__ == '__main__':
    main()
