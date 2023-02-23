from tkinter import *
from PIL import ImageTk, Image 

class LonginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        #================== background Image =================
        self.bg_frame = Image.open("images\\background1.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
      
        #================ login frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width='950', height=600)
        self.lgn_frame.place(x=200, y=70)

        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg="#040405", fg='white')
        self.heading.place(x=80, y=30, width=300, height=30)

        #================left side image=======================
      
        self.side_image = Image.open("images\\vector.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        #============ sign in image ===========================
        
        self.sign_in_image = Image.open("images\\hyy.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image = Label(self.lgn_frame, image=photo, bg="#040405")
        self.sign_in_image.image = photo
        self.sign_in_image.place(x=620, y=130)

        self.sign_in_label = Label(self.lgn_frame, text='Sign in', bg="#040405", fg="white", font=('yu gothic ui', 17, 'bold')) 
        self.sign_in_label.place(x=650, y=240)

        #================= Username ============================

        self.username_label = Label(self.lgn_frame, text='Username', bg='#040405', font=('yu gothic ui', 13,'bold'), fg='#4f4e4d')
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=550, y=359)

        #===================username icon ============================

        self.username_icon = Image.open("images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

      #================= Password ============================

        self.password_label = Label(self.lgn_frame, text='password', bg='#040405', font=('yu gothic ui', 13,'bold'), fg='#4f4e4d')
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.password_entry.place(x=580, y=416, width=270)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=440)

        #===================password icon ============================

        self.password_icon = Image.open("images\\password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        #=================== Login button =============================

        self.lgn_button = Image.open("images\\btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)

        self.login = Button(self.lgn_button_label, text='LOGIN', font=('yu gothic ui', 13, 'bold'), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        #============== forgot password =================================

        self.forgot_button = Button(self.lgn_frame, text='Forgot Password ?', font=('yu gothic ui', 13, 'bold underline'), fg='white', width=25, bd=0,
        bg='#040405', activebackground='#040405', cursor='hand2')
        self.forgot_button.place(x=580, y=510)

        #============== sign up =======================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=('yu gothic ui', 11, 'bold'), background='#040405', fg='white')

        self.sign_label.place(x=550, y=560)

        self.signup_button = Image.open("images\\register.png")
        photo = ImageTk.PhotoImage(self.signup_button )
        self.signup_button_label = Button(self.lgn_frame, image=photo, bg="#040405", activebackground='#040405', cursor='hand2', bd=0)
        self.signup_button_label.image = photo
        self.signup_button_label.place(x=670, y=555, width=111, height=35)


        #===================show/hide password ===========

        self.show_image = Image.open("images\\show.png")
        self.photo1 = ImageTk.PhotoImage(self.show_image )
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white', cursor='hand2', bd=0, command=self.show)
        
        self.show_button.image =self.photo1
        self.show_button.place(x=860, y=420)

        self.hide_image = Image.open("images\\hide.png")
        self.photo = ImageTk.PhotoImage(self.hide_image)
       
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.photo, bg='white', activebackground='white', cursor='hand2', bd=0, command=self.hide)

        self.hide_button.image =self.photo
        self.hide_button.place(x=860, y=420) 
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white', cursor='hand2', bd=0, command=self.show)
        
        self.show_button.image =self.photo1
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')



def page():
    window = Tk()
    LonginForm(window)
    window.mainloop()


if __name__ == '__main__':
    page()