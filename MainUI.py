import tkinter as tk
from AddView import addStudentFrame
from InquireView import inquireStudentFrame
from DeleteView import deleteStudentFrame
from ModifyView import modifyStudentFrame


class MainWindow:

    def __init__(self, master):
        self.root = master
        self.root.geometry('1000x450')
        self.root.title('Student Management System v1.0')
        self.root.resizable(0, 0)

        self.setup_main_window()

        # Add student view
        self.add_Frame = addStudentFrame(self.root)
        # Inquire student view
        self.inquire_frame = inquireStudentFrame(self.root)
        # Delete student view
        self.delete_frame = deleteStudentFrame(self.root)
        # Modify student view
        self.modify_frame = modifyStudentFrame(self.root)

    def setup_main_window(self):
        menu_bar = tk.Menu(self.root)

        menu_bar.add_command(label='Add', command=self.show_add_frame)
        menu_bar.add_command(label='Inquire', command=self.show_inquire_frame)
        menu_bar.add_command(label='Delete', command=self.show_delete_frame)
        menu_bar.add_command(label='Modify', command=self.show_modify_frame)

        self.root['menu'] = menu_bar

    def show_add_frame(self):
        self.add_Frame.pack()
        self.inquire_frame.forget()
        self.delete_frame.forget()
        self.modify_frame.forget()

    def show_inquire_frame(self):
        self.add_Frame.forget()
        self.inquire_frame.pack()
        self.delete_frame.forget()
        self.modify_frame.forget()

    def show_delete_frame(self):
        self.add_Frame.forget()
        self.inquire_frame.forget()
        self.delete_frame.pack()
        self.modify_frame.forget()

    def show_modify_frame(self):
        self.add_Frame.forget()
        self.inquire_frame.forget()
        self.delete_frame.forget()
        self.modify_frame.pack()


if __name__ == '__main__':
    root = tk.Tk()
    # MainWindow(master=root)
    # root.mainloop()
