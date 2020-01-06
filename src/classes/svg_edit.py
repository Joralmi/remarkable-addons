# Load external packages
import os
from PIL import Image
import img2pdf
from xml.dom import minidom
from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg

# Custom packages
from src.classes.utils import utils

class svg_edit:
    def __init__(self, color, temp_path, quality=5):
        fun = utils()
        self.color = color
        self.temp_path = temp_path + fun.check_platform()
        self.original_size = 0
        self.final_size = 0
        self.quality = quality # 0 to 100
    
    def edit_and_save(self, file, index):    
        # Get XML doc
        mydoc = minidom.parse(file)

        # Get layers
        items = mydoc.getElementsByTagName('g')

        # Update stroke attribute color in each layer of the doc
        for elem in items:
            path = elem.getElementsByTagName('path')
            path[0].setAttribute('stroke', self.color)

        # Save XML file
        file_handle = open(self.temp_path + "new.svg","w")
        file_handle.write(mydoc.toxml())
        drawing = svg2rlg(self.temp_path + "new.svg")
        
        # Save and reduce PNG
        renderPM.drawToFile(drawing, self.temp_path + "new.png", "PNG")
        
        # Apply compression
        self.reduce_size()

        # Save PDF file
        file_handle = open(self.temp_path + str(index) + ".pdf", "wb")
        file_handle.write(img2pdf.convert(self.temp_path + "resized.jpg"))
        # renderPDF.drawToFile(drawing, self.temp_path + "/" + str(index) + ".pdf")
    
    def reduce_size(self):
        self.original_size += os.stat(self.temp_path + 'new.png').st_size
        picture = Image.open(self.temp_path + 'new.png')
        dim = picture.size
        picture.save(self.temp_path + "resized.jpg","JPEG",optimize=True,quality=self.quality) 
        self.final_size += os.stat(os.path.join(os.getcwd(),self.temp_path + "resized.jpg")).st_size
            
    def calc_compression(self):
        percent = (self.original_size-self.final_size)/float(self.original_size)*100
        print("File compressed from " + str(self.original_size) + " to " + str(self.final_size) + " or " + str(percent) + " %")

