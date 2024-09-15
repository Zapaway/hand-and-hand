import customtkinter as ctk


WINDOW_TITLE = "Your Dictionary 👋"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]

class VideoDisplayArea(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="white")
        
        self.button = ctk.CTkButton(self, text="Testing")

class SidebarSelector(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class DictionaryWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        self.title(WINDOW_TITLE)
        self.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.sidebar = SidebarSelector(self)
        self.sidebar.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        
        self.video_display = VideoDisplayArea(self)
        self.video_display.grid(row=0, column=1, columnspan=2,   sticky="nsew")
        
        self.focus()
        
        