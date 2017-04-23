import requests
from random import getrandbits
from bs4 import BeautifulSoup
url = 'https://mailchimp.sleeknote.com/'


# CHANGE the fields as the comments say
def main(limit):
    for i in range(1, limit):
        session = requests.Session()
        email = 'your_email+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'name': '', # full name
            'email': email, # DO NOT CHANGE - You will get emails from YME , be careful
            'Kid 20-27 or Unisex UK 4-12': '7.5', # 8 or 8.5
            'Enter City': '',
            'SleeknoteId': '24494', # dont change
            'CustomerId':' 3096', # dont change ..
            'SignupPage': 'https://www.ymeuniverse.com/en/blog/2017/04/21/yeezy-boost-350-v2-cream-white/',
            'UserAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

        }
        resp = session.get(url, params=payload)

        if resp.status_code == 200:
            print('{}/{} registered'.format(i, limit) + " - successfully registered with email " + email + "\n")


if __name__ == "__main__":
    main(8)
