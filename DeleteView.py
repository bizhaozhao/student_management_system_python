import tkinter as tk
from tkinter import messagebox

import pymysql


class deleteStudentFrame(tk.Frame):
    # inherit tkinter Frame
    def __init__(self, root):
        super().__init__(master=root)
        self.id = tk.IntVar()
        self.status = tk.StringVar()
        self.setup_delete_page()

    def setup_delete_page(self):
        tk.Label(self, text='Input Student ID to delete!', font=('Arial', 12)).pack()
        tk.Entry(self, textvariable=self.id).pack()
        tk.Button(self, text='Delete', command=self.delete_by_id).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete_by_id(self):
        id = self.id.get()
        db = pymysql.connect(host="localhost", user="root", password="", database="student_management_db")
        cursor = db.cursor()

        sql1 = 'select * from student'
        sql2 = 'delete from student where id=%s'

        try:
            cursor.execute(sql1)
            db.commit()
            students = cursor.fetchall()
            for student in students:
                if student[0] == id:
                    cursor.execute(sql2, str(id))
                    db.commit()
                    self.status.set('ID ' + str(id) + ' was deleted successfully!')
                    # messagebox.showinfo("System Message", 'Deleted successfully!')
                else:
                    self.status.set('ID ' + str(id) + ' is not exist!')
                    # messagebox.showinfo("System Message", 'This ID is not exist!')
                    # break
        except Exception as e:
            print(e)
            print('Inquire Unsuccessfully')
            messagebox.showinfo("System Message", 'Inquire Unsuccessfully!')
        finally:
            db.close()
