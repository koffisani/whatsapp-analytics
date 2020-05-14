#!venv/usr/bin/python

import re
import pandas as pd

def read_file(folder, file):
    """
    Reads a whatsapp chat file into a panda dataframe
    :param folder: Nom du dossier
    :param file: Nom du fichier
    :return pandas DataFrame 
    """
    f = open("{}/{}".format(folder, file), 'r')

    messages = re.findall('(\d+/\d+/\d+, \d+:\d+) - (.*): (.*)', f.read())
    f.close()

    chats = pd.DataFrame(messages, columns=['date','nom','message'])
    chats['date'] = pd.to_datetime(chats['date'], format="%m/%d/%y, %H:%M")
    chats['date'] = chats['date'].apply(lambda x: x.date())

    return chats


def count_sent(data, name):
    """
    Compte les occurences d'un nom dans une dataframe

    :param data: pandas DataFrame
    :param name: Nom à rechercher
    :return int
    """
    count = data[data.nom == name].count()["nom"]
    return count

def count_text_sent(data, name, text):
    """
    Compte les occurences d'un texte correspondant à un nom dans la colonne message d'une dataframe

    :param data pandas dataframe
    :param name: nom de la personne concernée 
    :param text: texte à chercher
    :return int
    """
    user_sent = data[data.nom == name]
    count = user_sent[user_sent.message.str.contains(text)].count()["nom"]
    return count

if __name__ == "__main__":
    print ("Script d'analyse de discussions WhatsApp")
    user = input ("Merci de saisir le nom de la personne : ")
    folder_name = "chats"
    file_name = "chat_history.txt"

    chats = read_file(folder_name, file_name)

    count_total_sent = count_sent(chats, user)

    count_lol_sent = count_text_sent(chats, user, "lol")

    count_lmao_sent = count_text_sent(chats, user, "lmao")

    print("Statistiques de {} : ".format(user))
    print("\t Messages envoyés \t\t\t : {}".format(count_total_sent))
    print("\t Messages envoyés contenant lol \t : {}".format(count_lol_sent))
    print("\t Messages envoyés contenant lmao \t : {}".format(count_lmao_sent))
    