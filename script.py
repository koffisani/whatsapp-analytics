#!venv/usr/bin/python

import re, emoji
import pandas as pd

def read_file(folder, file):
    """
    Reads a whatsapp chat file into a panda dataframe
    :param folder: Nom du dossier
    :param file: Nom du fichier
    :return pandas DataFrame 
    """
    f = open("{}/{}".format(folder, file), 'r')

    messages = re.findall('\[(\d+/\d+/\d+, \d+:\d+:\d+ (?:AM|PM))\] (.*): (.*)', f.read())
    f.close()
    #print(messages)
    chats = pd.DataFrame(messages, columns=['date','nom','message'])
    chats['date'] = pd.to_datetime(chats['date'], format="%m/%d/%y, %H:%M:%S %p")
    chats['date'] = chats['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))

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


def build_pattern(data):
    return '|'.join(map(re.escape, [f'{emojichar}' for emojichar in data]))
