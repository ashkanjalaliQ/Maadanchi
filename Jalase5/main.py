from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd  

def divider_tag(tag):
    tag = tag[tag.find('>') + 1:tag.find('</')]
    if len(tag) == 0:
        tag = '-'
    return tag

def attach(names):
    result = ''
    if len(names) != 1:
        for i in range(len(names)):
            if i != len(names) - 1:
                result += names[i] + ', '
            else:
                return result + names[i]
    return names[0]
        

def scraping(website):
    html = urlopen(website)
    bs = BeautifulSoup(html, "html.parser")


    data = {
            'Game Name' : '',
            'Score' : '',
            'Published date' : '',
            'author' : '',
            'Vote' : '',
            'Number of Players' : '',
            'Age range' : '',
            'Game time' : '',
            'Favorite' : '',
            'Want it' : '',
            'Own it' : '',
            'Follow' : '',
            'Played it' : '',
            'Heart it' : ''
            
    }
    data['Game Name'] = divider_tag(str(bs.findAll('h1')))
    data['Score'] = divider_tag(str(bs.findAll('span', {'class' : 'average'})))
    
    
    data['Published date'] = str(bs.findAll('div', {'class' : 'meta'}))[:str(bs.findAll('div', {'class' : 'meta'})).find('<div class="game-tags">')].strip().split(':')[-1]
        
    author = bs.findAll('a', {'rel' : 'tag'})
    author_name = []
    for i in range(len(author)):
        if 'https://boardgaming.com/publishers/' in str(author[i].attrs['href']):
            author_name.append(divider_tag(str(author[i])))
    data['author'] = attach(author_name)
    data['Vote'] = divider_tag(str(bs.findAll('div', {'class' : 'votes'})))
    data['Number of Players'] = divider_tag(str(bs.findAll('div', {'id' : 'detail-icon-players'})))
    data['Age range'] = divider_tag(str(bs.findAll('div', {'id' : 'detail-icon-age'})))
    data['Game time'] = divider_tag(str(bs.findAll('div', {'id' : 'detail-icon-time'})))
    other_info = str(bs.findAll('span', {'class' : 'stat'})).split(',')
    data['Own it'] = divider_tag(other_info[0])
    data['Want it'] = divider_tag(other_info[1])
    data['Favorite'] = divider_tag(other_info[2])
    data['Heart it'] = divider_tag(other_info[3])
    data['Played it'] = divider_tag(other_info[4])
    data['Follow'] = divider_tag(other_info[5])
    
    return data
    
def Link_extractor(page_link):
    html = urlopen(page_link)
    bs = BeautifulSoup(html, "html.parser")
    
    link = bs.findAll('a')
    links = []
    
    for i in range(len(link)):
        #link[i] = str(link[i])
        if 'boardgaming.com/games/card-games/' in str(link[i]) or 'boardgaming.com/games/board-games/' in str(link[i]) or 'boardgaming.com/games/' in str(link[i]):
            if 'href' in str(link[i]) and 'title' in str(link[i]):
                if not 'class' in str(link[i]) and not 'img' in str(link[i]):
                    links.append(link[i].attrs['href'])
                    #print(link[i].attrs['href'])
        
    return links
html = urlopen('https://boardgaming.com/category/games/board-games')
bs = BeautifulSoup(html, "html.parser")
pages = int(str(bs.findAll('div', {'class' : 'pagination'}))[str(bs.findAll('div', {'class' : 'pagination'})).find('Page 1 of') + 10 : str(bs.findAll('div', {'class' : 'pagination'})).find('Page 1 of') + 13])
print(str(pages) + ' Pages')
info = [
        ['Game Name'],
        ['Score'],
        ['Published date'],
        ['author'],
        ['Vote'],
        ['Number of Players'],
        ['Age range'],
        ['Game time'],
        ['Own it'],
        ['Want it'],
        ['Favorite'],
        ['Heart it'],
        ['Played it'],
        ['Follow']
]
for i in range(28,29):
    links = Link_extractor('https://boardgaming.com/category/games/board-games/page/' + str(i + 1))
    print('Page ' + str(i + 1) + ' Started')
    for link in links:
        link_data = scraping(link)
        for j in range(len(info)):
            info[j].append(link_data[info[j][0]])
        #print(info)
    print('Page ' + str(i + 1) + ' Completed!')
    #print(info)

for i in range(len(info)):
    info[i] = info[i][1:]

data = {'Game Name': info[0],
        'Score': info[1], 
        'Published date': info[2],
        'author': info[3],
        'Vote': info[4],
        'Number of Players': info[5],
        'Age range': info[6],
        'Game time': info[7],
        'Own it': info[8],
        'Want it': info[9],
        'Favorite': info[10],
        'Heart it': info[11],
        'Played it': info[12],
        'Follow': info[13],
}  
     
df = pd.DataFrame(data) 
  
df.to_csv('export2.csv', index=False)

print('File Saved!')