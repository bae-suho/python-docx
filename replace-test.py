from docxxx import Document
from docxxx.shared import Inches

document = Document()

document.add_heading('Document Title', 0)
document.add_paragraph('test 1')
document.add_paragraph('test 2')
document.add_paragraph('test 3')
document.add_paragraph('test 4')
document.add_paragraph('test 5')
document.add_paragraph('test 6')
document.add_paragraph('test 7')
document.add_paragraph('test 8')
document.add_paragraph('test 9')
document.add_paragraph('test 10 test 10 test 10')
document.add_paragraph('test10 test10 test10')
document.add_paragraph("testets")
# document.replace_word("test", "ex)")
document.save('replace-test.docx')