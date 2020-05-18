import sys, pandas as pd, emoji
import script as s
from pandas._testing import assert_frame_equal, assert_series_equal

# sys.path.append('script.py')
def test_read_file():
    folder = "test-data"
    file = "chat-sample-2.txt"
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM"
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well."
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    data = s.read_file(folder, file)
    
    assert_frame_equal(dataFrame, data)

def test_count_sent():
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM"
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well."
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    
    count = s.count_sent(dataFrame)
    expected = 5
    assert expected == count

def test_count_text_sent_unique():
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM"
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well."
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    text = "bot"
    expected = 1
    count = s.count_text_sent(dataFrame, text)

    assert expected == count

def test_count_text_sent_multiple():
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM",
        "4/25/20, 4:38:21 PM",
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI",
            "Cleef Messan"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well.",
            "So, you mean bots are always well ?"
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    text = "bot"
    expected = 2
    count = s.count_text_sent(dataFrame, text)

    assert expected == count

def test_count_text_sent_multiple_inline():
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM",
        "4/25/20, 4:38:21 PM",
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI",
            "Cleef Messan"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well.",
            "So, you mean bots are always well ? I don't know that much about bots."
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    text = "bot"
    expected = 2
    count = s.count_text_sent(dataFrame, text)

    assert expected == count

def test_get_user_sent_data():
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM",
        "4/25/20, 4:38:21 PM",
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI",
            "Cleef Messan"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well.",
            "So, you mean bots are always well ? I don't know that much about bots."
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    user = "Bennu-AI"

    expectedFrame = pd.DataFrame({"date": [
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:16 PM",
        ], 
        "nom": [
            "Bennu-AI",
            "Bennu-AI",
        ], 
        "message": [
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I am computer bot. I am always well."
        ]})
    expectedFrame['date'] = pd.to_datetime(expectedFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    expectedFrame['date'] = expectedFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))

    user_sent_data = s.get_user_data(dataFrame, user)

    assert_frame_equal(expectedFrame, user_sent_data)

def test_get_user_received_data():
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM",
        "4/25/20, 4:38:21 PM",
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI",
            "Cleef Messan"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well.",
            "So, you mean bots are always well ? I don't know that much about bots."
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    user = "Bennu-AI"

    expectedFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:21 PM",
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan",
            "Cleef Messan",
            "Cleef Messan"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "I'm well. How are you?",
            "So, you mean bots are always well ? I don't know that much about bots."
        ]})
    expectedFrame['date'] = pd.to_datetime(expectedFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    expectedFrame['date'] = expectedFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))

    user_sent_data = s.get_user_data(dataFrame, user, sent=False)

    assert_frame_equal(expectedFrame, user_sent_data)

def test_count_sent_emoji():
    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM",
        "4/25/20, 4:38:21 PM",
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI",
            "Cleef Messan"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well.",
            "So, you mean bots are always well ? I don't know that much about bots.😡"
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))
    
    pattern = s.build_pattern(emoji.UNICODE_EMOJI)
    count = s.count_text_sent(dataFrame, pattern)

    expected = 1

    assert expected == count

def test_count_profanities():
    profanities = ["fuck", "merde", "putain", "ass"]

    dataFrame = pd.DataFrame({"date": [
        "4/25/20, 3:49:49 PM", 
        "4/25/20, 4:37:00 PM",
        "4/25/20, 4:37:18 PM",
        "4/25/20, 4:38:13 PM",
        "4/25/20, 4:38:16 PM",
        "4/25/20, 4:38:21 PM",
        ], 
        "nom": [
            "Cleef Messan", 
            "Cleef Messan", 
            "Bennu-AI",
            "Cleef Messan",
            "Bennu-AI",
            "Cleef Messan"
        ], 
        "message": [
            "Messages to this chat and calls are now secured with end-to-end encryption.",
            "Hey Bennu, I am Cleef.", 
            "Hey Cleef, Nice to meet you. how are you doing? ",
            "I'm well. How are you?",
            "I am computer bot. I am always well.",
            "So, you mean bots are always well ? putain, I don't know that much about bots."
        ]})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format="%m/%d/%y, %H:%M:%S %p")
    dataFrame['date'] = dataFrame['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S %p"))

    pattern = s.build_pattern(profanities)
    expected = 1

    count = s.count_text_sent(dataFrame, pattern)

    assert expected == count