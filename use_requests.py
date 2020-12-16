import requests

try:
    response = requests.get('https://detik.com')
    if response.status_code == 200 :
        print( f" URL founded {response}")
        print( f" Teh content is {response.text}")
        print(response.status_code)
    else:
        print(f'Oops, ada kesalahan requests {response.status_code}')

except Exception as e:
    print( 'There is an Error', e )
print( 'Program Ended' )
