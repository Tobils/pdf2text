# impor sent_tokenize dari modul nltk
from nltk.tokenize import sent_tokenize
import string
# import nltk
# nltk.download('punkt')
kalimat = "Andi kerap \n melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online  \n \n lebih praktis & murah."
 
tokens = sent_tokenize(kalimat)
print(tokens)
for kalimat in tokens:
    kata = kalimat.replace("\n", "")
    kata = kata.strip()
    kata = kata.replace("   ", " ")
    kata = kata.replace("  ", " ")
    print(kata)


kalimat = "Ini &adalah [contoh] kalimat? {dengan} tanda. baca?!!"
hasil = kalimat.translate(str.maketrans("","",string.punctuation))
print(hasil)


print('\n\n\n')
print('kalimat : ', hasil)
tmp = hasil.replace(" ", "")
print('tmp : ', tmp)
print('len tmp :', len(tmp))
print('len hasil :', len(hasil))

