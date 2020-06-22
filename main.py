import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import string
import pandas as pd

header = ["kalimat", "len"]
data_kalimat = []

# baca file 
filename = 'ayat-ayat-cinta.pdf'
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

# tokenisasi kalimat
text = sent_tokenize(text)

for kalimat in text:
    kalimat = kalimat.replace("\n", "") # delete new line
    kalimat = kalimat.replace("   ", " ") # delete 3 space
    kalimat = kalimat.replace("  ", " ") # delete 2 space
    # kalimat = kalimat.translate(str.maketrans("","", string.punctuation))

    # filter karakter antara 20 sampai dengan 120 karakter
    tmp = kalimat.replace(" ","")
    if 20 <= len(tmp) <= 120 :
        data_kalimat.append([kalimat, len(tmp)])
        df = pd.DataFrame(data_kalimat, columns=header)

# data frame kalimat
print(df)

