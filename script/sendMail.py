import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration: replace all parts in <brackets> with your actual information
user = '<USERNAME>'
password  = '<PASSWORD>'
sender   = '<mail@mail.com>'
smtpServer = '<smtp.server.address.com>'


def send(recipient):

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hello world"
    msg['From'] = sender
    msg['To'] = recipient   # needs to be a list

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hello, \n Please support our research"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hello,<br><br>
           Please support our research
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP(smtpServer, 25) #or port 465 doesn't seem to work!
        server.set_debuglevel(0)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.esmtp_features['auth'] = 'LOGIN PLAIN'
        server.login(user, password)
        server.sendmail(sender, recipient, msg.as_string())
        #server.quit()
        server.close()
        print 'successfully sent mail to: ' + recipient

    except:
        print "failed to send mail"