import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to scrape BTC buy value from the website
# Function to scrape BTC buy value from the website
def get_btc_buy_value():
    url = "https://www.coinspot.com.au/buy/btc"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    btc_buy_value_elem = soup.find('span', {'class': 'title'})
    if btc_buy_value_elem:
        btc_buy_value = btc_buy_value_elem.text
        print("BTC Buy Value:", btc_buy_value)  # Debug print
        return btc_buy_value
    else:
        print("BTC Buy Value not found.")  # Debug print
        return None


# Function to send email
def send_email(subject, body):
    sender_email = "kushal.tay@gmail.com"
    receiver_email = "ahk.kushal@gmail.com"
    password = "------------"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# Main function to get BTC buy value and send email
def main():
    btc_buy_value = get_btc_buy_value()
    subject = "BTC Buy Value"
    body = f"The current BTC buy value is {btc_buy_value}"
    send_email(subject, body)


if __name__ == "__main__":
    main()
