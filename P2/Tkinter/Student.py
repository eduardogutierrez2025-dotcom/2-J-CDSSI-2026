class Student:
    def __init__(self, name, email, exam, note, grade, group, shift):
        self.name = name
        self.email = email
        self.exam = exam
        self.note = note
        self.grade = grade
        self.group = group
        self.shift = shift
import tkinter as tk

class EntryTest:

    def draw_entry(self):
        root = tk.Tk()
        root.title("Entry Demo")
        root.geometry("600x400")
        
        name_var = tk.StringVar()
        passw_var = tk.StringVar()

        # Label para mostrar resultados
        result_label = tk.Label(root, text="", font=('calibre', 10))
        result_label.grid(row=3, column=1)

        def submit():
            name = name_var.get()
            password = passw_var.get()
            
            # Mostrar en la ventana en lugar de consola
            result_label.config(text=f"Usuario: {name} | Password: {password}")
            
            name_var.set("")
            passw_var.set("")
        
        name_label = tk.Label(root, text='Username', font=('calibre',10,'bold'))
        name_entry = tk.Entry(root, textvariable=name_var, font=('calibre',10,'normal'))
        
        passw_label = tk.Label(root, text='Password', font=('calibre',10,'bold'))
        passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre',10,'normal'), show='*')
        
        sub_btn = tk.Button(root, text='Submit', command=submit)
        
        name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=1)
        passw_label.grid(row=1, column=0)
        passw_entry.grid(row=1, column=1)
        sub_btn.grid(row=2, column=1)

        root.mainloop()

test = EntryTest()
test.draw_entry()