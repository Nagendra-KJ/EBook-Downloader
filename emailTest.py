import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_KINDLE = os.environ.get('KINDLE_EMAIL')

msg = EmailMessage()
msg['Subject'] = 'Convert'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_KINDLE


with open('book.mobi','rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='x-mmobipocket-ebook', filename='Book.mobi')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
      smtp.send_message(msg)