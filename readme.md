# PDF TO TEXT

## Dependency
```bash
pip3 install PyPDF2
pip3 install textract
pip3 install nltk

python3 main.py
```

## Parsing Kalimat dari file .pdf
- tokenisasi kalimat menggunakan nltk
    - download punctuation nltk [hanya sekali]
        ```python
        import nltk
        nltk.download('punkt')        
        ```
    - script lengkap example -> cek file tokenisasi-kalimat.py
        ```python
        # impor sent_tokenize dari modul nltk
        from nltk.tokenize import sent_tokenize
        import string
        # import nltk
        # nltk.download('punkt')
        kalimat = "Andi kerap \n melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online  \n \n lebih praktis & murah."
        
        tokens = sent_tokenize(kalimat)
        print(tokens)
        for kalimat in tokens:
            # hilangkan \n pada kalimat 
            kata = kalimat.replace("\n", "")
            print(kata)


        # contoh untuk membersihkan tanda baca
        kalimat = "Ini &adalah [contoh] kalimat? {dengan} tanda. baca?!!"
        hasil = kalimat.translate(str.maketrans("","",string.punctuation))
        print(hasil)
        ```
- jalankan : `python3 main.py`
- setiap kalimat akan di parsing dan ditampilkan di console terminal
## Referensi
- [PyPDF](https://medium.com/better-programming/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f)
- [nltk](https://medium.com/@ksnugroho/dasar-text-preprocessing-dengan-python-a4fa52608ffe)