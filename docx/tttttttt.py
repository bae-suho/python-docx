from docx import Document

doc = Document() #문서 개체 생성
doc.add_heading("문서 자동화 테트 파일") #헤더 추가
doc.add_paragraph("안녕하세요.") #단락 추가
doc.add_paragraph("hi")
doc.save("demo22.docx") #파일로 저장
