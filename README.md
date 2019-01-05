# feedDiasp*
Feed Diaspora with RSS-Feeds or Facebook.

## Requirements

`feedDiasp` requires Python 3 and the `pandoc` library (optional) for converting HTML into Markdown:
 * On Debian based distributions : `apt-get install pandoc`
 * On ArchLinux : `pacman -S pandoc`
 * On MacOS: `brew install pandoc`
  
## Installation
`$ pip install feeddiasp`  

## Usage example

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

## Running the tests

```
$ python -m unittest tests
```

To run the tests, login credentials for a diaspora account must be stored in the following environment variables:
* `FEEDDIASP_TEST_POD`
* `FEEDDIASP_TEST_USERNAME`
* `FEEDDIASP_TEST_PASSWORD`


## Contributors
* ![Moritz Duchêne](https://github.com/Debakel)
* ![Alexey Veretennikov](https://github.com/fourier)
* ![Céline Libéral](https://github.com/celisoft)

## License

[Gnu General Public License (GPL), Version 2 or later](https://www.gnu.org/licenses/gpl-2.0.html#SEC1)
