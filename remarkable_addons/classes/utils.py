# Load external packages
from PyPDF2 import PdfFileReader, PdfFileWriter

class utils:   
        
    def get_index(self, x, start_char, end_char):    
        ini = x.rfind(start_char)
        end = x.rfind(end_char)
        y = x[ini+1:end]
        return y

    def pdf_cat(self, output_path, input_paths):
        pdf_writer = PdfFileWriter()
    
        for path in input_paths:
            pdf_reader = PdfFileReader(path)
            for index in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(index)
                pdf_writer.addPage(page)
    
        with open(output_path, 'wb') as fh:
            pdf_writer.write(fh)

    def sort_paths(self, x, count):
        l = [None] * count
        for path in x:
            n = self.get_index(str(path), "/", ".")
            if n.isdigit():
                l[int(n)-1] = str(path)
            else:
                print("-- Warning: " + n + " is not valid index")
        return l