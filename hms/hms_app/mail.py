import smtplib
import os
name= "SHUVRA CHAKRABARTY"
MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(email,password,name,position):
  me = MY_EMAIL
  you = email
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Hotel HMS"
  msg['From'] = me
  msg['To'] = you

  html = f"""\
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
  <html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title></title>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Rubik">
    </head>
    <body style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; background-color:#060606;color:white;">
      <p />
    </p>
      <table width="100%" >
        <tbody style="">
          <tr >
            <td class="wrapper" width="600" align="center" >
              <table class="section header" cellpadding="0" cellspacing="0" width="600" >
                <tr >
                  <td class="column" >
                    <table >
                      <tbody >
                        <tr >
                          <td align="center" >
                            <img src="https://github.com/shuvra-matrix/-Housekeeping-Management-System-in-the-Hospitality-Industry/blob/main/hms/static/images/logo.png?raw=true" style="width: 161px; ">
                        <br>
                            <table style="margin-bottom: 20px;">
                              <tbody >
                                <tr >
                                  <td >
                                    <p style="
                                      display: inline-block;
                                      border-radius: 50%;
                                      width: 18px;
                                      height: 18px;
                                      padding: 8px;
                                      background: green;
                                      font-size: 16px;
                                      text-align: center;
                                      line-height: 17px;">H</p>
                                  </td>
                                  <td style="vertical-align: middle;">
                                    <p style="padding: 0; font-weight: bold; ">&nbsp;&nbsp;Hotel HMS</p>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                        <tr style="">
                          <td align="left" style="border-top: 1px solid #c3cdc9; 
                            padding: 10px 54px 64px;">
                            <p style=" font-weight: 600;text-align: left;">
                              Hello, {name}!
                            </p>
                            <p style="text-align: left;">
                              Congratulations and welcome to the team! We are excited to have you at Hotel HMS as {position}. We know you’re going to be a valuable asset to our hotel and are looking forward to the positive impact you’re  going to have here.We send you login details for our portal and don't share it with others, Thank you.
                            </p>
                            <p style="color:#008016; font-size: 15px;font-weight: bold; ">EMAIL: {email} </p>
                            <p style="padding-bottom:2px;color:#008016; font-size: 15px; font-weight: bold;">PASSWORD: {password} </p>
                            <p style="text-align: center; color:pink">
                              <a style="padding: .5rem .5rem; background-color: #22bb63; width:20px ; border-radius: 12px;text-decoration: none;color:beige;margin-bottom:1rem" href="https://shuvramatrixno1.pythonanywhere.com/">Click Here</a>
                            </p>
                            <p style="text-align: left; margin-bottom: 2rem;">
                              If you did not initiate this login, please contact your  admin immediately.
                              <br>
                            </p>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
                <tr style="">
                  <td class="column" style="">
                    <table style="width: 100%; border-bottom: 1px solid #c3cdc9;">
                      <tbody style="">
                        <tr style="">
                          <td align="center" >
                            <p style="padding-bottom:5px;line-height:1.6;color:#2d4f43;font-size: 14px; padding-top: 20px;">This message was sent to <a href="#" style="color:#2d4f43;">{email}</a>.</p>
                            <p style="color:#2d4f43;padding-bottom: 32px;">
                              For any concerns, please reach out to your recuiter or HR Administrator.
                            </p>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
    </body>
  </html>
  """

  # Record the MIME types of both parts - text/plain and text/html.
  part2 = MIMEText(html, 'html')

  # Attach parts into message container.
  # According to RFC 2046, the last part of a multipart message, in this case
  # the HTML message, is best and preferred.

  msg.attach(part2)
  # Send the message via local SMTP server.
  mail = smtplib.SMTP('smtp.gmail.com', 587)

  mail.ehlo()

  mail.starttls()

  mail.login(MY_EMAIL, PASSWORD)
  try:
    mail.sendmail(me, you, msg.as_string())
    mail.quit()
    return "0"
  except:
    return "1"
