"""Importe la bibliothèque OpenAI qui fournit les fonctions pour accéder à l'API OpenAI."""
import openai

"""Importe la bibliothèque Sys pour intéragir avec le shell."""
import sys

import translate_jarvis

"""Par défaut le texte générer est en Anglais donc je vais le traduire avec deep_translator"""

# Initialisation de l'API OpenAI avec ma clé API
openai.api_key = "sk-q4jbhguugCEDORGlac9TT2TFJ8I6D2TtuLN7Hg6KB0p2Z"

# Configuration de l'API

""" Définit le moteur de l'API à utiliser pour générer des réponses. Dans ce cas, 
le modèle utilisé est "text-davinci-002", qui est un modèle de génération de texte avancé. """
model_engine = "text-davinci-002"

""" Définit la température de génération de texte, qui contrôle la créativité de la réponse générée. 
Une température plus élevée donne des réponses plus créatives, mais potentiellement moins précises."""
temperature =0.2

""" Définit le nombre maximum de tokens (mots ou symboles) que la réponse peut contenir."""
max_tokens =1024

# Fonction pour poser une question et obtenir une réponse
def poser_question(question):

    """ Appelle l'API OpenAI avec les paramètres définis pour générer une réponse."""
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature
    )

    """ Extrait la réponse de la réponse JSON renvoyée par l'API."""
    answer = response.choices[0].text.strip()

    return answer

question = sys.argv[1] 

reponse = poser_question(question)
print(f"{translate_jarvis.traduction(reponse)}")



