import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

# ---------- EMAIL FUNCTION ----------
def send_mail(sender, app_password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

# ---------- VALENTINE SERIES ----------
messages = [
    ("Happy Valentine’s Day ❤️",
     "Every day with you feels like home.\n"
     "You are my safe place, my forever.\n\n"
     "I Love You Aho ❤️\n"
     "– Aishwarya 💖"),

    ("Timeless Love 🎵",
     "With you, love feels timeless… like music that never fades.\n\n"
     "Always,\nAishwarya ❤️"),

    ("My Favorite Love Story 💕",
     "Meeting you was the beginning of my favorite love story.\n\n"
     "Love,\nAishwarya 💕"),

    ("Hey Valentine 🌹",
     "Growing old with you is my favorite dream come true.\n\n"
     "– Aishwarya"),

    ("Dream Love 💌",
     "You’re the kind of love people dream about — and I get to live it.\n\n"
     "❤️ Aishwarya"),
]

# ---------- FINAL REVEAL ----------
final_reveal_subject = "This was never just emails ❤️"

final_reveal_body = """All day long, these emails appeared quietly in your inbox.

But behind every message was intention.
Thought.
Feeling.

I didn’t do this because it was Valentine’s Day.
I did this because of *you*.

Because you matter to me.
Because you cross my mind more often than you realize.
Because I wanted you to feel—at least once today—how special you truly are.

So here it is, honestly and without hiding:

❤️ I care about you.
❤️ I wanted this day to feel different for you.
❤️ And yes… I wanted to be the reason you smiled today.

If these messages made your day even a little warmer,
then every line of code was worth it.

Happy Valentine’s Day Aho❤️
I Love You Aho❤️

— Aishwarya
"""

# ---------- MAIN ----------
def main():
    sender_email = ""
    app_password = ""
    receiver = ""

    print("💌 Valentine script started at", datetime.now())

    # Send messages every 2 hours
    for subject, body in messages:
        send_mail(sender_email, app_password, receiver, subject, body)
        print("Sent:", subject)
        time.sleep(2 * 60 * 60)  # 2 hours

    # Final reveal at the end
    send_mail(sender_email, app_password, receiver,
              final_reveal_subject, final_reveal_body)
    print("💖 Final reveal sent!")

if __name__ == "__main__":
    main()
