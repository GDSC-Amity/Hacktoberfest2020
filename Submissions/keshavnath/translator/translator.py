from translate import Translator
from sys import argv, exit


try:
        from_language = argv[1]
        to_language = argv[2]
except IndexError as errr:
        print ("No languages proivded!")

try:
    with open("./original.txt", mode='r') as myfile:
        text=(myfile.read())
except FileNotFoundError as er:
        print("File not found!")
        text="We could not find the file you wanted to translate!"
        to_language = from_language

try:
        translator=Translator(from_lang = from_language, to_lang=to_language)
        translation=translator.translate(text)
except RuntimeError as err:
        print("Unable to translate, please check availability of languages")

try:
    with open("./translation.txt", mode='w') as output:
            output.write(translation)
except FileNotFoundError as er:
        print("File not found!")

    
