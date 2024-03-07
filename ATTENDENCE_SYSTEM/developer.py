from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        title_lb1 = Label(self.root, text="Developer", font=(
            "times new roman", 35, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # firstimage
        img_top = Image.open(r"D:\DIP\Attendence_System\Images\16.webp")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=1530, height=720)

        # frame
        main_frame = Frame(f_lb1, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1 = Image.open(r"C:\Users\saura\Downloads\SauravPoojari.jpg")
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lb1 = Label(main_frame, image=self.photoimg_top1)
        f_lb1.place(x=300, y=0, width=200, height=200)

        # Developer Info
        dev_label = Label(main_frame, text="Helow My name is MCA", font=(
            "times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0, y=5)

        dev_label = Label(main_frame, text="I am Full stack developer", font=(
            "times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0, y=40)

        img_left = Image.open(r"D:\DIP\Attendence_System\Images\16.webp")
        img_left = img_left.resize((500, 390), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(main_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=210, width=500, height=390)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
