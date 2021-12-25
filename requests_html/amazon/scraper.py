from requests_html import HTMLSession
import json
import time


class Reviews:
    def __init__(self, asin):
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        self.url = f'https://www.amazon.com/Razor-Kick-Scooter-Kids-Lightweight/product-reviews/{self.asin}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber='


    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        print(r.html.html)
        if not r.html.find('div[data-hook=review]'):
            return False
        else:
            return r.html.find('div[data-hook=review]')
        
    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook=review-title]', first=True).text
            rating = review.find('i[data-hook=review-star-rating] span', first=True).text
            body = review.find('span[data-hook=review-body] span', first=True).text.replace('\n', '').strip()

            data = {
                'title': title,
                'rating': rating,
                'body': body[:100],
            }
            total.append(data)
        return total

    def save(self, results):
        with open(self.asin + '-reviews.json', 'w') as f:
            json.dump(results, f)


if __name__ == '__main__':
    amz = Reviews('B08WNV9WSJ')
    results = []
    for x in range(1, 3):
        print('getting page ', x)
        time.sleep(0.7)
        reviews = amz.pagination(x)
        if reviews is not False:
            results.append(amz.parse(reviews))
        else:
            print('no more pages')
            break


    amz.save(results)


'''
needed a vpn to get around bot-detection...
'''