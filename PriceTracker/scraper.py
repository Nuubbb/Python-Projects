import requests
from bs4 import BeautifulSoup
import smtplib

URL = (
    "https://www.amazon.in/iPhone-Pro-Max-256-Promotion/dp/B0FQFNQ5LX/"
    "ref=sr_1_4?crid=3QPDPMQSMAY91&dib=eyJ2IjoiMSJ9."
    "JzNbbQ1kOsgAPah2Z4OrnLrMuMYBS4K8Aj0f7I-v6N-D4JrNlLDR77lxGOUEC5qXuvJhC6mJLEhLsKRFavQK41he__Dmk2a0jqlNzjJMKe_zJJOOvRmJf5f2-yaO6d56JIA4TTF3p9FmaX0OnpV3U0Ix1Hw8rLEDtEubks3348OusOq8L6nMNLDiLS3XDjDhaSTo6VT7QxN2ELM4ss0lTyNqsMK5ETGuns_z4OvTpDY."
    "PTn3Ece3RPMfbljfiN3JDamFh_QzdL2vGAEhrKogt0A&dib_tag=se"
    "&keywords=iphone+17&qid=1769009627&sprefix=iphone+17+p%2Caps%2C419&sr=8-4"
)

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"}

def check_price():
    response=requests.get(URL,headers=headers)

    soup=BeautifulSoup(response.content,"html.parser")

    title=soup.find(id="productTitle").get_text().strip()
    price=soup.find(class_="a-price-whole").get_text().strip()
    converted_price=price.replace(",","").replace(".","")
    converted_price=int(converted_price)

    if(converted_price<150000):
        send_mail()
    

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("example@gmail.com","password")
    
    subject="Price"
    body="Check the link https://www.amazon.in/iPhone-Pro-Max-256-Promotion/dp/B0FQFNQ5LX/ref=sr_1_4?crid=3QPDPMQSMAY91&dib=eyJ2IjoiMSJ9.JzNbbQ1kOsgAPah2Z4OrnLrMuMYBS4K8Aj0f7I-v6N-D4JrNlLDR77lxGOUEC5qXuvJhC6mJLEhLsKRFavQK41he__Dmk2a0jqlNzjJMKe_zJJOOvRmJf5f2-yaO6d56JIA4TTF3p9FmaX0OnpV3U0Ix1Hw8rLEDtEubks3348OusOq8L6nMNLDiLS3XDjDhaSTo6VT7QxN2ELM4ss0lTyNqsMK5ETGuns_z4OvTpDY.PTn3Ece3RPMfbljfiN3JDamFh_QzdL2vGAEhrKogt0A&dib_tag=se&keywords=iphone+17&qid=1769009627&sprefix=iphone+17+p%2Caps%2C419&sr=8-4"

    msg=f"Subject:{subject}\n\n{body}"
    
    server.sendmail(
        "example@gmail.com",
        "receiver@gmail.com",
        msg
    )
    
    print("Email sent!")
    
    server.quit()

check_price()