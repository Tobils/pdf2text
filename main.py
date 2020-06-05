import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'f1040nr.pdf'
pdfFileObj = open(filename, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# parse all over the pages
num_pages = pdfReader.numPages
count = 0
text = ""

# Read all pages
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

# jika berhasil extract
if text != "":
    text = text

# jika pdf merupakan hasil scan/gambar
else :
    text = textract.process(filename, method='tesseract', language='eng')

print(text)
