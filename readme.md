# wz-uniform-crawler
This is a simple crawler script for downloading images from [Uniform Map / 制服地圖](http://uniform.wingzero.tw/)

## Installation
Install from [PyPI](https://pypi.org/):

```
pip install wz-uniform-crawler
```

Install from [GitHub](https://github.com/):

```
pip install git+https://github.com/issaclin32/wz_uniform_crawler/
```


## Usage
```python

import wz_uniform_crawler

# download images according to page url
wz_uniform_crawler.fetch_by_url('https://uniform.wingzero.tw/school/intro/jr/198')

# download images with 20 parallel download threads (default = 10), without showing messages.
wz_uniform_crawler.fetch_by_url('https://uniform.wingzero.tw/school/intro/jr/198', num_of_parallel_downloads=20, verbose=False)

# download all images from Uniform Map
wz_uniform_crawler.fetch_all()

# download all images from Uniform Map tagged as type "jr"(Junior High Schools in Taiwan) and "tw" (High Schools in Taiwan)
# with 20 parallel download threads
wz_uniform_crawler.fetch_all(school_types=['jr', 'tw'], num_of_parallel_downloads=20)

```

## Disclaimer
This crawler script is only made on the purpose of personal programming practice. I do not own the copyright, nor have any affiliation with the maintainer of [Uniform Map](http://uniform.wingzero.tw/).