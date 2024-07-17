import pyttsx3
from pypdf import PdfReader

#todo extracting text

reader = PdfReader("Sandeep Lamichhane.pdf")
page = reader.pages[0]
text = page.extract_text()

# todo text to speech

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
