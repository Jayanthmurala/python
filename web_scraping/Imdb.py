import requests
from bs4 import BeautifulSoup
import pandas

# Define the URL you want to scrape
url = "https://www.imdb.com/interest/in0000030/?ref_=ints_cat_3_in_i_5"

# Add headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

# Make the request with headers
response = requests.get(url, headers=headers)

# Check the response status
# print(response)

# If the request is successful, proceed with parsing the content
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())  # Print the parsed HTML for inspection

    """"Collection-Data"""

    titles=soup.find_all("span",attrs={"data-testid":"title"})
    tl=[]
    for i in titles[:30]:
        tl.append(i.get_text())
    # print(tl)

    rating = soup.find_all("span",attrs={"class":"ipc-rating-star--rating"})
    rl=[]
    for r in rating[:30]:
        rl.append("⭐ "+r.get_text())
    # print(rl)
    trailer= soup.find_all("a",attrs={"aria-label":"Trailer"})
    tr=[]
    for t in trailer[:30]:
        tr.append("https://www.imdb.com/"+t['href'])
    # print(tr)
    title_links=soup.find_all('a',{"class":"ipc-lockup-overlay ipc-focusable"})
    tLink=[]
    for link in title_links[:30]:
        tLink.append("https://www.imdb.com/"+t['href'])
    # print(tLink)
    Data={"titles":pandas.Series(tl),
    "rating":pandas.Series(rl),
    "trailer":pandas.Series(tr),
    "title_links":pandas.Series(tLink)
    }
    pandas.DataFrame(Data).to_csv("IMDB.csv")

else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
   
