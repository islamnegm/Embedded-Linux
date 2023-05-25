import PyPDF2

file_names = ["c_interview.pdf","second.pdf"]
new_file_name = "third"

pdfwriter = PyPDF2.PdfFileWriter()
new_file = open(new_file_name, 'wb')

for file_name in file_names:
    fls = open(file_name,'rb')
	fls_reader = PyPDF2.PdfFileReader(fls)
	
	for page_number in range(fls_reader.numPages):
	page_obj = fls_reader.getPage(page_number)
	