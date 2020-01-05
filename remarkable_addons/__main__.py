# Load external packages
import sys
import os
from pathlib import Path
import tkinter
from tkinter import filedialog

# Load custom packages
from remarkable_addons.classes.svg_edit import svg_edit
from remarkable_addons.classes.measure_time import measure_time
from remarkable_addons.classes.utils import utils

def main(args=None):
    # The main routine
    if args is None:
        args = sys.argv[1:]
        print("You need to specify the path where your SVG files are located...")
        print("Exiting the program now...")
        # sys.exit()

    # Process arguments

    # Configuration defaults (Change according to your needs)
    stroke_color = "#FF0000" # default red
    outputs_path = "temp"
    output_pdf_name = "final_result.pdf"
    quality = 5 # 5 is the default value

    # Ask for inputs path
    root = tkinter.Tk()
    inputs_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    print("Opening folder: " + str(inputs_path))
    
    # Initialize classes
    timer = measure_time()     # Create timer object to measure elapsed time
    update_inputs = svg_edit(stroke_color, outputs_path, quality)
    funcs = utils()

    # Main process
    timer.start()
    print("Editing Remarkable output started!")

    pathlist = Path(inputs_path).glob('**/*.svg')
    num_of_pages = 0
    for path in pathlist:
        index = funcs.get_index(str(path), " ", ".")
        if index.isdigit():
            num_of_pages = num_of_pages + 1
            update_inputs.edit_and_save(str(path), index)
        else:
            print("-- Warning: " + index + " is not valid index")

    print(str(num_of_pages) + " PDFs generated, now compiling final PDF")
    paths = Path(outputs_path).glob('**/*.pdf')
    funcs.pdf_cat(output_pdf_name, funcs.sort_paths(paths, num_of_pages))
    timer.end(num_of_pages)
    update_inputs.calc_compression()
    print("Done!")
    print("Exiting program now!")
    sys.exit()

if __name__ == "__main__":
    main()
