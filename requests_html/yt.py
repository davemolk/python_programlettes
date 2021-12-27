from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg/videos'

r = session.get(url)

# sleep at 1 or 2 usually works, scrolldown can get pretty high if necessary
r.html.render(sleep=1, keep_page=True, scrolldown=1)

videos = r.html.find('#video-title')

for item in videos:
    video = {
        'title': item.text,
        'link': item.absolute_links,
    }
    print(video)

