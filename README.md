# feedDiasp*
Feed Diaspora with RSS-Feeds or Facebook.
## Installation

`$ pip install feeddiasp`  

## Usage

    from feeddiasp import FeedDiasp, FBParser, RSSParser
    
    #Sync posts from a facebook site
    fb = FBParser(user='spiegelonline', auth_token='...')
    bot = FeedDiasp(parser=fb, pod='https://diasp.eu', username='zwirbel', password='Blume123', db='posts.txt')
    bot.publish()
    
    #Sync posts from a RSS feed
    rss = RSSParser(url='http://www.spiegel.de/schlagzeilen/index.rss')
    bot = FeedDiasp(parser=rss, pod='https://diasp.eu', username='zwirbel', password='Blume123', db='posts.txt')
    bot.publish()
    
To avoid duplicates, submitted posts will be stored in `posts.txt` (defined in `db`).

## Contributors
* ![Moritz Duchêne](https://github.com/Debakel)
* ![Alexey Veretennikov](https://github.com/fourier)

## License

[Gnu General Public License (GPL), Version 2 or later](https://www.gnu.org/licenses/gpl-2.0.html#SEC1)
