from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.ttk import *
from Contoller.Main import Main
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
from tkinter.scrolledtext import Scrollbar



class App(Frame):
    def __init__(self):
        super().__init__(master=None)
        self.choices = []
        self.main = Main()
        self.data_filepath = ""
        self.test_filepath = ""

        self.fr_test_data = Frame(window, borderwidth=5)
        self.fr_canvas = Frame(window, borderwidth=5)
        self.fr_custom_vec = Frame(window, borderwidth=5)
        self.fr_option = Frame(window, borderwidth=5)
        self.fr_acc = Frame(window, borderwidth=5)
        self.fr_iteration = Frame(window, borderwidth=5)
        self.fr_data = Frame(window, borderwidth=5)
        self.fr_learning_r = Frame(window, borderwidth=5)

        self.lbl_test = Label(self.fr_test_data, text="Data to test (optional):")
        self.lbl_data = Label(self.fr_data, text="Data to learn (optional):")
        self.lbl_custom_vex = Label(self.fr_custom_vec, text="Enter custom vec:")
        self.lbl_custom_name = Label(self.fr_custom_vec, text="Enter name for custom vec:")
        self.lbl_accuracy = Label(self.fr_acc, text="Accuracy: ")
        self.lbl_accuracy.config(font=("Courier", 35))
        self.lbl_learning_r = Label(self.fr_learning_r, text="Enter learning rate [0-1]: ")
        self.lbl_iterations = Label(self.fr_iteration, text="Enter iteration count: ")
        self.enter_vec = Text(self.fr_custom_vec)
        # self.enter_vec = Scrollbar(self.fr_custom_vec)
        # self.enter_vec.config(command=self.txt.yview)
        # self.txt.config(yscrollcommand=self.enter_vec.set)
        self.enter_learning_r = Entry(self.fr_learning_r)
        self.enter_lbl_iterations = Entry(self.fr_iteration)
        self.option = StringVar(window)
        self.option.set('none')
        imageToShow = Image.open("/Users/juliadebecka/Documents/GitHub/NAI/Perceptron/Resources/plot.png")
        tw = 0.5
        out = imageToShow.resize([int(tw * s) for s in imageToShow.size], Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(out)
        self.image_view = Label(self.fr_canvas, image=self.photo, anchor=CENTER)
        self.image_view.image = self.photo

        self.image_view.pack(side=TOP, fill=BOTH, expand="yes")
        self.popup_menu_name = OptionMenu(self.fr_custom_vec, self.option, *self.choices)
        self.lbl_data.pack(side=LEFT)
        self.lbl_learning_r.pack(side=LEFT)
        self.lbl_test.pack(side=LEFT)
        self.lbl_custom_name.pack(side=LEFT)
        self.popup_menu_name.pack(side=LEFT)
        self.lbl_custom_vex.pack(side=LEFT)
        self.lbl_accuracy.pack(side=TOP, fill=BOTH, expand="yes")
        self.enter_vec.pack(side=LEFT, fill=BOTH, expand="yes")
        self.enter_learning_r.pack(side=LEFT)
        self.popup_menu_name.config(state=DISABLED)
        self.lbl_iterations.pack(side=LEFT)
        self.enter_lbl_iterations.pack(side=LEFT)

    def create_widget(self):
        btn_data = Button(self.fr_data, text="Choose", command=self.open_data_to_learn)
        btn_test = Button(self.fr_test_data, text="Choose", command=self.open_data_to_test)
        btn_custom_vec = Button(self.fr_custom_vec, text="Test custom", command=self.test_custom_vec)
        btn_test_from_file = Button(self.fr_test_data, text="Test", command=self.test_from_file)
        btn_train = Button(self.fr_data, text="Train", command=self.train_algo)

        btn_train.pack(side=RIGHT)
        btn_data.pack(side=RIGHT)
        btn_test_from_file.pack(side=RIGHT)
        btn_test.pack(side=RIGHT)
        btn_custom_vec.pack(side=RIGHT)

        self.fr_data.pack(side=TOP)
        self.fr_canvas.pack(side=TOP)
        self.fr_test_data.pack(side=TOP)
        self.fr_custom_vec.pack(side=TOP)
        self.fr_acc.pack(side=BOTTOM)
        self.fr_iteration.pack(side=BOTTOM)
        self.fr_option.pack(side=BOTTOM)
        self.fr_learning_r.pack()

        self.fr_data.place(relheight=.1, relwidth=1)
        self.fr_canvas.place(relheight=.5, relwidth=1, rely=.1)
        self.fr_test_data.place(relheight=.1, relwidth=1, rely=.6)
        self.fr_iteration.place(relheight=.1, relwidth=.5, rely=.7)
        self.fr_learning_r.place(relheight=.1, relwidth=.5, rely=.7, relx=.5)
        self.fr_custom_vec.place(relheight=.1, relwidth=1, rely=.8)
        self.fr_acc.place(relheight=.1, relwidth=1, rely=.9)

    def train_algo(self):
        learning_r = self.enter_learning_r.get()
        iterations = self.enter_lbl_iterations.get()
        if learning_r == '':
            if iterations == '':
                choices_set = self.main.train(self.data_filepath)
            else:
                choices_set = self.main.train(self.data_filepath, iteration_count=int(iterations))
        else:
            if iterations == '':
                choices_set = self.main.train(self.data_filepath, learning_rate=float(learning_r))
            else:
                choices_set = self.main.train(self.data_filepath, int(iterations), float(learning_r))
        self.set_img()

        if len(self.choices) == 0:
            self.append_choices(choices_set)
            self.popup_menu_name.set_menu(None, *self.choices)
            self.popup_menu_name.config(state=ACTIVE)

    def append_choices(self, choices_set):
        for choice in choices_set:
            self.choices.append(choice)

    def set_img(self):
        img = Image.open(
            "/Users/juliadebecka/Documents/GitHub/NAI/Language_Classifier/Single_Layer_Network/Resources/Plots"
            "/errors_iter.png")
        tw = 0.5
        out = img.resize([int(tw * s) for s in img.size], Image.ANTIALIAS)
        imgShow = ImageTk.PhotoImage(out)
        self.photo = imgShow
        self.image_view.image = self.photo
        self.image_view["image"] = self.photo

    def open_data_to_learn(self):
        filepath = askdirectory(
            initialdir="/Users/juliadebecka/Documents/GitHub/NAI/Language_Classifier/Single_Layer_Network/Resources"
            )
        if not filepath:
            return
        self.data_filepath = filepath
        self.lbl_data["text"] = f"Data to learn: {filepath}"

    def open_data_to_test(self):
        filepath = askdirectory(
            initialdir="/Users/juliadebecka/Documents/GitHub/NAI/Language_Classifier/Single_Layer_Network/Resources"
            )
        if not filepath:
            return
        self.test_filepath = filepath
        self.lbl_test["text"] = f"Data to test: {filepath}"

    def test_custom_vec(self):
        if len(self.choices) < 2:
            self.train_algo()

        text = self.enter_vec.get("1.0", END)

        prediction = self.main.custom_text(text, "Custom")
        self.lbl_accuracy["text"] = f"Predicted: {prediction}"

    def test_from_file(self):
        if len(self.choices) < 1:
            self.train_algo()
        acc = self.main.test(self.test_filepath)
        self.lbl_accuracy["text"] = f"Accuracy: {acc}%"


window = Tk()
window.title("Single layer network")
window.minsize(800, 500)
app = App()
app.create_widget()
window.bind("<Return>", )
window.mainloop()
