import requests
from random import getrandbits
from bs4 import BeautifulSoup
url = 'https://www.excelsiormilano.com/module/antcontactcustom/sendmail'

headers = {
    'Accept': '/*/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length':'212',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'www.excelsiormilano.com',
    'Origin':'https://www.excelsiormilano.com',
    'Referer':'https://www.excelsiormilano.com/content/31-yeezy',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }


# CHANGE the fields as the comments say
def main(limit):
    for i in range(1, limit):
        session = requests.Session()
        email = 'jade.jch+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'first_name': 'Jakrarat', # put your first name
            'last_name': 'Chunnananda', # put your last name
            'birth': '1997-02-16',  # YYYY-MM-DD
            'mail': email, # DO NOT CHANGE
            'size': '7 1/2',
            'country': 'Canada',
            'state': 'British Columbia',
            'city': 'Vancouver',
            'zip': 'V6B3A4',
            'street': '2406-788 Richards Street'
        }
        resp = session.post(url, data=payload, headers=headers)
        
        print('{}/{} registered'.format(i, limit) + " - successfully registered with email " + email + "\n")

if __name__ == "__main__":
    main(1000)
