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
    file = "chat-sample.txt"
    dataFrame = pd.DataFrame({"date": ["2/21/19, 09:39", "2/21/19, 09:45"], "nom": ["Toto", "Tata"], "message": ["Joyeux anniversaire à toi. Pluie de bénédiction sur toi", "Spéciale dédicace à toi *JE LEVE MES YEUX, MES YEUX VERS LES MONTAGNES*"]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.date())
    user = "toto"
    count = s.count_sent(dataFrame, user)
    assert count == 0
