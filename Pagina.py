from urllib.parse import urlparse
from bs4 import BeautifulSoup
import cloudscraper

class Pagina:

    def __init__(self,url):
        self.Url=str(url);
    
    def GetPhotos(self):
        scraper = cloudscraper.create_scraper();
        page = scraper.get(self.Url).text;
        soup = BeautifulSoup(page, "html.parser");
        for photoStr in soup.find_all("figure","photo"):
            photo=BeautifulSoup(str(photoStr),"html.parser");
            yield '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self.Url))+ photo.find_all("img")[0]["src"];
