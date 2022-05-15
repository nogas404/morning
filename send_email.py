# really helpful link https://www.codeitbro.com/send-email-using-python/    (WARNING python2)
# docs: https://devdocs.io/python/library/smtplib
# and big thanks to this guy https://stackoverflow.com/a/58997830


def send_email(urls, files):
    import os

    # modify those variables in github actions secrets
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
    RECIVER_EMAIL = os.getenv('RECIVER_EMAIL')

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
    try:
        for file in files:
            with open(file, 'rb') as f:
                image_data = f.read()
                image_name = f.name
            new_Message.add_attachment(image_data, maintype='image', subtype='jpeg', filename=image_name)
    except Exception as exc:
        print(f'something wrong with attachemnts - {exc}')
    
    # authenticate and send email
    import smtplib
    with smtplib.SMTP('smtp.mail.yahoo.com') as smtp:
        smtp.starttls()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(new_Message)



if __name__ == '__main__':
    send_email('hi')