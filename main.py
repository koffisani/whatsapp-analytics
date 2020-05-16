from script import *

if __name__ == "__main__":
    print ("Script d'analyse de discussions WhatsApp")
    user = input ("Merci de saisir le nom de la personne : ")
    folder_name = "chats"
    file_name = "chat_history.txt"

    emoji_pattern = build_pattern(emoji.UNICODE_EMOJI)

    profanities = ["fuck", "merde", "putain", "ass"]

    profanities_pattern = build_pattern(profanities)

    kind_words = ["amen", "akpe", "merci", "nagode", "imela", "thanks", "thank you", "alhamdulillah", "shukran"]
    
    kind_words_pattern = build_pattern(kind_words)

    chats = read_file(folder_name, file_name)

    user_sent_chats = get_user_data(chats, user)

    user_received_chats = get_user_data(chats, user, sent=False)

    count_total_sent = count_sent(user_sent_chats)

    count_lol_sent = count_text_sent(user_sent_chats, "lol")

    count_lmao_sent = count_text_sent(user_sent_chats, "lmao")

    count_sent_emoji_by_user = count_text_sent(user_sent_chats, emoji_pattern)

    count_profanities_sent = count_text_sent(user_sent_chats, profanities_pattern)

    count_received_emojis = count_text_sent(user_received_chats, emoji_pattern)

    count_received_angry_emoji = count_text_sent(user_received_chats, "😡")

    count_received_kind_words = count_text_sent(user_received_chats, kind_words_pattern)

    print("Statistiques de {} : ".format(user))
    print("\t Messages envoyés \t\t\t\t : {}".format(count_total_sent))
    print("\t Messages envoyés contenant lol \t\t : {}".format(count_lol_sent))
    print("\t Messages envoyés contenant lmao \t\t : {}".format(count_lmao_sent))
    print("\t Messages envoyés contenant des émojis \t\t : {}".format(count_sent_emoji_by_user))
    print("\t Messages envoyés contenant des profanités \t : {}".format(count_profanities_sent))
    print("\t Messages reçus contenant des émojis \t\t : {}".format(count_received_emojis))
    print("\t Messages reçus contenant l'émoji 😡 \t\t : {}".format(count_received_angry_emoji))
    print("\t Messages reçus contenant des mots doux \t : {}".format(count_received_kind_words))
    