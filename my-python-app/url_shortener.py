from pyshorteners import Shortener

ACCESS_TOKEN = "98b0cd92f11b961378183b5fcaf1d4f07c6c3bc2"

long_url = input()
url_shortener = Shortener(domain="bit.ly", api_key=ACCESS_TOKEN)
print("short url is: {}", format(url_shortener.bitly.short(long_url)))