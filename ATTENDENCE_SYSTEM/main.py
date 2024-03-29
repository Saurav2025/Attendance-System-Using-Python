from calendar import c
from time import strftime
from tkinter import*
import tkinter
from time import strftime
from PIL import Image, ImageTk
from student import Student
from train import Train
from attendance import Attendance
import os
from face_recognition import Face_Recognition
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        # image1
        img = Image.open(r"Images\1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # image2
        img1 = Image.open(r"Images\3.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # image3
        img2 = Image.open(r"Images\2.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # backimg
        img3 = Image.open(r"Images\4.gif")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'),
                    background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # Student img Button
        img4 = Image.open(r"Images\5.webp")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, command=self.std_details,
                    image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, command=self.std_details, text="Student Details", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detetect Face img Button
        img5 = Image.open(r"Images\6.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendence img Button

        img6 = Image.open(r"Images\7.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    cursor="hand2", command=self.attendance_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendence", cursor="hand2", command=self.attendance_data,  font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help img Button
        img7 = Image.open(r"Images\8.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,
                    cursor="hand2", command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train img Button
        img8 = Image.open(r"Images\9.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, command=self.train_data,
                    image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, command=self.train_data, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        # Photo img Button
        img9 = Image.open(r"Images\9.webp")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        # Developer img Button
        img10 = Image.open(r"Images\10.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,
                    cursor="hand2", command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit img Button
        img11 = Image.open(r"Images\11.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,
                    cursor="hand2", command=self.IExit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.IExit, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def IExit(self):
        self.IExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.IExit > 0:
            self.root.destroy()
        else:
            return

        # *****************Function Button**************************

    def std_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
