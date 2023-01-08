import tkinter as tk

import pymysql
#
#
# class addStudentFrame(tk.Frame):
#     # inherit tkinter Frame
#     def __init__(self, root):
#         super().__init__(master=root)
#
#         self.name = tk.StringVar()
#         self.gender = tk.StringVar()
#         self.mobile = tk.StringVar()
#         self.email = tk.StringVar()
#         self.faculty = tk.StringVar()
#         self.SWEN501 = tk.StringVar()
#         self.SWEN502 = tk.StringVar()
#         self.SWEN504 = tk.StringVar()
#         self.SWEN589 = tk.StringVar()
#         self.status = tk.StringVar()
#         # self["bg"] = "cornflowerblue"
#         self.setup_add_page()
#
#     def setup_add_page(self):
#         # Create Label + Entry   --- student name
#         tk.Label(self, text='Name:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.name).grid(row=1, column=1, padx=5, pady=5)
#         # Create Label + Entry   --- gender
#         tk.Label(self, text='Gender:', font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.gender).grid(row=2, column=1, padx=5, pady=5)
#         # Create Label + Entry   --- mobile
#         tk.Label(self, text='Mobile:', font=('Arial', 12)).grid(row=3, column=0, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.mobile).grid(row=3, column=1, padx=5, pady=5)
#         # Create Label + Entry   --- email
#         tk.Label(self, text='Email:', font=('Arial', 12)).grid(row=4, column=0, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.email).grid(row=4, column=1, padx=5, pady=5)
#         # Create Label + Entry   --- faculty
#         tk.Label(self, text='Faculty:', font=('Arial', 12)).grid(row=5, column=0, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.faculty).grid(row=5, column=1, padx=5, pady=5)
#         # Create Label + Entry   --- SWEN501
#         tk.Label(self, text='SWEN501:', font=('Arial', 12)).grid(row=1, column=2, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.SWEN501).grid(row=1, column=3, padx=5, pady=5)
#         # Create Label + Entry   --- SWEN502
#         tk.Label(self, text='SWEN502:', font=('Arial', 12)).grid(row=2, column=2, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.SWEN502).grid(row=2, column=3, padx=5, pady=5)
#         # Create Label + Entry   --- SWEN504
#         tk.Label(self, text='SWEN504:', font=('Arial', 12)).grid(row=3, column=2, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.SWEN504).grid(row=3, column=3, padx=5, pady=5)
#         # Create Label + Entry   --- SWEN589
#         tk.Label(self, text='SWEN589:', font=('Arial', 12)).grid(row=4, column=2, padx=5, pady=5)
#         tk.Entry(self, width=20, textvariable=self.SWEN589).grid(row=4, column=3, padx=5, pady=5)
#
#         tk.Button(self, text='Add Student', command=self.add).grid(row=5, column=3, padx=5, pady=5)
#         # Create Label for status info
#         tk.Label(self, textvariable=self.status).grid(row=6, column=1)
#
#     def add(self):
#
#         db = pymysql.connect(host="localhost", user="root", password="", database="student_management_db")
#         cursor = db.cursor()
#         sql = 'insert into student(name,gender,mobile,email,faculty,SWEN501,SWEN502,SWEN504,SWEN589) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#         try:
#             cursor.execute(sql,
#                            (self.name.get(), self.gender.get(), self.mobile.get(), self.email.get(), self.faculty.get(),
#                             self.SWEN501.get(), self.SWEN502.get(), self.SWEN504.get(), self.SWEN589.get()))
#             db.commit()
#             print('Add student successfully')
#             self.status.set('Successful')
#
#         except Exception as e:
#             print(e)
#             db.rollback()
#             print('Add student unsuccessfully')
#             self.status.set('Unsuccessful')
#         # stu = {
#         #     "name": self.name.get(),
#         #     "gender": self.gender.get(),
#         #     "mobile": self.mobile.get(),
#         #     "email": self.email.get(),
#         #     "faculty": self.faculty.get(),
#         #     "SWEN501": self.SWEN501.get(),
#         #     "SWEN502": self.SWEN502.get(),
#         #     "SWEN504": self.SWEN504.get(),
#         #     "SWEN589": self.SWEN589.get()
#         # }


# class inquireStudentFrame(tk.Frame):
#     # inherit tkinter Frame
#     def __init__(self, root):
#         super().__init__(master=root)
#
#         self.table_view = tk.Frame()
#         self.table_view.pack()
#
#     def setup_inquire_page(self):
#         pass



# class deleteStudentFrame(tk.Frame):
#     # inherit tkinter Frame
#     def __init__(self, root):
#         super().__init__(master=root)
#
#         tk.Label(self, text='delete student').pack()
#         tk.Label(self, text='delete student').pack()
#         tk.Label(self, text='delete student').pack()
#         tk.Label(self, text='delete student').pack()


# class modifyStudentFrame(tk.Frame):
#     # inherit tkinter Frame
#     def __init__(self, root):
#         super().__init__(master=root)
#
#         tk.Label(self, text='modify student').pack()
#         tk.Label(self, text='modify student').pack()
#         tk.Label(self, text='modify student').pack()
#         tk.Label(self, text='modify student').pack()
