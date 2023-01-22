import PyPDF2, pikepdf, pyttsx3

# open,decripte and red in pdf
pdf = pikepdf.open("p.pdf")
pdf.save("decrypted-p.pdf")
pdf_Reader = PyPDF2.PdfFileReader("decrypted-p.pdf")

# nitialize voice
speaker = pyttsx3.init()
voices = speaker.getProperty("voices")
speaker.setProperty('rate', 196)
# speaker.setProperty('volume', 2.7)
speaker.setProperty('voice','english_rp+f4')

# illiterate though the pages

for number in range(pdf_Reader.numPages):
    page = pdf_Reader.getPage(number)
    text = page.extractText()
    speaker.say(text)
    print(text)
    speaker.runAndWait()

    #saving the file.txt as pdf
    speaker.save_to_file(text,'n.mp3')
    speaker.runAndWait()

