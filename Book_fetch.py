# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import cloudsight
from goodreads import client
import goodreads
import os
import sys
import re
import subprocess

from googlesearch import *

print("Welcome to the simple book-review tool")
print("--------------------------------------------")
print("Authentication for cloud services in progress")
gc = client.GoodreadsClient('YZGDbGQrMRAAygCAr8Z8tw', 'iH9xo6jhIkNEEHQ9a0nJopDPNEL0TLfq3Z2E2ZNgBDc')
result = requests.get("https://firebasestorage.googleapis.com/v0/b/book-finder-1f3de.appspot.com/o/image_0?alt=media&token=61ce6b03-fead-45fb-b875-71e869c3015c")


auth = cloudsight.SimpleAuth('nHo9nAczgUTzB6pLiCv1UA')
api = cloudsight.API(auth)
print("Authentication complete!!")

print("Your book is being recognised..")
response = api.remote_image_request('https://firebasestorage.googleapis.com/v0/b/book-finder-1f3de.appspot.com/o/image_0?alt=media&token=48e00dec-ffc4-494b-aa4c-5424cca5b9cc', {
    'image_request[locale]': 'en-US',
})

status = api.image_response(response['token'])
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    # Done!
    pass

status = api.wait(response['token'], timeout=30)

res = status['name']
print("Book recognition complete !!!!\n")

print("Querying the book id from Goodreads...\n")
res = "goodreads " + res 
results = []
print("url's queried so far:")
print("--------------------------\n")
for url in search(res, tld='us', lang='en', stop=5):
           print(url)
           results.append(url)
print("\n" + "Query complete")
book_id = ''

for result in results:
    if result[0:36] == "https://www.goodreads.com/book/show/":
        i = 36
        while result[i].isnumeric():
               book_id += result[i]
               i += 1;
        break
    else: continue

print("Book-ID Query Successful...!! \n\n")

book = gc.book(int(book_id))

print("Book Title :" + book.title +"\n")
print("----------------------------------------------------------")
print("Author :")
print( book.authors)
print("\n")
print("Released in : ")
print(book.publication_date)
print("\n")
print("ISBN : " + book.isbn)
print("ISBN13 : " + book.isbn13)
print("\n")
print("Description : ")
print(book.description)
print("\n")
print("Average user rating : " + book.average_rating)
print("Rating Distribution : " + book.rating_dist)
print("\n")
print("Similar Books: ")
print(book.similar_books)
print("\n\n\n")

'''
f = open("Book_review.txt", 'w')

f.write("Book Title :" + book.title +"\n")
f.write("----------------------------------------------------------")
f.write("Author :")
f.write(book.authors)
f.write("\n")
f.write("Released in : ")
f.write(book.publication_date)
f.write("\n")
f.write("ISBN : " + book.isbn + "\n")
f.write("Description : ")
f.write(book.description)
f.write("\n")
f.write("\n\n")

f.close()
'''
