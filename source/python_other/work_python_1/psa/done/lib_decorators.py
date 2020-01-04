import Tkinter as tk
import tkMessageBox


def add_warning_window(text0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            def exit_application():
                MsgBox = tkMessageBox.askquestion('', 'Are you sure ?', icon='warning')
                if MsgBox == 'yes':
                    func(*args, **kwargs)
                    root.destroy()
                else:
                    pass

            root = tk.Tk()  # create window
            canvas1 = tk.Canvas(root, width=300, height=300)
            canvas1.pack()
            button1 = tk.Button(root, text=text0, command=exit_application)
            canvas1.create_window(150, 150, window=button1)
            root.mainloop()
        return wrapper
    return decorator


@add_warning_window('You want to destroy some files')
def some_method():
    print("elo")


some_method()