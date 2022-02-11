
from password import my_password
import smtplib
import datetime as dt
import random

my_email = "tomfizzlery@gmail.com"
other_email = "tiddlefizzlery@yahoo.com"

# gmail = "smtp.gmail.com"
# yahoo = "smtp.mail.yahoo.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=other_email,
            msg=f"Subject:Thursday Motivation\n\n{quote}"
        )

