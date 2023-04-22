import requests
from pandas import json_normalize
import pandas as pd
import time
import random
from bs4 import BeautifulSoup

# PHOTO SEARCH RESULTS
def image_search(query, page_limit=1, base_time=3, basic=True):
    """
    Extract search results based on a specific search query.
    Args:
        query (:obj:`str`, required): Search query
        limit (:obj:`int`, optional): Maximum results to extract.
        base_time (:obj:`str`, required): choose a number of seconds to generate sleep time between each request.
        base_time (:obj:`str`, required): True to return the simplified DataFrame, False to return all data.
    """
    frac = random.randint(1,17)
    delay = base_time/frac
    query_format = query.lower().replace(' ', '-')
    combine_df = []
    for i in range(1, page_limit+1):
        url = f'https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/search/{query_format}.json?image_type=photo&term={query_format}&page={str(i)}'
        response = ss_api_request(url).json()
        pages_num = response['pageProps']['meta']['pagination']['totalPages']
        if i == 1:
            print(f'Total result pages: {pages_num}')
        else:
            pass
        page_df = json_normalize(response['pageProps']['assets'])
        page_df['page_num'] = pages_num
        combine_df.append(page_df)
        time.sleep(delay)
    df = pd.concat(combine_df).reset_index(drop=True)
    simple_df = df[['id', 'title', 'description', 'aspect', 'isEditorial', 'src', 'link', 'width', 'height', 'channels', 'contentTier', 'contributorId', 
                               'sizes.hugeJpg.format', 'sizes.hugeJpg.dpi', 'sizes.hugeJpg.width', 'sizes.hugeJpg.height', 'sizes.hugeJpg.humanReadableSize', 
                               'sizes.hugeJpg.widthCm','sizes.hugeJpg.heightCm',
                               'meta.relatedKeywords', 'meta.query', 'modelReleaseInfo', 'meta.pagination.totalPages', 'meta.pagination.totalRecords']]
    if basic == True: # Return a shortened report with the most important columns
        return simple_df
    else:
        return df

def image_search_url(url):
    """
    Extract search results from the image search.
    Args:
        url (:obj:`str`, required): URL of the image search page. Eg: https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/search/ha-giang.json?image_type=photo&term=ha-giang
    """
    response = ss_api_request(url).json()
    df = json_normalize(response['pageProps']['assets'])
    return df


# VIDEO CREATIVE SEARCH
def video_search(query, page_limit=1, base_time=3, basic=True):
    """
    Extract search results based on a specific search query.
    Args:
        query (:obj:`str`, required): Search query
        limit (:obj:`int`, optional): Maximum results to extract.
        base_time (:obj:`str`, required): choose a number of seconds to generate sleep time between each request.
        base_time (:obj:`str`, required): True to return the simplified DataFrame, False to return all data.
    """
    frac = random.randint(0,17)
    delay = base_time/frac
    query_format = query.lower().replace(' ', '-')
    combine_df = []
    for i in range(1, page_limit+1):
        url = f'https://www.shutterstock.com/_next/data/qaf5FoOwtgZ0aXCZ3JlVY/en/_shutterstock/video/search/{query_format}.json?term={query_format}&page={str(i)}'
        response = ss_api_request(url).json()
        total_results = response['pageProps']['meta']['pagination']['total']
        results_per_page = response['pageProps']['meta']['pagination']['start']
        try:
            pages_num = total_results % results_per_page
            print(f'Total result pages: {pages_num}')
        except:
            pass
        page_df = json_normalize(response['pageProps']['videos'])
        combine_df.append(page_df)
        time.sleep(delay)
    df = pd.concat(combine_df).reset_index(drop=True)
    simple_df = df[['id', 'description', 'duration', 'aspectRatioCommon', 'previewImageUrl', 'modelReleaseInfo', 'isEditorial',
                    'uploadedDate', 'rRated', 'channels', 'categories', 'descriptionLanguageMap.en', 'previewVideoUrls.mp4',
                    'sizes.hdOriginal.height', 'sizes.hdOriginal.width', 'sizes.hdOriginal.fps', 'sizes.hdOriginal.format', 'sizes.hdOriginal.fileSize', 'sizes.hdOriginal.displayName',
                    'sizes.ultrahd4KOriginal.height', 'sizes.ultrahd4KOriginal.width', 'sizes.ultrahd4KOriginal.fps', 'sizes.ultrahd4KOriginal.format', 'sizes.ultrahd4KOriginal.fileSize', 'sizes.ultrahd4KOriginal.displayName',
                    'contributor.id', 'contributor.displayName', 'contributor.publicInformation.displayName', 'contributor.type', 
                    'contributor.publicInformation.accountsId', 'contributor.publicInformation.contributorId', 'contributor.publicInformation.bio',
                    'contributor.publicInformation.location',
                    'contributor.publicInformation.website',
                    'contributor.publicInformation.contributorTypeList',
                    'contributor.publicInformation.equipmentList',
                    'contributor.publicInformation.styleList',
                    'contributor.publicInformation.subjectMatterList',
                    'contributor.publicInformation.facebookUsername',
                    'contributor.publicInformation.storageKey',
                    'contributor.publicInformation.portfolioUrl',
                    'contributor.publicInformation.longBio',
                    'contributor.publicInformation.hasPublicSets',
                    'contributor.publicInformation.instagramUsername',
                    'contributor.publicInformation.instagramUrl',
                    'contributor.publicInformation.facebookUrl', 
                    'meta.query', 'meta.queryTranslations.en', 'meta.relatedTerms', 'modelReleaseInfo', 'isEditorial'
                    ]]
    if basic == True: # Return a shortened report with the most important columns
        return simple_df
    else:
        return df

def video_search_url(url):
    """
    Extract search results from the Video creative search.
    Args:
        url (:obj:`str`, required): URL of the video search page
    """
    response = ss_api_request(url).json()
    df = json_normalize(response['pageProps']['videos'])
    return df

# GET MEDIA DETAILS
## Photo
def bulk_photo_detail(search_df, limit=10, base_time=3):
    """
    Extract details of the target images list.
    Args:
        search_df (:obj:`str`, required): a DataFrame that returned from `image_search` function
        limit (:obj:`int`, optional): Maximum results to extract.
        base_time (:obj:`str`, required): choose a number of seconds to generate sleep time between each request.
    """
    frac = random.randint(1,17)
    delay = base_time/frac    
    search_df['slug'] = search_df['link'].apply(slug_extract)
    combine_df = []
    try:
        for i in range(limit):
            slug = search_df['slug'][i]
            url = f'https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/image-photo/{slug}.json?title={slug}'
            detail_df = photo_detail(url)
            combine_df.append(detail_df)
            time.sleep(delay)
    except:
        pass
    finally:
        df = pd.concat(combine_df).reset_index(drop=True)
    return df

def photo_detail(url):
    """
    Extract details info or a specific photo by its url.
    Args:
        url (:obj:`str`, required): URL of the photo detail page. Eg: https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/image-photo/ha-giang-province-northeast-vietnam-1575835303.json?title=ha-giang-province-northeast-vietnam-1575835303
    """
    response = ss_api_request(url).json()
    df = json_normalize(response['pageProps']['asset'])
    return df

## Video
def bulk_video_detail(video_df, limit=10, base_time=3):
    """
    Extract details of the target images list.
    Args:
        video_df (:obj:`str`, required): a DataFrame that returned from `video_search` function
        limit (:obj:`int`, optional): Maximum results to extract.
        base_time (:obj:`str`, required): choose a number of seconds to generate sleep time between each request.
    """
    frac = random.randint(1,17)
    delay = base_time/frac    
    combine_df = []
    try:
        for i in range(limit):
            video_id = video_df['id'][i]
            url = f'https://www.shutterstock.com/video/clip-{video_id}'
            response = ss_api_request(url)
            bs = BeautifulSoup(response.text, 'html.parser')
            video_link = bs.select('link[rel*=canonical]')[0]['href']
            slug = video_link.split('video/')[1]
            video_detail_url = f'https://www.shutterstock.com/_next/data/qaf5FoOwtgZ0aXCZ3JlVY/en/_shutterstock/video/{slug}.json?slug={slug}'
            video_detail_df = json_normalize(ss_api_request(video_detail_url).json()['pageProps']['asset'])
            combine_df.append(video_detail_df)
            time.sleep(delay)
    except:
        pass
    finally:
        df = pd.concat(combine_df).reset_index(drop=True)
    return df

def video_detail(url):
    """
    Extract details info or a specific video by its url.
    Args:
        url (:obj:`str`, required): url of the video detail page. Eg. https://www.shutterstock.com/_next/data/qaf5FoOwtgZ0aXCZ3JlVY/en/_shutterstock/video/clip-1027346687-gimbal-forward-temple-literature-hanoi-vietnam-ancient.json?slug=clip-1027346687-gimbal-forward-temple-literature-hanoi-vietnam-ancient
    """
    response = ss_api_request(url).json()
    return response

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
  response = requests.request("GET", url, headers=headers, data=payload)
  return response

def slug_extract(url_path):
    """Extract the url slug of image details page
    Args:
    url_path: (`str` required): Value from the `link` column that extracts from the search result page. Eg: `/image-photo/lanscape-view-ha-giang-province-vietnam-1542872723`
    """
    slug = url_path.split('/')[2]
    return slug