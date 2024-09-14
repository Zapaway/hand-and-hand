import customtkinter as ctk
from PIL import ImageTk, Image
import cv2


WINDOW_TITLE = "Hand and Hand 👋"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400


class VideoFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
                
        self.cap = cv2.VideoCapture(0)
    
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

        self.video_frame = VideoFrame(self)
        self.video_frame.place(x=0, y=0, anchor="nw")



if __name__ == "__main__":
    app = App()
    app.video_frame.stream()
    app.mainloop()
    
