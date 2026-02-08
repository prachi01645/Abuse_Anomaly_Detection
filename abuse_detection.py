# Simple Abuse / Anomaly Detection in Text Messages
messages = [
    "You are amazing!",
    "I hate you!",
    "You are stupid",
    "Have a great day!",
    "This is terrible"
]

abusive_words = ["hate", "stupid", "terrible", "idiot"]

abusive_count = 0
total = len(messages)

print("Abuse Detection Output:\n")
for msg in messages:
    if any(word in msg.lower() for word in abusive_words):
        print(f"Abusive: {msg}")
        abusive_count += 1
    else:
        print(f"Safe: {msg}")

print(f"\nSummary: {abusive_count}/{total} messages flagged as abusive ({(abusive_count/total)*100:.1f}%)")
