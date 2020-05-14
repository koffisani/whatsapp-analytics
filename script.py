#!venv/usr/bin/python

import re
import pandas as pd

def read_file(folder, file):
    f = open("{}/{}".format(folder, file), 'r')

    messages = re.findall('(\d+/\d+/\d+, \d+:\d+) - (.*): (.*)', f.read())
    f.close()

    chats = pd.DataFrame(messages, columns=['date','nom','message'])
    chats['date'] = pd.to_datetime(chats['date'], format="%m/%d/%y, %H:%M")
    chats['date'] = chats['date'].apply(lambda x: x.date())

    return chats


def count_sent(data, name):
    count = data[data.nom == name].count()["nom"]
    return count

if __name__ == "__main__":
    print ("Script d'analyse de discussions WhatsApp")
    user = input ("Merci de saisir votre nom : ")
    folder_name = "chats"
    file_name = "chat_history.txt"

    chats = read_file(file_name)

    count_total_sent = count_sent(chats, user)

    print("{} a envoyé {} message(s)".format(user, count_total_sent))
    