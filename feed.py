import requests
import xml.etree.ElementTree as ET

from feedparser import parse

feed = requests.get('http://www.wollens.top/all/rss/').text
url = 'http://www.wollens.top/all/rss/'
data=parse(url)
entries = data['entries'][:5]
for entry in entries:
    title = entry['title']
    url = entry['link'].replace('http://127.0.0.1:28001', 'http://www.wollens.top')

with open('README.md', 'w') as f:
    f.write(r'''
    _   _      _                                                                                      _
                      ___====-_  _-====___
            _--^^^#####//      \\#####^^^--_
         _-^##########// (    ) \\##########^-_
        -############//  |\^^/|  \\############-
      _/############//   (@::@)   \\############\_
     /#############((     \\//     ))#############\
    -###############\\    (oo)    //###############-
   -#################\\  / VV \  //#################-
  -###################\\/      \//###################-
 _#/|##########/\######(   /\   )######/\##########|\#_
 |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
 `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
    `   `  `      `   / | |  | | \   '      '  '   '
                     (  | |  | |  )
                    __\ | |  | | /__
                   (vvv(VVV)(VVV)vvv)

## Latest blog posts
''')
    f.write('- [{}]({})\n'.format(title, url))

    f.write('''
[🌆 My blog](http://www.wollens.top/blog)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=netcan)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=netcan&hide=ipynb,html&layout=compact)
''')