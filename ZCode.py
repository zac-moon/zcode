import tkinter as tk
import sys

root = tk.Tk()
root.title("ZCODE EDITOR")

def runCode(code):
    outputWin = tk.Toplevel()
    outputWin.title("ZCODE OUTPUT")

    print("Ran Code")
    try:
        exec(code)
    except Exception as e:
        print("An error occurred:", e)

    outputWin.mainloop()

def enter():
    runCode("hi")


codeBox = tk.Text(root, height=4, width=40)  # Create a Text widget
codeBox.pack(fill=tk.BOTH, expand=True)

runBtn = tk.Button(root, text="Run Code",width="100",command=enter)  
runBtn.pack()


root.mainloop()