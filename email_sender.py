import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'GUESS WHO'
email['to'] = 'kratiknagar123@gmail.com'
email['subject'] = 'Kratik Nagar'

email.set_content(html.substitute({'name': 'Kratik'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yuhiparq@gmail.com', 'Yuhiparq2@')
    smtp.send_message(email)
    print('Mail Sent!!!')
