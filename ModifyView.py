import tkinter as tk
from tkinter import messagebox

import pymysql


class modifyStudentFrame(tk.Frame):

    # inherit tkinter Frame
    def __init__(self, root):
        super().__init__(master=root)
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.gender = tk.StringVar()
        self.mobile = tk.StringVar()
        self.email = tk.StringVar()
        self.faculty = tk.StringVar()
        self.SWEN501 = tk.StringVar()
        self.SWEN502 = tk.StringVar()
        self.SWEN504 = tk.StringVar()
        self.SWEN589 = tk.StringVar()
        self.status = tk.StringVar()
        self.setup_modify_page()
        # self.search_by_id()
        # self.modify()
        self.status.set('')
        # self.id.set('')

    def setup_modify_page(self):
        # Create Label + Entry   --- student id
        tk.Label(self, text='ID:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.id).grid(row=0, column=1, padx=5, pady=5)
        # Create Label + Entry   --- student name
        tk.Label(self, text='Name:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.name).grid(row=1, column=1, padx=5, pady=5)
        # Create Label + Entry   --- gender
        tk.Label(self, text='Gender:', font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.gender).grid(row=2, column=1, padx=5, pady=5)
        # Create Label + Entry   --- mobile
        tk.Label(self, text='Mobile:', font=('Arial', 12)).grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.mobile).grid(row=3, column=1, padx=5, pady=5)
        # Create Label + Entry   --- email
        tk.Label(self, text='Email:', font=('Arial', 12)).grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.email).grid(row=4, column=1, padx=5, pady=5)
        # Create Label + Entry   --- faculty
        tk.Label(self, text='Faculty:', font=('Arial', 12)).grid(row=5, column=0, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.faculty).grid(row=5, column=1, padx=5, pady=5)
        # Create Label + Entry   --- SWEN501
        tk.Label(self, text='SWEN501:', font=('Arial', 12)).grid(row=1, column=2, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.SWEN501).grid(row=1, column=3, padx=5, pady=5)
        # Create Label + Entry   --- SWEN502
        tk.Label(self, text='SWEN502:', font=('Arial', 12)).grid(row=2, column=2, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.SWEN502).grid(row=2, column=3, padx=5, pady=5)
        # Create Label + Entry   --- SWEN504
        tk.Label(self, text='SWEN504:', font=('Arial', 12)).grid(row=3, column=2, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.SWEN504).grid(row=3, column=3, padx=5, pady=5)
        # Create Label + Entry   --- SWEN589
        tk.Label(self, text='SWEN589:', font=('Arial', 12)).grid(row=4, column=2, padx=5, pady=5)
        tk.Entry(self, width=20, textvariable=self.SWEN589).grid(row=4, column=3, padx=5, pady=5)

        tk.Button(self, text='Inquire', command=self.search_by_id).grid(row=6, column=1, padx=5, pady=5)
        tk.Button(self, text='Modify', command=self.modify).grid(row=6, column=2, padx=5, pady=5)
        tk.Button(self, text='Clear', command=self.clear_text_label).grid(row=6, column=3, padx=5, pady=5)
        # Create Label for status info
        tk.Label(self, textvariable=self.status).grid(row=7, column=1)

        tk.Label(self, text='1. Input Student ID to search student', font=('Arial', 12)).grid(row=10, column=0, padx=5,
                                                                                              pady=5)
        tk.Label(self, text='2. Input data to modify', font=('Arial', 12)).grid(row=11, column=0, padx=5, pady=5)
        tk.Label(self, text='3. Click the Modify Button', font=('Arial', 12)).grid(row=13, column=0, padx=5, pady=5)

    def search_by_id(self):

        students = self.fetch_all_students()
        id = self.id.get()
        if id:
            for student in students:
                if student[0] == int(id):
                    self.name.set(student[1])
                    self.gender.set(student[2])
                    self.mobile.set(student[3])
                    self.email.set(student[4])
                    self.faculty.set(student[5])
                    self.SWEN501.set(student[6])
                    self.SWEN502.set(student[7])
                    self.SWEN504.set(student[8])
                    self.SWEN589.set(student[9])
                    self.status.set(id + ' can be modified')
                    break
                else:
                    self.name.set('')
                    self.gender.set('')
                    self.mobile.set('')
                    self.email.set('')
                    self.faculty.set('')
                    self.SWEN501.set('')
                    self.SWEN502.set('')
                    self.SWEN504.set('')
                    self.SWEN589.set('')
                    self.status.set(str(id) + ' is Not exist')
        else:
            messagebox.showinfo("System Message", 'Must input ID!')

    def modify(self):

        id = self.id.get()
        if id == '':
            messagebox.showinfo("System Message", 'Must input ID!')
        else:
            db = pymysql.connect(host="localhost", user="root", password="", database="student_management_db")
            cursor = db.cursor()
            students = self.fetch_all_students()
            for student in students:
                if student[0] == int(id):
                    sql1 = 'update student set name=%s where id=%s'
                    sql2 = 'update student set gender=%s where id=%s'
                    sql3 = 'update student set mobile=%s where id=%s'
                    sql4 = 'update student set email=%s where id=%s'
                    sql5 = 'update student set faculty=%s where id=%s'
                    sql6 = 'update student set SWEN501=%s where id=%s'
                    sql7 = 'update student set SWEN502=%s where id=%s'
                    sql8 = 'update student set SWEN504=%s where id=%s'
                    sql9 = 'update student set SWEN589=%s where id=%s'
                    try:
                        cursor.execute(sql1, (self.name.get(), id))
                        cursor.execute(sql2, (self.gender.get(), id))
                        cursor.execute(sql3, (self.mobile.get(), id))
                        cursor.execute(sql4, (self.email.get(), id))
                        cursor.execute(sql5, (self.faculty.get(), id))
                        cursor.execute(sql6, (self.SWEN501.get(), id))
                        cursor.execute(sql7, (self.SWEN502.get(), id))
                        cursor.execute(sql8, (self.SWEN504.get(), id))
                        cursor.execute(sql9, (self.SWEN589.get(), id))
                        db.commit()
                        self.status.set(self.name.get() + ' has been modified Successfully')
                        messagebox.showinfo("System Message", self.name.get() + ' has been modified Successful')

                    except Exception as e:
                        print(e)
                        db.rollback()
                        print('Update student unsuccessfully')
                        self.status.set('Update student Unsuccessful')
                        break

    @staticmethod
    def fetch_all_students():
        db = pymysql.connect(host="localhost", user="root", password="", database="student_management_db")
        cursor = db.cursor()
        sql = 'select * from student'

        try:
            cursor.execute(sql)
            db.commit()
            students = cursor.fetchall()
            return students
        except Exception as e:
            print(e)
            print('Inquire Unsuccessfully')
        finally:
            db.close()

    def clear_text_label(self):
        self.status.set('')
        self.id.set('')
        self.name.set('')
        self.gender.set('')
        self.mobile.set('')
        self.email.set('')
        self.faculty.set('')
        self.SWEN501.set('')
        self.SWEN502.set('')
        self.SWEN504.set('')
        self.SWEN589.set('')
