from requests_html import HTMLSession

s = HTMLSession()

query = 'denver'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})

# this returns a list, so use first=True to stop that
# finding the span with id wob_tm
temp = r.html.find('span#wob_tm', first=True).text

# replace spaces with a dot, chain the span below the div like so:
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text

desc = r.html.find('div.VQF4g span#wob_dc', first=True).text

# can also chain together like so
# print(r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)

print(query, temp, unit, desc)