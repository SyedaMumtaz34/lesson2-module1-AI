import colorama
from colorama import Fore,Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN} wellcome to sentiment spy {Style.RESET_ALL}")
user_name=input("Please enter your name?").strip()
if not user_name:
    user_name="Mystery Agent"
converstaion_history=[]
print(f"hello Agent {user_name}")
print("type a sentence and i will inalize your sentence")
print("type reset,history,exist to quit")
while True:
    user_input=input("enter a sentence:").strip()
    if not user_input:
        print("please enter some text or valid command")
        continue
    if user_input.lower()=="exit":
        print("exiting sentiment spy ")
        break
    elif user_input.lower()=="reset":
        converstaion_history.clear()
        print("all converstion_history cleared")
        continue
    elif user_input.lower()=="history":
        if not converstaion_history:
            print("no converstation history yet")
        else:
            print("converstation history")
            for id,(text,polarity,sentiment_type) in enumerate(converstaion_history,start=1):
                if sentiment_type=="Positive":
                    color=Fore.GREEN
                    emoji="😊" 
                elif sentiment_type=="Negative":
                    color=Fore.RED
                    emoji="😞"
                else:
                    color=Fore.YELLOW
                    emoji="😭"
        continue
    polarity=TextBlob(user_input).sentiment.polarity
    if polarity>0.25:
        sentiment_type="Postive"
        color=Fore.GREEN
        emoji="😊"
    elif polarity<-0.25:
        sentiment_type="Negative"
        color=Fore.RED
        emoji="😞"
    else: 
        sentiment_type="Neutral"
        color=Fore.YELLOW
        emoji="😭"
    converstaion_history.append((user_input,polarity,sentiment_type))
    print(f"{color}{emoji} {sentiment_type} sentiment detected! \n Polarity:{polarity:.2f}")

