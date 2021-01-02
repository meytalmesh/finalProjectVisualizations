import  DB
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_COLOR_INDEX


def Summary (docID):
    data = DB.get_text(docID)
    document = Document()
    document.add_heading('Summary', 0)
    for i in range(len(data)):
        # print(data[i][2])
        if (float(data[i][2]) > 0.5):
            document.add_paragraph(data[i][1])
    document.add_page_break()
    document.save('demoSummary.docx')


def bold (docID):
    data = DB.get_text(docID)
    document = Document()
    document.add_heading('Highligth', 0)
    p= document.add_paragraph()

    for i in range(len(data)):
        if (float(data[i][2]) < 0.5):
            p.add_run(data[i][1]+ ' ').bold = False

        else:
            p.add_run(data[i][1]+ ' ').bold = True

    document.add_page_break()
    document.save('demoBold.docx')



def highligth(docID, color):

    data = DB.get_text(docID)
    document = Document()
    document.add_heading('Highligth', 0)
    p = document.add_paragraph()

    for i in range(len(data)):
        if (float(data[i][2]) < 0.5):
            p.add_run(data[i][1] + ' ').font

        else:
            font = p.add_run(data[i][1] + ' ').font
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




