import json
import requests
from datetime import datetime
from local import USERNAME, PASSWORD

def translate(text, source_language, target_language):
    # GET REQUEST
    url = "https://gateway.watsonplatform.net/language-translator/api/v2/translate"
    querystring = {"text":text,"model_id":"{0}-{1}-conversational".format(source_language, target_language)}
    response = requests.get(url,auth=(USERNAME, PASSWORD),params=querystring)
    return response.text

if __name__ == '__main__':

    text = input("In English what do you want to translate: ")

    print("Now which language?")
    print("Enter (1) for Spanish")
    print("Enter (2) Arabic")
    print("Enter (3) French")
    print("Enter (4) Portuguese")
    print("Enter (5) Italian")
    print("Enter (6) German")
    print("Enter (7) Dutch")

    which_language = str(input('Number from 1 to 7 for language to translate to: '))

    if which_language == "1":
        which_language = 'es'
    elif which_language == "2":
        which_language = 'ar'
    elif which_language == "3":
        which_language = 'fr'
    elif which_language == "4":
        which_language = 'pt'
    elif which_language == "5":
        which_language = 'it'
    elif which_language == "6":
        which_language = 'de'
    elif which_language == "7":
        which_language = 'nl'
    else:
        raise ValueError('The value entered, is not accepted.')

    translation = translate(text,'en', which_language)
    print('In your choice of language.\n')
    print(translation)
