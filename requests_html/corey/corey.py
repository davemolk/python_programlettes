from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://coreyms.com/')

# articles = r.html.find('article')
# for article in articles:
#     headline = article.find('.entry-title-link', first=True).text
#     print(headline)
#     # p tag within element w class of entry-content
#     summary = article.find('.entry-content p', first=True).text
#     print(summary)

#     try:
#         vid_src = article.find('iframe', first=True).attrs['src']
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except:
#         yt_link = None


# get links
# for link in r.html.links:
#     print(link)

for link in r.html.absolute_links:
    print(link)