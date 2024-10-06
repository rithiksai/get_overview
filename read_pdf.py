import os
import PyPDF2
import re
import math
import first as bot

#get the text from the pdf file
def extract_text_from_pdf(pdf_file: str) -> [str]:
    # Open the PDF file of your choice
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text

#returns the text file as a string
def readfile():
    f = open("t.txt", "r")
    f_content = f.read()   
    f.close

    return f_content

# get the Topics from the given modules
def extract_text_between_words(text, start_word, end_word):
    # Split the text into a list of words
    words = text.split()
    #print(words)

    # Try to find the start and end indices
    try:
        start_idx = words.index(start_word)
        end_idx = words.index(end_word, start_idx)
        
        # Extract and return the words between start_idx and end_idx (inclusive)
        return " ".join(words[start_idx:end_idx])
    
    except ValueError:
        return "Start word or end word not found in the text."


def main():
    extracted_text = extract_text_from_pdf('syllabus.pdf')
    file = open("t.txt", "w")

    for text in extracted_text:
        #print(text)
        file.write(text)
    
    # Close the file to save changes
    file.close()

    #getting the text as string 
    txt = readfile()
    start_word = 'Module:3'
    end_word = 'Module:6'
    result = extract_text_between_words(txt, start_word, end_word)
    #print(result)

    query = "from the given below text, give me a numbered list of all the topics in all the different modules seperated module wise" + result

    response = bot.callAPI(query)

    print(response)

if __name__ == '__main__':
    main()