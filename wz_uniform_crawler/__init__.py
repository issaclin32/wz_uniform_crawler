import os
import re
import time
import urllib.request as req  # built-in for Python 3
from urllib.error import HTTPError

from bs4 import BeautifulSoup  # pip/beautifulsoup4


# May require update in the future
_USER_AGENT_HEADER = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'


def _init_header(verbose: bool = False) -> None:
    global FLAG_header_inited
    if 'FLAG_header_inited' not in globals():
        if verbose: print('using fake user-agent header: {_USER_AGENT_HEADER}')
        opener=req.build_opener()
        opener.addheaders=[('User-Agent', _USER_AGENT_HEADER)]
        req.install_opener(opener)
        FLAG_header_inited = True
    return


def fetch_pics(url: str, verbose: bool = True) -> None:
    match_results = re.findall(r'https?:\/\/uniform\.wingzero\.tw\/school\/(intro|album)\/([a-z]+)\/([0-9]+)([\/][0-9]+)?', url)
    
    if match_results is None:
        print('\nSorry. This URL is not supported.\nValid URL for this application should be like: http://uniform.wingzero.tw/school/album/twes/78\n')
        raise ValueError('URL not supported')
    
    
    school_type: str = match_results[0][1]
    school_id: int = int(match_results[0][2])
    url_prefix = f'http://uniform.wingzero.tw/school/album/{school_type}/{school_id}'
    
    _init_header(verbose=verbose)
    
    img_urls = []
    # Fetch page content
    for page_index in range(1, 10):
        if verbose: print(f'Opening {url_prefix}/{page_index}...')
        try:
            response = req.urlopen(f'{url_prefix}/{page_index}').read()
        except HTTPError as ex:
            print('An error happened when trying to read the webpage.\nThis is probably caused by network issue, or the "fake user-agent header" needs update.')
            raise HTTPError(ex)
        
        # Analyze the page with BeautifulSoup
        soup = BeautifulSoup(response, 'lxml')
        
        if page_index == 1:
            school_name = soup.find('h1', class_='h1_title').find(text=True, recursive=False).strip()
        
        img_elements = soup.find_all('img', class_='lazyload img-fluid')
        if len(img_elements) == 0:
            if verbose: print(f'No image found on {url_prefix}/{page_index}. \nStop fetching pages.')
            break
        img_urls.extend([e['data-src'] for e in img_elements])


    # Download images
    output_folder_name = f'{school_type}{school_id:04d}_{school_name}'
    
    if not os.path.isdir(output_folder_name):
        os.makedirs(output_folder_name, exist_ok=True)
    output_path = os.path.abspath(output_folder_name)
        
    for img_index, source in enumerate(img_urls):
        destination = output_path + '/' + source.split('/')[-1]  # use / instead of \\ for Windows+Linux compatibility
        if verbose: print(f'({img_index+1}/{len(img_urls)}) Downloading: {source} --> {destination}')
        
        for retry_count in range(1, 6):
            try:
                req.urlretrieve(source, destination)
            except HTTPError:
                print(f'Connection error. Wait for 10 seconds and retry({retry_count}/5)...')
                time.sleep(10)
            else:
                break
        else:  # this block will be executed if the for-loop is not "break"ed
            print('Retry limit reached. This image will be ignored.')
    return