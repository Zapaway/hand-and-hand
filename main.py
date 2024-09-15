import customtkinter as ctk
from dictionary_window import DictionaryWindow
from PIL import ImageTk, Image
import cv2


WINDOW_TITLE = "Hand and Hand 👋"
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480


class VideoFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
                
        self.cap = cv2.VideoCapture(1)
    
    def stream(self):
        # function for video streaming
        _, frame = self.cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.imgtk = imgtk
        self.master.configure(image=imgtk)
        self.after(1, self.stream) 


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.video_frame = VideoFrame(self)
        self.video_frame.grid(row=0, column=0)
        self.button = ctk.CTkButton(self, text="my button", command=self.open_dictionary_window)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def open_dictionary_window(self):
        self.dictionary_window = DictionaryWindow()


if __name__ == "__main__":
    app = App()
    app.video_frame.stream()
    app.mainloop()
    
