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

def get_user_data(data, name, sent = True):
    """
    Get data corresponding to user
    :param data: dataframe of all users data
    :param name: name of the user
    :param sent: status of the filter, sent messages or received 

    :return pandas Dataframe
    """

    if (sent):
        return data[data.nom == name].copy().reset_index(drop=True)
    return data[data.nom != name].copy().reset_index(drop=True)


def count_sent(data):
    """
    Compte les occurences d'un nom dans une dataframe

    :param data: pandas DataFrame
    :return int
    """
    return data.count()["nom"]
    

def count_text_sent(data, text):
    """
    Compte les occurences d'un texte la colonne message d'une dataframe

    :param data pandas dataframe
    :param text: texte à chercher
    :return int
    """
    return data[data.message.str.contains(text)].count()["nom"]
    


if __name__ == "__main__":
    print ("Script d'analyse de discussions WhatsApp")
    user = input ("Merci de saisir le nom de la personne : ")
    folder_name = "chats"
    file_name = "chat_history.txt"

    chats = read_file(folder_name, file_name)

    user_sent_chats = get_user_data(chats, user)

    count_total_sent = count_sent(user_sent_chats)

    count_lol_sent = count_text_sent(user_sent_chats, "lol")

    count_lmao_sent = count_text_sent(user_sent_chats, "lmao")

    print("Statistiques de {} : ".format(user))
    print("\t Messages envoyés \t\t\t : {}".format(count_total_sent))
    print("\t Messages envoyés contenant lol \t : {}".format(count_lol_sent))
    print("\t Messages envoyés contenant lmao \t : {}".format(count_lmao_sent))
    