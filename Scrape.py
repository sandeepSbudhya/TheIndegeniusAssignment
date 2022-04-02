from newsplease import NewsPlease
import pandas as pd

class Scrape:
    def __init__(self) -> None:
        pass

    def scrapeUrls(self,):
        count = 1
        articles = []
        with open("./data/urls/urls.txt","r") as f:
            for line in f:
                print(str(count)+line)
                article = NewsPlease.from_url(line.strip())
                article = {
                            "Title":article.title.replace('\n', ''),
                            "Content":article.maintext.replace('\n', '')
                            }
                articles.append(article)
                count+=1
        df = pd.DataFrame(articles)
        df.to_csv('./data/results/scrapeddata.csv', index=False)

