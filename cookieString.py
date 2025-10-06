
# Paste your cookie string here
cookie_string = "https://cdn.mediago.io/js/cookieSync.html?tn=41b6e88a2b85b0e731ef8e73e5558712"

# Dict to store cookies
cookies = {}

# Loop through each cookie
for cookie in cookie_string.split('; '):
    # Split cookie into name and value
    cookie_parts = cookie.split('=')
    cookies[cookie_parts[0]] = cookie_parts[1]
