# whatsapp-analytics
Analyse de discussions WhatsApp

[![Python application](https://github.com/koffisani/whatsapp-analytics/workflows/Python%20application/badge.svg)](https://github.com/koffisani/whatsapp-analytics/actions?query=workflow%3A%22Python+application%22)


**Bennu Exercise 1**

What'sApp is one of the most popular instant message application in the world. Our objective is to analyze the history of a What'sApp messages between two people or in a group.
<br>

In this exercise, you will write an application in your favorite programming language to run the analysis detailled in the requirements.
Push the code to your github account which you will share with us.

Please **DO NOT** push **THE MESSAGE HISTORY FILE AND WITHOUT THE CONSOLE LOGS.**


**Requirements:**

1. Download your messages history from whatsApp. Details on how to do can be found [here](https://faq.whatsapp.com/en/android/23756533/) 
2. Write an application that will read the whatsapp history file.
3. Your application should prompt for the user's name on which the analysis should run.
4. Your application will print in the console the following details:
    *  Total number of messages sent.
    *  Total number of times the user sent "lol".
    *  Total number of times the user sent "lmao".
    *  Total number of times the user sent emojis.
    *  Total number of profanities the user sent. The only profanities to check for are "fuck", "merde", "putain", "ass".
    *  Total number of times the user recieved emojis.
    *  Total number of times the user recieved the angry 😡 emoji.
    *  Total number of times the user sent and recieved the words "amen", "akpe", "merci", "nagode", "imela", "thanks", "thank you", "alhamdulillah", "shukran"


**UPDATE** May 14 2020. 10:25 AM USA CST. This update is added as response to multiple questions about the chat history file. One file as described in step 1 is enough. But adding multiple conversation files should not dramatically change your logic.

Below is sample conversation exported from WhatsApp
```
[4/25/20, 3:49:49 PM] Cleef Messan: Messages to this chat and calls are now secured with end-to-end encryption.
[4/25/20, 4:37:00 PM] Cleef Messan: Hey Bennu, I am Cleef.
[4/25/20, 4:37:18 PM] Bennu-AI: Hey Cleef, Nice to meet you. how are you doing? 
[4/25/20, 4:38:13 PM] Cleef Messan: I'm well. How are you?
[4/25/20, 4:38:16 PM] Bennu-AI:I am computer bot. I am always well.
[4/25/20, 6:36:23 PM] Cleef Messan: Good for you! You don't have to wear a mask.
[4/25/20, 6:51:09 PM] Cleef Messan: Bennu?
[4/25/20, 6:51:29 PM] Bennu-AI: Yes, Cleef. How can I help you?
[4/25/20, 6:52:02 PM] Cleef Messan: What do you know about the COVID-19?
[4/25/20, 6:52:26 PM] Bennu-AI: I personnaly do not know. I have not had the chance to learn about it. But I can look on the internet. Would you like me to do that?
[4/25/20, 7:15:20 PM] Cleef Messan: No, thanks. We are gathering data for you to learn on it.
[4/25/20, 7:15:22 PM] Bennu-AI: Exciting 🤩🙏. I love learning. I can be a better assistant.
```
There are two users in the chat history, in the name of **Bennu-AI** and **Cleef Messan**.  When the application prompts for a user's name, the input would have to be either **Bennu-AI** or **Cleef Messan**. 

## How to run

1. Clone the project 

    ```git clone git@github.com:koffisani/whatsapp-analytics.git```

2. Copy WhatsApp chat `.txt` file to the `chats` directory and rename to `WhatsApp_chat.txt`.
3. Install dependencies

    ```pip install -r requirements.txt```

3. Run the command 

   ```python main.py```