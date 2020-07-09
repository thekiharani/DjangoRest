import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg5MTk4MTcxLCJqdGkiOiIyNDZkYmNlMDVlNDU0OTgwOTg3MjA0NjU4NWJlNzliMCIsInVzZXJfaWQiOjF9.kPv-Je4FLB9Xe34Pus7rPoJxRn2RUPmF9psSH-qOIg8'

r = requests.get('http://127.0.0.1:8000/api/paradigms/', headers=headers)
print(r.text)
