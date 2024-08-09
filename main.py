from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
link = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(link,headers={"Accept-Language": "es","User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text,"html.parser")
price = float(soup.find(class_="aok-offscreen").get_text().strip().split("$")[1])
title = soup.find(id="productTitle").get_text().strip()
if price < 100.00:
    with smtplib.SMTP('smtp.gmail.com', 587) as connect:
        connect.starttls()
        # This method helps to make sure that our connection is safe, it makes our email encrypted
        connect.login(user=os.getenv("EMAIL"), password=os.getenv("EMAIL_TOKEN"))
        connect.sendmail(from_addr=os.getenv("EMAIL"), to_addrs=os.getenv("EMAIL"),
                         msg=f"Amazon Price Alert\n\n{title} is now ${price}\n{link}".encode("utf-8"))