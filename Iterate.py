# # import requests
# # from response import Response
# # response = requests.get('http://localhost:8000/UserDetails')
# # print(response.json())
# import os

# import sys
# # print(sys.path)

# path = 'c:\\Users\\Sourabh\\Fingerprints\\Fingerprints'
# if path not in sys.path:
#     sys.path.append(path)

# # print(sys.path)
# from Matcher.views import data
# os.environ['DJANGO_SETTINGS_MODULE'] = 'Fingerprits.settings'
# print(data)
import os
home = os.path.expanduser('~')
print(os.path.join(home, 'ssss'))