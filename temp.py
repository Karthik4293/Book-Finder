# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import cloudsight
from firebase import firebase
from goodreads import client
import goodreads
import os
import sys
import re
import subprocess
#import goodreads_api_client as gr

gc = client.GoodreadsClient('YZGDbGQrMRAAygCAr8Z8tw', 'iH9xo6jhIkNEEHQ9a0nJopDPNEL0TLfq3Z2E2ZNgBDc')
result = requests.get("https://firebasestorage.googleapis.com/v0/b/book-finder-1f3de.appspot.com/o/image_0?alt=media&token=61ce6b03-fead-45fb-b875-71e869c3015c")
print(result)

auth = cloudsight.SimpleAuth('cx6Xj2LioifuNFJc21_tbw')
api = cloudsight.API(auth)

response = api.remote_image_request('https://firebasestorage.googleapis.com/v0/b/book-finder-1f3de.appspot.com/o/image_0?alt=media&token=61ce6b03-fead-45fb-b875-71e869c3015c', {
    'image_request[locale]': 'en-US',
})

status = api.image_response(response['token'])
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    # Done!
    pass

status = api.wait(response['token'], timeout=30)
print(status)
res = status['name']

print(res)

fw = open("ls_load_file.txt", 'w')
fw.write(res)

fw.close()

#inter_rev = requests.get('https://www.goodreads.com/book/'+res)
#book = gc.book(res)
#result = book.description

#print(result)