import requests
import pandas as pd


url = "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837"

results = []

for x in range(1, 5):
    querystring = {"":"","isProductNeeded":"true","pageSize":"100","responseFormat":"json","isChanelCategory":"false","currency":"USD","gclid":"Cj0KCQiAk4aOBhCTARIsAFWFP9GHb-HHlTtcWEbqNZGNwV0h-apJtRsxbX_GHTF_HUo3dm_nDS9rTmQaAp4pEALw_wcB","pageView":"image","DM_PersistentCookieCreated":"true","categoryId":"3074457345626651837","beginIndex":"0","cid":"PM-SGA_300419-3.US-SGH-EN-NB-Sunglasses_Sunglasses-Men-P_men+sunglasses","gclsrc":"aw.ds","viewTaskName":"CategoryDisplayView","catalogId":"20602","langId":"-1","storeId":"10152","top":"Y","orderBy":"default","currentPage":f"{x}"}

    headers = {"cookie": "aka-cc=US; aka-ct=DENVER; aka-zp=80201-80212%2B80214-80239%2B80241%2B80243-80244%2B80246-80252%2B80256-80257%2B80259-80266%2B80271%2B80273-80274%2B80279-80281%2B80290-80291%2B80293-80295%2B80299; ak_bmsc=00E8541210983C58521FA8C88A8F9B9D~000000000000000000000000000000~YAAQfQswFz%2Ft%2FNh9AQAAqRc24g7Qa14vE29dZIw4hBcOwMjy%2F3i7x9nADupjLM7GwMG5IqBvlE%2BhrD4urwYJk1uQ%2BfBu5gcw8ZloOb4cReIeGAUKd%2Fm2mRkTtWJUEhedAQz4YKmywTsBSPzfpxOcyjE2QJEJgs2GPlObbHDOs3%2FVpnnK1CK6%2FmvjraQQBldTbfOyfmavsAyxiAZf0GJJHyvf2DaVv%2FJAg4FCmjBQwRpHESB%2Fz1HCRJhYHxbZkmJ7KEC5MCcxmDeeYU5X7jx6nQFJK6SLDkR1tEv2u9zjk8iUpSqg%2BsBDLRTlbcvW61aED93K2ZxkqkIEkmtSUpihy4zVIGEZvQ3asJjAf2zYwoCxwMYU4TILboDkfGGdxIGGeAQnv0dvJglSOGFd2Rpl; bm_sv=BC314ACEB244B820A3BEB16E52FD9C73~FkMuWIkW1RW4a5g8ZztMcd2D6NLmshA8ZrIqULrdIDBPZQyE9trp%2BkFmcHU9P6hume1jBD%2Fkw6vTC94UPDtFOVMdLKzjXYQ7pfWjIhguFAYaMt4nKGQCtXOWycWu2F87VZg%2BV1b1qHbxYwoKte6WspNHoMhxIFM%2FsHN9uKlsqSw%3D; TS011f624f=015966d292a8fc7cdb515f45b15207998d9849238cf47e82131c359584c2b37cd82a7c8d9633b575631bd009c79506dc499e755c40"}

    r = requests.request("GET", url, headers=headers, params=querystring)
    data = r.json()
    for product in data['plpView']['products']['products']['product']:
        results.append(product)

df = pd.json_normalize(results)
df.to_csv('firstresults.csv')