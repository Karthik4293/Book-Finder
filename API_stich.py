import firebase
from firebase import firebase

firebase = firebase.FirebaseApplication("gs://book-finder-1f3de.appspot.com")
result = firebase.get('image_0')
print(result)
