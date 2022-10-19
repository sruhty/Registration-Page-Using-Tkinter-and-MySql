from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk
import sqlite3


class Res:
    def __init__(self, root):
        self.root = root
        self.root.title("Lambton registration page")
        self.root.geometry("1380x700")
        self.root.config(bg="white")
        self.bg = ImageTk.PhotoImage(file="images/lambtonclg.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
        self.left = ImageTk.PhotoImage(file="images/clg.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=780, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")

        # -------------Row1

        f_name = Label(frame1, text="First Name", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(
            x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 12), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(
            x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 12), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
        # -------------Row2
        contact = Label(frame1, text="Contact No.", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(
            x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 12), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="E-mail", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(
            x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 12), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # ---------------Row3
        question = Label(frame1, text="Security Question.", font=("times new roman", 12, "bold"), bg="white",
                         fg="gray").place(
            x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 10), state='readonly')
        self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)
        answer = Label(frame1, text="Answer", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(
            x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 12), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)
        # ----------------Row4
        password = Label(frame1, text="Password", font=("times new roman", 12, "bold"), bg="white", fg="gray").place(
            x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 12), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 12, "bold"), bg="white",
                          fg="gray").place(
            x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 12), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)
        # -----------Row5
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0,
                          bg="white", font=("times new roman", 12)).place(x=50, y=380)
        btn = Button(frame1, text="Register", bg="green", bd=0, cursor="hand2", command=self.register_data).place(x=50,
                                                                                                                  y=420)

        btn2 = Button(self.root, text="Sign in", bg="dark grey", font=("times new roman", 15), bd=0,
                      cursor="hand2").place(x=200, y=470, width=150)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All Feilds Are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password not matching", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree our terms & conditions", parent=self.root)
        else:
            try:
                db = sqlite3.connect('Lambton.db')
                cur = db.cursor()

                qry = 'insert into users (FirstName, LastName,Phone,Email,Question,Answer,password,cpassword)VALUES(?, ?, ?, ?,?,?,?,?)'
                val = [(self.txt_fname.get(), self.txt_lname.get(), self.txt_contact.get(), self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get(), self.txt_password.get(), self.txt_cpassword.get())]
                cur.executemany(qry,val)
                db.commit()
                db.close()
                messagebox.showinfo("Success", "Register Successful", parent=self.root)

            except EXCEPTION as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root)
                messagebox.showerror("Error", "not registered", parent=self.root)
                db.rollback()


root = Tk()
Res(root)
root.mainloop()
