import smtplib
from password import my_password

my_email = "tomfizzlery@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="tiddlefizzlery@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

