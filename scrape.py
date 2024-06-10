import requests
alphabets = ['A', 'B', 'D', 'E', 'E', 'F', 'G', 'GB', 'GH', 'H',
             'I', 'K', 'KH', 'KP', 'L', 'M', 'MW', 'N', 'O', 'O',
             'P', 'R', 'RH', 'RR', 'S', 'T', 'U', 'V', 'VB', 'W', 'Y', 'Z']

for i in alphabets[:1]:
    link = f'https://edofolks.com/edo-{i}/'
    contents = requests.get(link)