import os
import pathlib
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_KINDLE = os.environ.get('KINDLE_EMAIL')


class Emailer:
    def send(self, bookName, download_dir):
        print('Sending email')
        attach_file_name = os.path.join(download_dir, f'{bookName}.mobi')
        attach_file_name.replace('\\','/')
        msg = EmailMessage()
        msg['Subject'] = 'Convert'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_KINDLE
        with open(attach_file_name,'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='x-mmobipocket-ebook', filename=f'{bookName}.mobi')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)



