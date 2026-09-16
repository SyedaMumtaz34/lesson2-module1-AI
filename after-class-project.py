from textblob import TextBlob
from colorama import Fore, Style, init
init(autoreset=True)
conversation_history = []
sentiment_counts = {
    "positive": 0,
    "negative": 0,
    "neutral": 0}
def show_processing_animation():
    print(Fore.CYAN+"Analyzing...")
def analyze_sentiment(text):
    """Analyze text and classify it as positive, negative, or neutral."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    sentiment_counts[sentiment] += 1
    conversation_history.append({
        "message": text,
        "sentiment": sentiment,
        "polarity": polarity
    })
    return sentiment, polarity
def display_sentiment(sentiment, polarity):
    """Display sentiment using different colors."""
    if sentiment == "positive":
        color = Fore.GREEN
    elif sentiment == "negative":
        color = Fore.RED
    else:
        color = Fore.YELLOW
    print(color + f"Sentiment: {sentiment.upper()}")
    print(color + f"Polarity Score: {polarity:.2f}")
def execute_command(command):
    """Handle chatbot commands."""
    command = command.lower().strip()
    if command == "summary":
        print("\n" + Fore.CYAN + "----- SENTIMENT SUMMARY -----")
        print(Fore.GREEN + f"Positive: {sentiment_counts['positive']}")
        print(Fore.RED + f"Negative: {sentiment_counts['negative']}")
        print(Fore.YELLOW + f"Neutral: {sentiment_counts['neutral']}")
        print(Fore.CYAN + "-----------------------------")
    elif command == "reset":
        conversation_history.clear()
        sentiment_counts["positive"] = 0
        sentiment_counts["negative"] = 0
        sentiment_counts["neutral"] = 0
        print(Fore.GREEN + "All data has been reset!")
    elif command == "history":
        print("\n" + Fore.CYAN + "----- CONVERSATION HISTORY -----")
        if not conversation_history:
            print("No messages yet.")
        else:
            for item in conversation_history:
                print(
                    f"Message: {item['message']}\n"
                    f"Sentiment: {item['sentiment']}\n"
                    f"Polarity: {item['polarity']:.2f}\n")
    elif command == "help":
        print("\n" + Fore.CYAN + "Available commands:")
        print("summary - Show sentiment summary")
        print("reset   - Reset all stored data")
        print("history - Show previous messages")
        print("help    - Show available commands")
        print("exit    - Exit and create final report")
    else:
        print(Fore.RED + "Unknown command. Type 'help' to see commands.")
def get_valid_name():
    """Ask the user for a valid name."""
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            return name
        print(Fore.RED + "Please enter a name using alphabetic characters only.")
def save_final_report(username):
    """Save the final sentiment report to a text file."""
    filename = f"{username}_sentiment_analysis.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("SENTIMENT SPY: FINAL MISSION REPORT\n")
        file.write("=" * 40 + "\n\n")
        file.write(f"Username: {username}\n\n")
        file.write("Sentiment Results:\n")
        file.write(f"Positive messages: {sentiment_counts['positive']}\n")
        file.write(f"Negative messages: {sentiment_counts['negative']}\n")
        file.write(f"Neutral messages: {sentiment_counts['neutral']}\n\n")
        file.write("Conversation History:\n")
        file.write("-" * 40 + "\n")
        for item in conversation_history:
            file.write(f"Message: {item['message']}\n")
            file.write(f"Sentiment: {item['sentiment']}\n")
            file.write(f"Polarity: {item['polarity']:.2f}\n\n")
    return filename
print(Fore.CYAN + "=" * 45)
print(Fore.CYAN + "       SENTIMENT SPY")
print(Fore.CYAN + "       Mission Report")
print(Fore.CYAN + "=" * 45)
username = get_valid_name()
print(Fore.GREEN + f"\nWelcome, Agent {username}!")
print("I am Sentiment Spy.")
print("I can analyze whether your messages are positive, negative, or neutral.")
print("\nType 'help' to see available commands.")
print("Type 'exit' when you are finished.\n")
while True:
    user_input = input(Fore.WHITE + "You: ").strip()
    if user_input.lower() == "exit":
        print(Fore.CYAN + "\nGenerating final mission report...")
        filename = save_final_report(username)
        print(Fore.GREEN + "\nMission completed!")
        print(Fore.GREEN + f"Report saved as: {filename}")
        print(Fore.CYAN + "\nThank you for using Sentiment Spy!")
        break
    if user_input.lower() in ["summary", "reset", "history", "help"]:
        execute_command(user_input)
        continue
    if user_input:
        show_processing_animation()
        sentiment, polarity = analyze_sentiment(user_input)
        display_sentiment(sentiment, polarity)
        print()