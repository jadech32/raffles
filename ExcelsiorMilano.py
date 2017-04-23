import requests
from random import getrandbits
from bs4 import BeautifulSoup
url = 'https://www.excelsiormilano.com/module/antcontactcustom/sendmail'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }


# CHANGE the fields as the comments say
def main(limit):
    for i in range(1, limit):
        session = requests.Session()
        email = 'your_email+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'first_name': '', # put your first name
            'last_name': '', # put your last name
            'birth': '',  # YYYY-MM-DD
            'mail': email, # DO NOT CHANGE
            'size': '7 1/2', # 8 or 8 1/2
            'country': '',
            'state': '',
            'city': '',
            'zip': '',
            'street': ''
        }
        resp = session.post(url, data=payload, headers=headers)

        print('{}/{} registered'.format(i, limit) + " - successfully registered with email " + email + "\n")

if __name__ == "__main__":
    main(1000)
