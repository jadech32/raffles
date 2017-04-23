import requests
import sys
from random import getrandbits

url = 'https://app.bronto.com/public/webform/process'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '305',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'app.bronto.com',
    'Origin': 'https://app.bronto.com',
    'Referer': 'https://app.bronto.com/public/webform/render_form/az29kh7x0eyaepdiyjrpwnoaucqqy/8d8606e3ebfefedc32115d645e3832e7/addcontact',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def main(limit):

    for i in range(1,limit):
        email = 'jade.jch+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.

        form = {
            'fid': 'az29kh7x0eyaepdiyjrpwnoaucqqy',
            'sid': '8d8606e3ebfefedc32115d645e3832e7',
            'delid': '',
            'subid': '',
            'td': '',
            'formtype': 'addcontact',
            '90298[29288859]': 'Jakrarat',  # FIRST NAME
            '90299[29288860]': 'Chunnananda',  # LAST NAME
            '90300': email,  # EMAIL JIG
            '90301[29288866]': '8',  # SHOE SIZE
            '90302[29289136]': '',  # INSTAGRAM / OPTIONAL
            '90303[29289137]': 'Agree to Terms',  # DON'T CHANGE THIS
            '90307[899049]': 'true'
        }

        response = requests.post(url,data=form,headers=headers)
        print('{}/{} registered.'.format(i, limit) + ' You have entered using ' + email)
        print(response)


if __name__ == "__main__":
    #amount = input('How many times do you want to enter? Enter a number:')
    main(2)


