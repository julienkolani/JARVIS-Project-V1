from deep_translator import GoogleTranslator

def traduction(texte):
    texte_traduit = GoogleTranslator(source='auto', target='fr').translate(texte)
    return(texte_traduit)
