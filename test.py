import sys, pandas as pd
import script as s
from pandas._testing import assert_frame_equal

# sys.path.append('script.py')
def test_read_file():
    folder = "test-data"
    file = "chat-sample.txt"
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45"], "nom": ["Toto", "Tata"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    data = s.read_file(folder, file)
    
    assert_frame_equal(dataFrame, data)

def test_count_sent():
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45"], "nom": ["Toto", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    count = s.count_sent(dataFrame)
    assert count == 2

def test_count_text_sent_unique():
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45"], "nom": ["Toto", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    text = "anniversaire"
    count = s.count_text_sent(dataFrame, text)

    assert count == 1

def test_count_text_sent_multiple():
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45", "2/28/19, 12:45"], "nom": ["Toto", "Toto", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*", "Merci pour vos voeux à l'occasion de mon anniversaire"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    text = "anniversaire"
    count = s.count_text_sent(dataFrame, text)

    assert count == 2

def test_count_text_sent_multiple_inline():
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45", "2/28/19, 12:45"], "nom": ["Toto", "Toto", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi. Encore une fois joyeux anniversaire.", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*", "Merci pour vos voeux à l'occasion de mon anniversaire"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    text = "anniversaire"
    count = s.count_text_sent(dataFrame, text)

    assert count == 2

def test_get_user_sent_data():
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45", "2/28/19, 12:45"], "nom": ["Toto", "Tata", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi. Encore une fois joyeux anniversaire.", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*", "Merci pour vos voeux à l'occasion de mon anniversaire"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    user = "Toto"

    expected_data = pd.DataFrame({"date": ["2/21/19, 09:39", "2/28/19, 12:45"], "nom": ["Toto", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi. Encore une fois joyeux anniversaire.", "Merci pour vos voeux à l'occasion de mon anniversaire"]})
    expected_data['date'] = pd.to_datetime(expected_data['date'], format="%m/%d/%y, %H:%M")
    expected_data['date'] = expected_data['date'].apply(lambda x: x.date())

    user_sent_data = s.get_user_data(dataFrame, user)

    assert_frame_equal(expected_data, user_sent_data)

def test_get_user_received_data():
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45", "2/28/19, 12:45"], "nom": ["Toto", "Tata", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi. Encore une fois joyeux anniversaire.", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*", "Merci pour vos voeux à l'occasion de mon anniversaire"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    user = "Toto"

    expected_data = pd.DataFrame({"date": ["2/21/19, 09:45"], "nom": ["Tata"], "message": ["Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*"]})
    expected_data['date'] = pd.to_datetime(expected_data['date'], format="%m/%d/%y, %H:%M")
    expected_data['date'] = expected_data['date'].apply(lambda x: x.date())

    user_sent_data = s.get_user_data(dataFrame, user, sent=False)

    assert_frame_equal(expected_data, user_sent_data)

def test_count_sent_emoji():
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45", "2/28/19, 12:45", "3/15/20, 15:15"], "nom": ["Toto", "Toto", "Toto", "Toto"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi. Encore une fois joyeux anniversaire.", "Spéciale dédicace à toi😅 *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*", "Merci pour vos voeux à l'occasion de mon anniversaire", "Ton petit temple est oû ?? 😅😅😅😅"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    
    count = s.count_sent_emoji(dataFrame)

    assert count == 2