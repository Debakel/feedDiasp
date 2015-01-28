# feedDiasp*
Feed Diaspora with RSS-Feeds or Facebook.
## Requirements

 * feedparser `pip install feedparser`
 * diaspy `pip install diaspy`

## Usage

    from FeedDiasp import FeedDiasp
    
    bot = FeedDiasp(feed_url='https://netzpolitik.org/feed', pod='https://diasp.eu', username='zwirbel', password='Blume123', db='posts.txt')
    bot.publish()


## License

[Gnu General Public License (GPL), Version 2 or later](https://www.gnu.org/licenses/gpl-2.0.html#SEC1)
