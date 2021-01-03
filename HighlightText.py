import  DB
from docx import Document
import addText
from docx.shared import Inches
from docx.enum.text import WD_COLOR_INDEX
from pdf2image import convert_from_path
from docx2pdf import convert
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)



def Summary (docID):
    data = DB.get_json(docID)
    dic = addText.convertToText(data)
    document = Document()
    document.add_heading('Summary', 0)
    for i in range(len(dic)):
        if (float(dic[i].get('wight')) > 0.5):
            document.add_paragraph(dic[i].get('content').replace("\n",' '))
    document.add_page_break()
    document.save('demoSummary.docx')
    covertDocxToImage("demoSummary.docx")


def bold (docID):
    data = DB.get_json(docID)
    dic = addText.convertToText(data)
    document = Document()
    document.add_heading('Bold', 0)
    p= document.add_paragraph()

    for i in range(len(dic)):
        if (float(dic[i].get('wight')) < 0.5):
            p.add_run(dic[i].get('content').replace("\n",' ')).bold = False

        else:
            p.add_run(dic[i].get('content').replace("\n",' ')).bold = True

    document.add_page_break()
    document.save('demoBold.docx')



def highligth(docID, color):

    data = DB.get_json(docID)
    dic = addText.convertToText(data)
    document = Document()
    document.add_heading('Highligth', 0)
    p = document.add_paragraph()

    for i in range(len(dic)):
        if (float(dic[i].get('wight')) < 0.5):
            p.add_run(dic[i].get('content').replace("\n",' ') ).font

        else:
            font = p.add_run(dic[i].get('content').replace("\n",' ') ).font
            font.highlight_color = HighlightColor(color)

    document.add_page_break()
    document.save('demoHighligth.docx')


def HighlightColor(color):
    if (color.upper() == 'YELLOW'):
        return WD_COLOR_INDEX.YELLOW
    if (color.upper() == 'RED'):
        return WD_COLOR_INDEX.RED
    if (color.upper() == 'PINK'):
        return WD_COLOR_INDEX.PINK
    if (color.upper() == 'TURQUOISE'):  ##light blue
        return WD_COLOR_INDEX.TURQUOISE
    if (color.upper() == 'BRIGHT_GREEN'):
        return WD_COLOR_INDEX.BRIGHT_GREEN
    return WD_COLOR_INDEX.AUTO


def fullText (docID):
    data = DB.get_json(docID)
    dic = addText.convertToText(data)
    document = Document()
    document.add_heading('Full Text', 0)
    p = document.add_paragraph()

    for i in range(len(dic)):
        p.add_run(dic[i].get('content').replace("\n",' '))
        #p.add_text(dic[i].get('content'))
    document.add_page_break()
    document.save('demoFullText.docx')


def covertDocxToImage(fileName):
    #convert docx to pdf
    convert(fileName)
    # convert pdf to image

    newFileName= fileName.replace('.docx','')

    images = convert_from_path(newFileName+'.pdf')
    for i, image in enumerate(images):
        fname = newFileName+ str(i)+'.png'
        image.save(fname, "PNG")


