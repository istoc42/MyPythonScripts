from bs4 import BeautifulSoup
import requests
# import lxml

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "lxml")

# all_anchor_tags = soup.find_all('a')
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# sec_heading = soup.find(name="h3", class_="heading")

# print(heading)
# print(sec_heading)

response = requests.get("https://news.ycombinator.com/")

print(response.text)