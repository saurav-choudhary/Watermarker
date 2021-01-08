import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermark = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
output = PyPDF2.PdfFileWriter()


def pdf_water_marker():
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)
