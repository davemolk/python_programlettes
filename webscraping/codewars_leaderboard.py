from requests_html import HTMLSession

session = HTMLSession()
url = "https://www.codewars.com/users/leaderboard"

r = session.get(url)
# rows = r.html.find('tr')
# for row in rows:
#     # print(row)
#     print(row.text)


# get usernames of top 500 on codewars leaderboard
names = r.html.find('.is-big a')
for name in names:
    print(name.text)
    