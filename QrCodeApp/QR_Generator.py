import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
import qrcode


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode('light')
        super().__init__(fg_color="white")

        self.title("")
        self.geometry("400x400")
        self.iconbitmap(
            r"C:\Active Coding Projects\Python\Simple_Python_TKinter_Projects\QrCodeApp\Images\Logo\empty.ico")

        # Entry Field
        self.entry_string = ctk.StringVar()
        self.entry_string.trace('w', self.create_qr_code)
        EntryField(self, self.entry_string, self.save)

        self.bind("<Return>", self.save)

        # QR Codes
        self.raw_image = None
        self.tk_image = None
        self.qr_image = QRImageGenerator(self)

        self.mainloop()

    def create_qr_code(self, *args):
        current_text = self.entry_string.get()
        if current_text:
            self.raw_image = qrcode.make(current_text).resize((400, 400))
            self.tk_image = ImageTk.PhotoImage(self.raw_image)
            self.qr_image.update_image(self.tk_image)
        else:
            self.qr_image.clear()
            self.raw_image = None
            self.tk_image = None

    def save(self, event=""):
        if self.raw_image:
            file_path = filedialog.asksaveasfilename()
            if file_path:
                self.raw_image.save(file_path + ".jpg")


class QRImageGenerator(tk.Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, background="white", bd=0, highlightthickness=0, relief="ridge")
        self.place(relx=0.5, rely=0.4, width=400, height=400, anchor="center")

    def update_image(self, image_tk):
        self.clear()
        self.create_image(0, 0, image=image_tk, anchor="nw")

    def clear(self):
        self.delete("all")


class EntryField(ctk.CTkFrame):
    def __init__(self, parent, entry_string, save_func):
        super().__init__(master=parent, corner_radius=20, fg_color="#4B0082")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure((0, 1), weight=1, uniform="a")

        self.Frame = ctk.CTkFrame(self, fg_color="transparent")
        self.Frame.columnconfigure(0, weight=1, uniform="b")
        self.Frame.columnconfigure(1, weight=4, uniform="b")
        self.Frame.columnconfigure(2, weight=2, uniform="b")
        self.Frame.columnconfigure(3, weight=1, uniform="b")
        self.Frame.grid(row=0, column=0)

        entry = ctk.CTkEntry(self.Frame, textvariable=entry_string, fg_color="#380062", border_width=0,
                             text_color="#FFFFFF")
        entry.grid(row=0, column=1, sticky="nsew")

        save_button = ctk.CTkButton(self.Frame, text="Save", fg_color="#380062", hover_color="#260041",
                                    command=save_func)
        save_button.grid(row=0, column=2, sticky="nsew", padx=10)


App()
