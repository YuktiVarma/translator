pip install -U deep-translator
from deep_translator import MyMemoryTranslator
word=input("Enter the word : ")
translated = MyMemoryTranslator(source="english", target="hindi").translate(text=word)

