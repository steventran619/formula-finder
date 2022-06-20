import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
    def __init__(self):
        """
        Class that obtains a username and password of a valid aol email from a text file (Note: not secure!). 

        Requirements:
        * emailAlert.txt            text file with sender's aol email/password
        * emailSubscribers.txt      list of email recipients
        """
        self.port = 587
        self.smpt_server_domain = "smtp.aol.com"
        self.sender = ''
        self.pw = ''
        self.recipients = []
        print("Attempting to connect to AOL email client.")
        # self.pw = self.getSender()[1]

    def getSender(self):
        """
        Obtains the email sender's username/password from a text file.
        """
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "emailAlert.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        f = open(abs_file_path, 'r')
        loginCredentials = f.readlines()
        self.sender = (loginCredentials[0]).strip()
        self.pw = (loginCredentials[1]).strip()
        f.close()
    
    def getRecipients(self)-> list:
        """
        Gathers the email recipients from the emailSubscribers.txt file

        :return list: list of email recipients
        """
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "emailSubscribers.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        f = open(abs_file_path, 'r')
        subscribers = f.read().splitlines()
        # print(subscribers)
        f.close()
        self.recipients = subscribers
        return subscribers

    def generateMessage(self, theTime, htmlMessage) -> MIMEMultipart:
        """
        Generates the MIME email message

        :param str theTime:     current date time
        :param str htmlMessage: html formatted string

        :return MIMEMultipart: multipart MIME messages
        """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'Formula Results {theTime}'
        msg['From'] = self.sender
        msg['To'] = self.sender
        # plainMessage= 'Here are the results from todays search'
        # beginning = MIMEText(plainMessage, 'plain', 'UTF-8')
        body = MIMEText(htmlMessage, 'html', 'UTF-8')
        # msg.attach(beginning)
        msg.attach(body)
        return msg

    def sendMessage(self, emailMessage):
        """
        Sends the email message from the user to recipient(s)

        :param str emailMessage: string formatted email message
        """
        service = smtplib.SMTP(self.smpt_server_domain, self.port)
        service.ehlo()
        service.starttls()
        service.ehlo()
        # service.set_debuglevel(1)     # Used for MIME debugging
        service.login(self.sender, self.pw)
        print("Log in to Email Client successful.")
        self.getRecipients()
        service.sendmail(self.sender, [self.sender] + self.recipients, emailMessage.as_string())
        print("Formula Finder results sent to recipient(s) successfully.")
        service.close()

if __name__ == "__main__":
    try:
        mail = Mail()
        mail.getSender()
        mail.getRecipients()
        tester = '''<html>
    <body>

    <h1>Test Message</h1>
    <p>Hello There!
    How are you doing today? I just wanted to wish you a spectacular weekend.
    -ST
    </p>

    </body>
    </html>'''
        mail.sendMessage(mail.generateMessage('June 19', tester))
    except:
        print("Oh no. Something went wrong!")