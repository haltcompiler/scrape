#!/usr/bin/python

from bs4 import BeautifulSoup as parser
import requests as r
import string
import time
import re

s = r.Session()

headers = {
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
#  'X-Requested-With' : 'XMLHttpRequest',
#  'Accept' : 'application/json, text/javascript, */*;'
}

cookies = {
}

def get_page(url):
  global headers, cookies
  try:
    resp = s.get(url, headers=headers, cookies=cookies)
  except r.exceptions.Timeout:
    print '[!] Time out occured on {}'.format(target)
    print '[!] Trying again {} with delay {}'.format(target, 1)

  except r.exceptions.TooManyRedirects:
    print '[-] Too many redirects on {}. Terminating !!'.format(target)
      
  except r.exceptions.RequestException as e:
    print '[-] Bad Request. Termination reason {}'.format(e)
  except r.exceptions.HTTPError as err:
    print '[-]  Does not exist !!'
  
if __name__ == '__main__':
  get_page()
