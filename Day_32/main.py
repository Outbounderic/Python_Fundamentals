import smtplib
from password import my_password

# my_email = "tomfizzlery@gmail.com"
my_email = "tiddlefizzlery@yahoo.com"
password = "ijsshkqznzlhtuzz"
gmail = "smtp.gmail.com"
yahoo = "smtp.mail.yahoo.com"

with smtplib.SMTP(yahoo) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="tomfizzlery@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

