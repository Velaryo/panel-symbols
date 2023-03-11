import tkinter as tk
import pyperclip

class ClipboardApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Clipboard App")
        self.master.geometry("200x100")
        self.create_widgets()

    def create_widgets(self):
        #1ra fila
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=5)

        self.button1 = tk.Button(self.button_frame, text="<", command=lambda: self.copy_to_clipboard("<"))
        self.button1.pack(side="left", padx=5)
        
        self.button2 = tk.Button(self.button_frame, text=">", command=lambda: self.copy_to_clipboard(">"))
        self.button2.pack(side="left", padx=5)

        self.button3 = tk.Button(self.button_frame, text="<>", command=lambda: self.copy_to_clipboard("<>"))
        self.button3.pack(side="left", padx=5)
        
        self.button4 = tk.Button(self.button_frame, text="`", command=lambda: self.copy_to_clipboard("`"))
        self.button4.pack(side="left", padx=5)
        
        #2da fila
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=5)

        self.button5 = tk.Button(self.button_frame, text="```", command=lambda: self.copy_to_clipboard("```"))
        self.button5.pack(side="left", padx=5)

        self.button6 = tk.Button(self.button_frame, text="=>", command=lambda: self.copy_to_clipboard("=>"))
        self.button6.pack(side="left", padx=5)

        self.button7 = tk.Button(self.button_frame, text="\\", command=lambda: self.copy_to_clipboard("\\"))
        self.button7.pack(side="left", padx=5)

        
        """ self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack() """

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)

root = tk.Tk()
app = ClipboardApp(master=root)
app.mainloop()
