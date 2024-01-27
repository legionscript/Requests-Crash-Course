# pip install requests
import requests

"""
1. Basic Response
"""
get_response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(help(get_response))
# print(get_response.status_code)
# print(get_response.json())
# print(get_response.text)


"""
2. POST with body and headers
"""
body = {
    'userId': '1',
    'title': 'Test Todo',
    'completed': False
}

headers = {
    'Content-Type': 'application/json'
}

post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=body, headers=headers)
# print(post_response.json())


# Do we have a successful response?
# if post_response.ok:
#     print('success!')
# else:
#     print('failure!')

"""
3. URL Params
"""
params = {
    'userId': '1'
}

filter_response = requests.get('https://jsonplaceholder.typicode.com/todos', params=params)
# print(filter_response.json())

"""
4. Basic Auth
"""
auth = ('testuser', 'password')

basic_auth_response = requests.get('https://httpbin.org/basic-auth/testuser/password', auth=auth)
# print(basic_auth_response)


"""
5. Bearer Auth
"""
headers = {
    'Authorization': 'Bearer 1234567'   
}

bearer_auth_response = requests.get('https://httpbin.org/bearer', headers=headers)
# print(bearer_auth_response)

"""
6. Some Common Status Codes
"""
# # 200 - OK
# ok = requests.get('https://httpbin.org/status/200')
# print(ok)

# # 400 - Bad Request
# bad_request = requests.get('https://httpbin.org/status/400')
# print(bad_request)

# # 401 - Unauthorized
# unauthorized = requests.get('https://httpbin.org/basic-auth/testuser/password')
# print(unauthorized)

# # 403 - Forbidden
# forbidden = requests.get('https://httpbin.org/status/403')
# print(forbidden)

# # 404 - Not Found
# not_found = requests.get('https://jsonplaceholder.typicode.com/todo')
# print(not_found)

# # 500 - Server Errors
# server_error = requests.get('https://httpbin.org/status/500')
# print(server_error)


"""
7. Timeout and Try/Except
"""
try:
    timeout_response = requests.get('https://httpbin.org/delay/5', timeout=2)
    print(timeout_response)
except requests.exceptions.Timeout as e:
    print('timed out: ', e)