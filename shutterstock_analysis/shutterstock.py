import requests
from pandas import json_normalize
import pandas as pd
import time
import random

# PHOTO SEARCH RESULTS
def search_results(query, page_limit=1, base_time=3):
    frac = random.randint(0,17)
    delay = base_time/frac
    query_format = query.lower().replace(' ', '-')
    combine_df = []
    for i in range(1, page_limit+1):
        url = f'https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/search/ha-giang.json?image_type=photo&term={query_format}&page={str(i)}'
        response = ss_api_request(url)
        page_df = json_normalize(response['pageProps']['assets'])
        combine_df.append(page_df)
        time.sleep(delay)
    df = pd.concat(combine_df).reset_index(drop=True)
    return df

def ss_search_url(url):
    response = ss_api_request(url)
    df = json_normalize(response['pageProps']['assets'])
    return df

# GET PHOTO DETAILS
def bulk_photo_detail(search_df, limit=10, base_time=3):
    frac = random.randint(0,17)
    delay = base_time/frac    
    search_df['slug'] = search_df['link'].apply(slug_extract)
    combine_df = []
    for i in range(limit):
        slug = search_df['slug'][i]
        url = f'https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/image-photo/{slug}.json?title={slug}'
        detail_df = photo_detail(url)
        combine_df.append(detail_df)
        time.sleep(delay)
    df = pd.concat(combine_df)
    return df

def photo_detail(url):
    response = ss_api_request(url)
    df = json_normalize(response['pageProps']['asset'])
    return df

# CONFIG
def ss_api_request(url, cookie=''):
  payload={}
  if cookie == '':
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-platform': 'macOS',
        "sec-fetch-site": "same-origin",
        "authority": "www.shutterstock.com"
    }
  else:
    headers = {
        "Cookie": f"{cookie}",
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-platform': 'macOS',
        "sec-fetch-site": "same-origin",
        "authority": "www.shutterstock.com"
    }
  response = requests.request("GET", url, headers=headers, data=payload).json()
  return response

def slug_extract(url_path):
    """Extract the url slug of image details page
    Args:
    url_path: (`str` required): Value from the `link` column that extracts from the search result page. Eg: `/image-photo/lanscape-view-ha-giang-province-vietnam-1542872723`
    """
    slug = url_path.split('/')[2]
    return slug