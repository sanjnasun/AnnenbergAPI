from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta, timezone
from articleObject import ArticleObject


def scrape_articles() -> set[ArticleObject]:
    try:
        page_to_scrape = requests.get("https://www.uscannenbergmedia.com/allnews/")
        page_to_scrape.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return set()

    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    date_limit = datetime.now(timezone.utc) - timedelta(weeks=2)
    article_set = set()

    divs = soup.find_all('div', class_='list-item')

    for div in divs:
        a_tag = div.find('a', title=True)
        time_tag = div.find('time', class_="primary-font__PrimaryFontStyles-sc-o56yd5-0 itpAFg date story-date")
        img_tag = div.find('img', src=True)

        if a_tag and 'title' in a_tag.attrs and 'href' in a_tag.attrs and time_tag and 'datetime' in time_tag.attrs:
            title = a_tag['title']
            link = a_tag['href']
            datetime_value = time_tag['datetime']
            time_text = time_tag.get_text()

            image_url = img_tag['src'] if img_tag else "Image URL not found"
            article_date = datetime.fromisoformat(datetime_value.replace('Z', '+00:00'))

            if article_date > date_limit:
                article = ArticleObject(title, f"https://www.uscannenbergmedia.com{link}", time_text, image_url)
                article_set.add(article)

    return article_set
