import os
from tkinter import Tk, filedialog

def folder_to_txt(input_dir):
    file_list = os.listdir(input_dir)

    folder_name = os.path.basename(os.path.normpath(input_dir))
    save_path = os.path.join(input_dir, f"{folder_name}_file_list.txt")

    with open(save_path, "w", encoding="utf-8") as f:
        for name in file_list:
            f.write(os.path.join(input_dir, name) + "\n")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    input_dir = filedialog.askdirectory(parent=root)

    root.destroy()

    if input_dir:
        folder_to_txt(input_dir)
