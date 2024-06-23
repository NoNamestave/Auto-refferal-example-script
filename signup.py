import os
import random
import mechanize

# Remove cookie file if it exists
cookie_file = os.path.join(os.getcwd(), 'cookie.txt')
if os.path.exists(cookie_file):
    os.remove(cookie_file)

# Generate a random User-Agent string
def generate_user_agent():
    return f'Mozilla/5.0 (Windows NT {random.randint(11, 99)}.0; Win64; x64) AppleWebKit/{random.randint(111, 999)}.{random.randint(11, 99)} (KHTML, like Gecko) Chrome/{random.randint(11, 99)}.0.{random.randint(1111, 9999)}.{random.randint(111, 999)} Safari/{random.randint(111, 999)}.{random.randint(11, 99)}'

# Initialize mechanize browser
def init_browser():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    return br

# Set cookie jar
def set_cookie_jar(br):
    cj = mechanize.LWPCookieJar(cookie_file)
    br.set_cookiejar(cj)

# Function to make HTTP requests
def req(br, url, method='GET', headers=None, data=None):
    if headers:
        for header, value in headers.items():
            br.addheaders = [(header, value)]
    if method == 'POST':
        response = br.open(url, data)
    else:
        response = br.open(url)
    return response.read()

# Function to extract string between two substrings
def get_str(string, start, end):
    return string.split(start)[1].split(end)[0]

# Function to perform a single sign-up
def sign_up(refer, index):
    ua = generate_user_agent()
    br = init_browser()
    set_cookie_jar(br)

    url1 = "https://example.site/auth/signup"
    headers1 = {
        'Host': 'example.site',
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': f'https://example.site/?referral={refer}',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin'
    }

    response1 = req(br, url1, 'GET', headers1)
    token = get_str(response1.decode('utf-8'), "var token = '", "',")

    url2 = "https://example.site/auth/ajax_sign_up"
    headers2 = {
        'Host': 'example.site',
        'User-Agent': ua,
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://example.site',
        'Referer': 'https://example.site/auth/signup',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }

    payload = f'first_name=uutfutfv&last_name=hfyjrdrd&email=Ardjjrfcyj{random.randint(0, 99999)}328%40gmail.com&password=Ardjjrfcyj923765856328%40gmail.com&re_password=Ardjjrfcyj923765856328%40gmail.com&timezone=America%2FNew_York&referral={refer}&terms=on&token={token}'
    response2 = req(br, url2, 'POST', headers2, payload.encode('utf-8'))

    print(f"<b>Token {index}: </b>{token}<br>")
    print(f"<b>Response2 {index}: </b>{response2.decode('utf-8')}<br><br><br>")

# Main function to perform multiple sign-ups sequentially
def main(num_signups, refer):
    for i in range(num_signups):
        sign_up(refer, i)

# Number of sign-ups desired
num_signups = 10
refer = '75166543'  # Default referral code

if __name__ == "__main__":
    main(num_signups, refer)
    