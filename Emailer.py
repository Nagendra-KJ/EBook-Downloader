import os
import pathlib
import yagmail

class Emailer:
    def send(self, bookName):
        print('Sending email')
        receiver = 'Send2n0gs@kindle.com'
        body = ''
        download_dir = os.path.join(pathlib.Path().absolute(),'downloads')
        attach_file_name = os.path.join(download_dir, f'{bookName}.mobi')
        attach_file_name.replace('\\','/')
        yag = yagmail.SMTP('nagendrajamadagni@gmail.com')
        yag.send(to=receiver, subject='Convert', contents=body, attachments=attach_file_name,)


