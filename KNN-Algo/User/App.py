import tkinter as tk
from tkinter.filedialog import askopenfilename


class App(tk.Frame):

    def create_widgets(self):
        fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
        fr_labels = tk.Frame(window, bd=2)

        lbl_test = tk.Label(fr_labels, text="Data to test")
        lbl_data = tk.Label(fr_labels, text="Data to learn:")

        btn_data = tk.Button(fr_buttons, text="Choose", command=self.open_file)
        btn_data.grid(row=0, sticky="ew")
        lbl_data.grid(row=0, sticky="ew")

        btn_test = tk.Button(fr_buttons, text="Choose")
        lbl_test.grid(row=1, sticky="ew")
        btn_test.grid(row=1, sticky="ew")

        fr_buttons.grid(column=1, sticky="ns")
        fr_labels.grid(column=0, sticky="ns")

    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("Data", "*.data"), ("CSV", "*.csv")]
        )
        if not filepath:
            return
        window.title(f"Simple Text Editor - {filepath}")


window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
app = App(window)
app.create_widgets()
window.mainloop()

