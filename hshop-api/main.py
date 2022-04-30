from tkinter import *
from tkinter import filedialog


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


def main():
    root = Tk()

    folder_path = ""
    lbl1 = Label(root, folder_path)
    lbl1.grid(row=0, column=1)
    button2 = Button(text="Browse", command=browse_button)
    button2.grid(row=0, column=3)

    root.mainloop()


if __name__ == "__main__":
    main()
