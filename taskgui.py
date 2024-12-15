import tkinter as tk
import pyttsx3

# محرك عشان احول النص لصوت
engine = pyttsx3.init()

# لانشاء الواجهة ل gui
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x400")
root.configure(bg="white")  

def play_text():
    text = text_box.get("1.0", "end-1c")  # عشان اجيب النص من مكانه
    if text:
        engine.say(text)
        engine.runAndWait()

def sit_text():
    text_box.delete("1.0", "end")

def exit_program():
    root.quit()

label = tk.Label(root,text="Enter your text:",font=("Arial", 16, "bold"),
                 bg="white",fg="black")
label.pack(pady=10)

text_box = tk.Text(root,height=6,width=40,font=("Arial", 12), bg="white",  
                   fg="black",relief="solid",)
text_box.pack(pady=10)

# ألوان الbutton
button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "black",  
    "fg": "white",
    "activebackground": "blue",  
    "activeforeground": "white", 
    "width": 10,
    "relief": "raised",
}

# buttonsعشان اضيف ال
button_play = tk.Button(root, text="Play", command=play_text, **button_style)
button_play.pack(side="left", padx=10, pady=20)

button_sit = tk.Button(root, text="Sit", command=sit_text, **button_style)
button_sit.pack(side="left", padx=10, pady=20)

button_exit = tk.Button(root, text="Exist", command=exit_program, **button_style)
button_exit.pack(side="left", padx=10, pady=20) 

root.mainloop()