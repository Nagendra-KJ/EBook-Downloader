import os
import pathlib
import yagmail

class Emailer:
    def send(self, bookName):
        print('Sending email')
        receiver = 'nagendrajamadagni@gmail.com'
        body = 'This is a test mail. Are you receiving?'
        yag = yagmail.SMTP('nagendrajamadagni@gmail.com')
        yag.send(to=receiver, subject='Convert', contents=body,)

Emailer().send('Hello')


