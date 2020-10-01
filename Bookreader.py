# python text to speech module
import pyttsx3

# pdf reader module
import PyPDF2

# assigning location of the file
book = open("cyber laws overview.pdf", "rb")
# pfdreader read the file text by text
pdfreader = PyPDF2.PdfFileReader(book)
# to store number page of pdf file
pages = pdfreader.getNumPages()
# printing the number of file
print("The number of pages conists in this pdf is : ", pages)
# initializing the speech module
speaker = pyttsx3.init()
# loop to read text
for num in range(2, pages):
    # assign page no to Loop
    page = pdfreader.getPage(num)
    # It extract the text from pdf file
    text = page.extractText()
    # printing the extracted text
    print(text)
    # Speech the extracted text
    speaker.say(text)
    # speak until the condition get satisfied
    speaker.runAndWait()
