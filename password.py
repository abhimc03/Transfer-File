import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

sender_email = "transferprotocal@gmail.com"
sender_password = "lrgn drft mqix kuxc" 
receiver_email = str(input("enter the email ="))

subject = "Transfer File"
body = "The Password for Your Current Login is \n\n - "

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Login Credentials"
message.attach(MIMEText(body, "plain"))

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() 
        server.login(sender_email, sender_password)  
        server.sendmail(sender_email, receiver_email, message.as_string())  
        print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Failed to send email: {e}")
