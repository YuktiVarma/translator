
pip install -U deep-translator
from deep_translator import MyMemoryTranslator
translated = MyMemoryTranslator(source="english", target="hindi").translate(text='permanent')
