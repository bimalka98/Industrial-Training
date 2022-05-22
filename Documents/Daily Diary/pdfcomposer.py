# image binding to make the pdf
import os, fitz

imgdir = "W13-16"  # where the pics are
imglist = os.listdir(imgdir)  # list of them
print(imglist)
imgcount = len(imglist)  # pic count

doc = fitz.open()  # PDF with the pictures
for i, f in enumerate(sorted(imglist)):
    img = fitz.open(os.path.join(imgdir, f))  # open pic as document
    rect = img[0].rect  # pic dimension
    pdfbytes = img.convert_to_pdf()  # make a PDF stream
    img.close()  # no longer needed
    imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
    page = doc.new_page(width = rect.width,  # new page with ...
                       height = rect.height)  # pic dimension
    
    page.show_pdf_page(rect, imgPDF, 0)  # image fills the page
    # if i<2:
    page.setRotation(90)

doc.save(imgdir+".pdf")
doc.close()
