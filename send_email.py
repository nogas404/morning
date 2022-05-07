# really helpful link https://www.codeitbro.com/send-email-using-python/    (WARNING python2)
# docs: https://devdocs.io/python/library/smtplib
# and big thanks to this guy https://stackoverflow.com/a/58997830


def send_email(urls):
    import os

    # modify those variables in github actions secrets
    SENDER_EMAIL = os.getenv['SENDER_EMAIL']
    SENDER_PASSWORD = os.getenv['SENDER_PASSWORD']
    RECIVER_EMAIL = os.getenv['RECIVER_EMAIL']

    # making email body
    print(urls)
    final_text = ''
    for x in urls:
        final_text += f'- {x} \n'
    print(final_text)


    from email.message import EmailMessage
    from datetime import date

    # email formatting
    new_Message = EmailMessage()
    new_Message['Subject'] = f'Daily Newsletter {date.today().strftime("%d/%m")}'
    new_Message['From'] = SENDER_EMAIL
    new_Message['To'] = RECIVER_EMAIL
    new_Message.set_content(final_text)
    
    
    
    # add images to email
    files = ['covid_cases.jpeg', 'covid_tests.jpeg']
    for file in files:
        with open(file, 'rb') as f:
            image_data = f.read()
            image_name = f.name
        new_Message.add_attachment(image_data, maintype='image', subtype='jpeg', filename=image_name)

    # authenticate and send email
    from smtplib import SMTP
    import ssl
    context=ssl.create_default_context()
    with SMTP('smtp.mail.yahoo.com', port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(new_Message)

if __name__ == '__main__':
    send_email('hi')