from bs4 import BeautifulSoup

soup = BeautifulSoup(open("podcasts.html"), "html.parser")

titles = [t.text for t in soup.find_all("div", class_="title")]
urls = [u["href"] for u in soup.find_all("a", class_="feedcell")]
formatted_output = "\n".join(
    "[{0}]({1})  ".format(t, u) for t, u in zip(titles, urls))
print(formatted_output)
