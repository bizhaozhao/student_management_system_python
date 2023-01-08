import tkinter as tk
from tkinter import LEFT, messagebox
import pymysql
from MainUI import MainWindow


# Reference1: https://www.bilibili.com/video/BV1r44y1Y7yQ/?spm_id_from=333.337.search-card.all.click&vd_source
# =71f74c573b25c9f452198b570f2d171b
# Reference2: https://blog.csdn.net/weixin_43580438/article/details/121378621


class LoginWindow:
    # Initialize
    def __init__(self, master):
        self.root = master
        self.root.geometry('1000x450')
        self.root.title('Student Management System v1.0')
        self.root.resizable(0, 0)

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        self.Login_image = tk.PhotoImage(file='vuw.gif')
        self.label_img = tk.Label(self.login_frame, image=self.Login_image)
        self.label_img.pack()

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.setup_login_window()

    def setup_login_window(self):

        # Create Label + Entry   --- admin
        Label_user = tk.Label(self.login_frame, text="Administrator:", font=('Arial', 14))
        Label_user.pack(side=LEFT, padx=10, pady=10)
        Entry_user = tk.Entry(self.login_frame, textvariable=self.username, width=12, font=('Arial', 14))
        Entry_user.pack(side=LEFT, padx=10, pady=10)
        # Create Label + Entry   --- password
        Label_password = tk.Label(self.login_frame, text="Password:", font=('Arial', 14))
        Label_password.pack(side=LEFT, padx=10, pady=10)
        Entry_password = tk.Entry(self.login_frame, textvariable=self.password, width=12, show="*", font=('Arial', 14))
        Entry_password.pack(side=LEFT, padx=10, pady=10)
        # Create button  --- login
        Button_login = tk.Button(self.login_frame, text="LogIn", width=16, command=self.check_login_password)
        Button_login.pack(side=LEFT, padx=20, pady=10)
        # Create button  --- logout
        Button_logout = tk.Button(self.login_frame, text="LogOut", width=16, command=self.login_frame.quit)
        Button_logout.pack(side=LEFT, padx=30, pady=10)

    # check username and password are valid or not
    def check_login_password(self):

        db = pymysql.connect(host="localhost", user="root", password="", database="student_management_db")
        cursor = db.cursor()
        sql = "select * from manage where user_name=%s"
        cursor.execute(sql, self.username.get())
        # save admin data into user_list
        self.login_frame.user_list = cursor.fetchall()
        print(self.login_frame.user_list)
        cursor.close()
        db.close()
        if len(self.login_frame.user_list) != 0:
            if self.password.get() != str(self.login_frame.user_list[0][1].strip().lower()):
                messagebox.showinfo("System Message", "Invalid Password!")
            else:
                messagebox.showinfo("System Message", "Login successfully！")
                self.login_frame.user = self.login_frame.user_list[0][0]
                self.login_frame.destroy()
                MainWindow(self.root)
        else:
            messagebox.showinfo("System Message", 'User name is not exist!')


if __name__ == '__main__':
    root = tk.Tk()
    login_window = LoginWindow(master=root)
    root.mainloop()
