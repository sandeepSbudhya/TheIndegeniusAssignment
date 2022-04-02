from newsplease import NewsPlease
import pandas as pd
count = 1
articles = []
with open("./urls.txt","r") as f:
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
# print(df)

df.to_csv('scrapeddata.csv', index=False)

