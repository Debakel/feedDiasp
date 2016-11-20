# feedDiasp*
Python 3 version of Feed Diaspora with RSS-Feeds or Facebook.

## Requirements

 * feedparser `pip3 install feedparser`
 * facepy `pip3 install facepy`
 * html2text `pip3 install html2text`
 * pypandoc `pip3 install pypandoc`
 * diaspy `git clone https://github.com/marekjm/diaspy.git /tmp/diaspy && cp -r /tmp/diaspy/diaspy $PYTHONPATH` (do not install with pip, the version in PyPI is not working.)

## Usage

    from FeedDiasp import FeedDiasp
    from FBParser import FBParser
    from RSSParser import RSSParser
    
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
* ![Céline Libéral](https://github.com/celisoft)

## License

[Gnu General Public License (GPL), Version 2 or later](https://www.gnu.org/licenses/gpl-2.0.html#SEC1)
