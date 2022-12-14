# shutterstock_analysis
> The internet's first python package supports analyzing the Shutterstock public data, which helps creators optimize their creative portfolio and earn more income with less effort.

`shutterstock_analysis` relies on public APIs, similar to how you use the web browser to access Shutterstock service to provide you the underlay insights. It is **FREE** and has **NO LIMITATIONS**. 

You can support this project on Patreon (or Momo in Vietnam) based on how you feel it is helpful. Scroll the end of this page for more details.

<div>
  <img src="https://img.shields.io/pypi/pyversions/shutterstock_analysis?logoColor=brown&style=plastic" alt= "Version"/>
  <img src="https://img.shields.io/pypi/dm/shutterstock_analysis" alt="Download Badge"/>
  <img src="https://img.shields.io/github/last-commit/thinh-vu/shutterstock_analysis" alt="Commit Badge"/>
  <img src="https://img.shields.io/github/license/thinh-vu/shutterstock_analysis?color=red" alt="License Badge"/>
</div>

---

# II. REFERENCES
## 2.1. How to use this package?
- Install the stable version: `pip install shutterstock_analysis`
- You can install the latest `shutterstock_analysis` version from source with the following command:
`pip install git+https://github.com/thinh-vu/shutterstock_analysis.git@main`

_(*) You might need to insert a `!` before your command when running terminal commands on Google Colab._

- To start using functions, you need to import them: `from shutterstock_analysis import *`

## 2.2. Function references

> You can also read the function suggestion on your IDE which loads the documentation from the doc string. It's fairly simple, trust me!

### 2.2.1. Image search
- Get image search results from multiple Shutterstock result pages:
  
   `search_df = image_search('ha giang', page_limit=10)`

- Get bulk photos details:

  `bulk_photo_detail = bulk_photo_detail(search_df, limit=100)`

### 2.2.2. Creative video search
> Although the data for the Editorial video is available, I decided to skip that option since it's not practical for my use case. Do feel free to develop it on your own if it's needed.

- Get video search results from multiple Shutterstock result pages:
  
  `search_df = image_search('ha giang', page_limit=10)`

- Get bulk videos details:
  
  `bulk_photo_detail = bulk_photo_detail(search_df, limit=100)`

### 2.2.3. Export data:
- This is the simplest way to export data from python to a CSV file which you can analyze easily either with Excel or Google Sheets.
  - Export search results: `search_df.to_csv('YOUR_PATH_TO_FILE.csv', index=False)`

  - Export photo details: `bulk_photo_detail.to_csv('YOUR_PATH_TO_FILE.csv', index=False)`

## Limitations
- Support photo and video searches: 
  - Photo Search (Non-Editorial and Editorial)
  - Video Creative Search. Skip Editorial Video search.

- Need to avoid abusing the API, which might lead to the service provider blocking the bot traffic.

# III. APENDICES

## Photo search query structure:
  <details>
    <summary>Default photo search</summary>

  ```https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/search/ha-giang.json?image_type=photo&term=ha-giang```

  Default Search UI:

  ![default_search](https://raw.githubusercontent.com/thinh-vu/shutterstock_analysis/main/src/shutter_stock_default_photo_search_ui.png)

  </details>

  <details>
    <summary>Advanced photo search</summary>

  ```https://www.shutterstock.com/_next/data/abgKsgPYfFDoIqIr0JlX0/en/_shutterstock/search/ha-giang.json?image_type=photo&term=ha-giang&page=2&&contributor=Big+Pearl&category=Nature&sort=newest&release=editorial&mreleased=true&exclude=car%2C+bike&artistsInclude=VN&authentic=true```

  Advanced Search UI

  ![advanced_search](https://raw.githubusercontent.com/thinh-vu/shutterstock_analysis/main/src/shutter_stock_advanced_photo_search_ui.png)
      
  </details>

## Video creative search query structure
<details>
  <summary>Default Video search</summary>
  
  ```https://www.shutterstock.com/_next/data/qaf5FoOwtgZ0aXCZ3JlVY/en/_shutterstock/video/search/ha-giang.json?term=ha-giang```

</details>

<details>
  <summary>Advanced Video Creative search</summary>
  
  ```https://www.shutterstock.com/_next/data/qaf5FoOwtgZ0aXCZ3JlVY/en/_shutterstock/video/search/ha-giang.json?term=ha-giang&page=2&sort=newest&res=4k&aspect_ratio=16%3A9&duration=0-90&fps=30&mreleased=true&people_number=2&contributor=bui+minh+vu&artistsInclude=VN&exclude=car%2C+bike&release=editorial&category=Nature&safe=off```

</details>

# IV. 🙋‍♂️ CONTACT INFORMATION
You can contact me at one of my social network profiles:

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/thinh-vu">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.messenger.com/t/mr.thinh.ueh">
    <img src="https://img.shields.io/badge/Messenger-00B2FF?style=for-the-badge&logo=messenger&logoColor=white" alt="Messenger Badge"/>
  <a href="https://www.youtube.com/channel/UCYgG-bmk92OhYsP20TS0MbQ">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  </a>
    <a href="https://github.com/thinh-vu">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Github Badge"/>
  </a>
</div>

---

If you want to support my open-source projects, you can "buy me a coffee" via [Patreon](https://patreon.com/thinhvu?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator) or Momo e-wallet (VN). Your support will help to maintain my blog hosting fee & to develop high-quality content.

![momo-qr](https://github.com/thinh-vu/vnstock/blob/main/src/momo-qr-thinhvu.jpeg?raw=true)