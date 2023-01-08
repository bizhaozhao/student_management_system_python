import tkinter as tk
from tkinter import ttk
import pymysql

# from Database import database


class inquireStudentFrame(tk.Frame):
    # inherit tkinter Frame
    def __init__(self, root):
        super().__init__(master=root)

        self.tree_view = None
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.setup_inquire_page()
        # self.show_data_frame()

    def setup_inquire_page(self):
        columns = ("id", "name", "gender", "mobile", "email", "faculty", "SWEN501", "SWEN502", "SWEN504", "SWEN589")
        # columns_values = ("ID", "Name", "Gender", "Mobile", "Email", "Faculty", "SWEN501", "SWEN502", "SWEN504",
        # "SWEN589")

        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)

        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.column('name', width=120, anchor='center')
        self.tree_view.column('gender', width=80, anchor='center')
        self.tree_view.column('mobile', width=120, anchor='center')
        self.tree_view.column('email', width=140, anchor='center')
        self.tree_view.column('faculty', width=100, anchor='center')
        self.tree_view.column('SWEN501', width=80, anchor='center')
        self.tree_view.column('SWEN502', width=80, anchor='center')
        self.tree_view.column('SWEN504', width=80, anchor='center')
        self.tree_view.column('SWEN589', width=80, anchor='center')

        self.tree_view.heading('id', text='ID')
        self.tree_view.heading('name', text='Name')
        self.tree_view.heading('gender', text='Gender')
        self.tree_view.heading('mobile', text='Mobile')
        self.tree_view.heading('email', text='Email')
        self.tree_view.heading('faculty', text='Faculty')
        self.tree_view.heading('SWEN501', text='SWEN501')
        self.tree_view.heading('SWEN502', text='SWEN502')
        self.tree_view.heading('SWEN504', text='SWEN504')
        self.tree_view.heading('SWEN589', text='SWEN589')

        self.tree_view.pack(fill=tk.BOTH, expand=True)

        self.show_data_frame()

        tk.Button(self, text='Update', command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    def show_data_frame(self):

        # Delete the old data
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        students = self.fetch_all_students()
        index = 0
        for student in students:
            self.tree_view.insert('', index+1, values=(
                student[0], student[1], student[2], student[3], student[4],
                student[5], student[6], student[7], student[8], student[9],
            ))

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
