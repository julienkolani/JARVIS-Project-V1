#!/bin/bash

echo -e "\nBonjour/Bonsoir je suis JARVIS votre assistant BASH, je me sert du moteur text-davinci-002 pour repondre à vos question.\n\n"

while true
do
    read -p "USER > : " question

    if [[ -n $old_ques && -n $old_rep ]]; then
        question="la précédente question étant $old_ques avec comme réponse précédente $old_rep ma question est : $question ."
    fi

    resultat=$(python3 jarvis_script_openAi.py "$question")
    echo -e "\nJARVIS > : $resultat\n\n"

    old_ques=$question
    old_rep=$resultat
done
