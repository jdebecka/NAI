import string
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from Main.Main import *


class App(Frame):
    def __init__(self):
        super().__init__(master=None)
        self.main = Main()

        self.fr_test_data = Frame(window, borderwidth=5)
        self.fr_custom_vec = Frame(window, borderwidth=5)
        self.fr_option = Frame(window, borderwidth=5)
        self.fr_acc = Frame(window, borderwidth=5)
        self.fr_pred = Frame(window, borderwidth=5)
        self.fr_data = Frame(window, borderwidth=5)
        self.fr_test_file = Frame(window, borderwidth=5)
        self.fr_k = Frame(window, borderwidth=5)

        self.lbl_test = Label(self.fr_test_data, text="Data to test:")
        self.lbl_data = Label(self.fr_data, text="Data to learn:")
        self.lbl_custom_vex = Label(self.fr_custom_vec, text="Enter custom vec:")
        self.lbl_accuracy = Label(self.fr_acc, text="Accuracy: ")
        self.lbl_predicted = Label(self.fr_pred, text="Predicted: ")
        self.lbl_k = Label(self.fr_k, text="Enter K ")
        self.enter_vec = Entry(self.fr_custom_vec)
        self.enter_k = Entry(self.fr_k)

        self.lbl_data.pack(side=LEFT)
        self.lbl_k.pack(side=LEFT)
        self.lbl_test.pack(side=LEFT)
        self.lbl_custom_vex.pack(side=LEFT)
        self.lbl_accuracy.pack(side=LEFT)
        self.lbl_predicted.pack(side=LEFT)
        self.enter_vec.pack(side=LEFT)
        self.enter_k.pack(side=LEFT)

    def create_widget(self):
        btn_data = Button(self.fr_data, text="Choose", command=self.open_data_to_learn)
        btn_test = Button(self.fr_test_data, text="Choose", command=self.open_data_to_test)
        btn_custom_vec = Button(self.fr_custom_vec, text="Predict", command=self.test_custom_vec)
        btn_test_from_file = Button(self.fr_test_file, text="Test", command=self.test_from_file)

        btn_data.pack(side=RIGHT)
        btn_test.pack(side=RIGHT)
        btn_custom_vec.pack(side=RIGHT)
        btn_test_from_file.pack()

        self.fr_data.pack(side=TOP)
        self.fr_test_data.pack(side=TOP)
        self.fr_custom_vec.pack(side=TOP)
        self.fr_acc.pack(side=BOTTOM)
        self.fr_pred.pack(side=BOTTOM)
        self.fr_option.pack(side=BOTTOM)
        self.fr_test_file.pack()
        self.fr_k.pack()

        self.fr_test_data.place(relheight=.2, relwidth=1)
        self.fr_data.place(relheight=.2, relwidth=1, rely=.2)

        self.fr_test_file.place(relheight=.2, relwidth=.5, rely=.4)
        self.fr_k.place(relheight=.2, relwidth=.5, rely=.4, relx=.5)

        self.fr_custom_vec.place(relheight=.2, relwidth=1, rely=.6)
        self.fr_acc.place(relheight=.2, relwidth=.5, rely=.8)
        self.fr_pred.place(relheight=.2, relwidth=.5, rely=.8, relx=.5)


    def open_data_to_learn(self):
        filepath = askopenfilename(initialdir="/Users/juliadebecka/Documents/GitHub/NAI/KNN-Algo/Resources/",
                                   filetypes=[("Data", "*.data"), ("CSV", "*.csv")]
                                   )
        if not filepath:
            return
        self.lbl_data["text"] = f"Data to learn: {filepath}"
        self.main.data_file(filepath)

    def open_data_to_test(self):
        filepath = askopenfilename(initialdir="/Users/juliadebecka/Documents/GitHub/NAI/KNN-Algo/Resources/",
                                   filetypes=[("Data", "*.data"), ("CSV", "*.csv")]
                                   )
        if not filepath:
            return
        self.lbl_test["text"] = f"Data to test: {filepath}"
        self.main.test_file(filepath)

    def test_custom_vec(self):
        vec = self.enter_vec.get()
        k = self.enter_k.get()
        temp = vec.split(",")
        floatList: [float] = []
        for argument in temp:
            floatList.append(float(argument))
        predicted = self.main.test_custom(floatList, int(k))
        self.lbl_predicted["text"] = f"Predicted: {predicted}",
        self.lbl_accuracy["text"] = f"Accuracy: "

    def test_from_file(self):
        k = self.enter_k.get()
        acc = self.main.test(int(k))
        self.lbl_accuracy["text"] = f"Accuracy: {acc}"


window = Tk()
window.title("KNN")
window.minsize(800, 500)
app = App()
app.create_widget()
window.mainloop()
