# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------
import sys
import os
import re
import json
import gc
import cookielib
import logging
import platform

resourceDir = "resources"
fileName =  os.path.basename(__file__)
sys.path.insert(0, __file__.replace(fileName, resourceDir))

import mechanize
import bs4

import time
from time import gmtime, strftime
from time import sleep
import MySQLdb


# User defined vars
#----------------------------------------------------------------------------------------
# Netflix email and password
username = 'guclutalu@smartup.network'
password = 'Smartnet9291'

# where to store collected shows
sourceDir = 'C:\Python27\Scripts\crawlers'

# globals
#----------------------------------------------------------------------------------------

netflixLogin = 'https://www.netflix.com/tr-en/login'
netflixHome  = 'http://www.netflix.com/browse'
httpBase     = 'http://www.netflix.com'
mediaHttp    = '%s/WiMovie' % httpBase
seasonHttp   = mediaHttp + '/%(titleid)s?actionMethod=seasonDetails&seasonId=' \
                           '%(seasonID)s&seasonKind=ELECTRONIC'
showAPI      = 'http://api-global.netflix.com/desktop/odp/episodes?video='     \
               '%(titleid)s&country=US&languages=en-US&routing=redirect'
movieAPI     = "http://www.netflix.com/api/shakti/%(identifier)s/bob?titleid=" \
               "%(titleid)s&trackid=%(trackId)s"
videoURL     = "http://www.netflix.com/WiPlayer?movieid=%(episodeId)s&trkid="  \
               "%(trackId)s"

resourcePath = os.path.normpath(os.path.join(os.path.split(__file__)[:-1][0], 'resources'))

# enumerations
#----------------------------------------------------------------------------------------

kCategoryName = 0
kGenre        = 1
kCategoryURL  = 1
kGenreURL     = 2

# objects
#----------------------------------------------------------------------------------------



class Categories(object): pass
class Genres(object): pass

class NetflixCollector(object):

    ID_REGEX    = re.compile(r"BUILD_IDENTIFIER[\'\"]:[\'\"]([a-zA-Z0-9]*)")
    CLEAN_REGEX = re.compile(r"[^a-zA-Z0-9'&! _-]")
    RETRIES     = 3

    LOGGER      = logging.getLogger('NetflixCrawler')
    LOGGER.setLevel(logging.INFO)
    CH = logging.StreamHandler()
    CH.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] : %(message)s')
    CH.setFormatter(formatter)
    LOGGER.addHandler(CH)

    def __init__(self):
        self.browser    = mechanize.Browser()
        self.cj         = cookielib.LWPCookieJar()
        self.categories = {}
        self.mediaInfo  = {}
        self.identifier = ''
        self.sourceDir  = sourceDir if sourceDir else self.defaultSourceDir()

    # Main App crawler
    def collectNetflix(self):
        self.LOGGER.info("Starting crawl")
        self.login()
        homePage = self.readURL(netflixHome)
        self.getCategories(homePage)
        self.collectIdentifier()
        self.browseGenres()
        self.collectMedia()

    def browserOptions(self):
        self.LOGGER.info("Setting Browser")
        self.browser.set_cookiejar(self.cj)
        self.browser.set_handle_equiv(True)
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(True)
        self.browser.set_handle_robots(False)
        self.browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self.browser.addheaders = [('user-agent',
                                    ' Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) '
                                    ' Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
                                   ('accept',
                                    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
        self.browser.addheaders.append(("Accept-Language", "en-us,en"))

    # Login to netflix
    def login(self):
        self.LOGGER.info("Loggin in")
        self.browserOptions()
        self.browser.open(netflixLogin)
        self.browser.form = list(self.browser.forms())[0]
        if self.browser.form:
            self.browser['email']    = username
            self.browser['password'] = password
            self.browser.submit()

    #------------------------------------------------------------------------------------
    # html parsing methods
    #------------------------------------------------------------------------------------

    def collectIdentifier(self):
        self.LOGGER.info("Collecting identifier")
        key     = self.categories.keys()[0]
        soup    = self.readURL(self.categories[key].href)
        scripts = "".join([str(x) for x in soup.findAll('script')])
        id      = re.search(self.ID_REGEX, scripts)
        if id:
            self.identifier = id.group(1)
            self.LOGGER.info("Collected identifier: %s" % self.identifier)
        else:
            self.LOGGER.critical("Identifier not found. Exiting.")
            raise Exception("Unable to get indentifier. Cannot crawl netflix without it. TRY AGAIN!")

    # collect browse categories
    def getCategories(self, soup):
        self.LOGGER.info("Collecting Categories")
        for flixTitle in soup.findAll("ol", {"class": "navigation-menu-genres"}):
            for browse in flixTitle.findAll('li'):
                #sectionTitle = browse.find('a')
                sectionTitle = browse
                #if sectionTitle and self.notSubNav(browse):
                if sectionTitle:
                    self.LOGGER.info("Collected: %s %s" % (sectionTitle.string,
                                                            sectionTitle['data-href']))
                    self.categories[sectionTitle.string] = Categories()
                    self.categories[sectionTitle.string].href = sectionTitle['data-href']


    def browseGenres(self):
        self.LOGGER.info("Collecting Genres")
        for name, category in self.categories.iteritems():
            category.genres = {}
            soup     = self.readURL(category.href)
            try:
                genreDiv = soup.find("div", {"class": "lomo"})
                for genre in genreDiv.findAll('a'):
                    sectionTitle = genre.find('span',{"class":"watch-page-link-title"})
                    imgSrc = genre.find('div',{"class":"title-boxart"})
                    imgArtArr = re.findall('url\((.*?)\)', imgSrc["style"])
                    imgArt = imgArtArr[0]
                    #print imgArt
                    #exit()
                    year = genre.find('span',{"class":"watch-page-link-year"}).text
                    #print imgArt
                    if sectionTitle:
                        category.genres[sectionTitle.string] = Genres()
                        category.genres[sectionTitle.string].href = sectionTitle['data-href']
                        category.genres[sectionTitle.string].art = imgArt
                        category.genres[sectionTitle.string].year = year
                        self.LOGGER.info("Adding to %s: %s" % (name, sectionTitle.string))
            except AttributeError, e:
                self.LOGGER.error("Unable to collect a genre for: %(name)s \n %(e)s" % locals())
                continue

    def collectMedia(self):
        self.LOGGER.info("Collecting Media")
        
        #Mysql connection
        db = MySQLdb.connect(host="localhost",user="root",passwd="N166i124Mbh",db="movies_scrap_new",charset='utf8')
        cur = db.cursor()

        for categoryTitle, category in self.categories.iteritems():
            
            for genreTitle, genreMedia in category.genres.iteritems():

                Movie_title = genreTitle.encode('ascii', 'ignore')
                #print Movie_title

                Thumb_urls  = genreMedia.art
                Video_urls  = 'https://www.netflix.com'+genreMedia.href
                Release_year =  genreMedia.year+'-01-01'
                Vendor_id = 3
                created_date = time.strftime("%Y-%m-%d %H:%M:%S")

                cur.execute("""SELECT auto_id FROM tbl_movies WHERE title LIKE %s""", [Movie_title])
                movie_set = cur.fetchall()
                if(movie_set):
                    for row in movie_set:
                        movie_id = row[0]
                        sql = "SELECT auto_id FROM tbl_prices WHERE movie_id = %s AND vendor_id = %s"% (movie_id,Vendor_id) 
                        cur.execute(sql)
                        price_set = cur.fetchall()
                        if(price_set):
                            pass
                            #cur.execute ("UPDATE tbl_prices SET video_url=%s, unique_id=%s, Rent_sd_price=%s, Rent_hd_price=%s, Buy_sd_price=%s, Buy_hd_price=%s, updated_date=%s  WHERE movie_id=%s AND vendor_id=%s", (Video_urls,'0',0,0,0,0,'1',created_date,movie_id,Vendor_id))
                            #cur.execute ("UPDATE tbl_prices SET video_url='%s', unique_id='%s', Rent_sd_price='%s', Rent_hd_price='%s', Buy_sd_price='%s', Buy_hd_price='%s', updated_date='%s'  WHERE movie_id='%s' AND vendor_id='%s'", (Video_urls,'0','0','0','0','0','1',created_date,movie_id,Vendor_id))
                            #print cur._last_executed
                        else:
                            insert_sql = "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,is_subscribe,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cur.execute(insert_sql,(movie_id,Video_urls,'0',Vendor_id,0,0,0,0,'1',created_date,created_date))
                else:
                    ##Inserting into movies table
                    if(Movie_title): 
                        insert_sql1 =  "INSERT INTO tbl_movies (title,thumbnail_url,release_year) VALUES(%s,%s,%s)"
                        cur.execute(insert_sql1,(Movie_title,Thumb_urls,Release_year))
                        movie_id    = cur.lastrowid
                        ##Inserting into prices table (need to update but_price,buyhd_price)
                        insert_sql2 =  "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,is_subscribe,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cur.execute(insert_sql2,(movie_id,Video_urls,'0',Vendor_id,0,0,0,0,'1',created_date,created_date))

                db.commit()
                  

    #------------------------------------------------------------------------------------
    # Utilities
    #------------------------------------------------------------------------------------
    def createNFO(self, savePath, mediaType):
        nfoFile = 'showNFO.xml' if mediaType == 'show' else 'movieNFO.xml'
        NFO = os.path.join(resourcePath, 'templates', nfoFile)
        with open(NFO, 'rU') as f:
            NFO = str(f.read())
        NFO %= self.mediaInfo
        self.saveMedia(NFO, savePath, 'nfo')

    def openURL(self, url):
        try:
            return self.browser.open(url)
        except Exception:
            print 'sleeping for 8 seconds'
            self.RETRIES -= 1
            if self.RETRIES <= 0:
                self.RETRIES = 3
                return False
            sleep(8)
            return self.browser.open(url)

    def readURL(self, url):
        self.LOGGER.info("Reading webpage into memory: %s" % url)
        res = self.openURL(url)
        res = res.read().replace('\\', '')
        return bs4.BeautifulSoup(res,"lxml")

    def createDir(self, category=None, genre=None, path=None):
        if path:
            if not os.path.exists(path):
                self.LOGGER.info("Creating directory: %s" % path)
                os.makedirs(path)
        else:
            category = self.cleanText(category)
            genre = self.cleanText(genre)
            dirTree = os.path.join(self.sourceDir, category, genre)
            if not os.path.exists(dirTree):
                self.LOGGER.info("Creating directory: %s" % dirTree)
                os.makedirs(dirTree)
            return dirTree

    def cleanText(self, dirtyText):
        return re.sub(self.CLEAN_REGEX, r"", dirtyText)

    @staticmethod
    def defaultSourceDir():
        windowsDir = r'C:\Users\Public\XBMC'
        unixDir    = r'~/XBMC'
        if 'windows' in platform.platform().lower():
            return windowsDir
        return unixDir

    @staticmethod
    def saveMedia(data, path, ext):
        media = '.'.join([path, ext])
        with open(media, 'w') as f:
            f.write(data.encode('ascii', 'ignore'))

    @staticmethod
    def notSubNav(browse):
        """Is category a class of subnav-tabs"""
        try:
            _ = browse.parent['class']
            return False
        except KeyError:
            return True

test = NetflixCollector()
test.collectNetflix()
