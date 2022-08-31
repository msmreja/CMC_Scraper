from bs4 import BeautifulSoup
import requests
import pandas as pd 





#------------------------------------------Extracting HTML Data---------------------------------------
response = requests.get('https://coinmarketcap.com/?page=1')
soup = BeautifulSoup(response.content, 'html.parser')

#----------------------------------------Code for Locating Reqired data and storing in resulsts-------

results = soup.find('table', {'class':'cmc-table'}).find('tbody').find_all('tr')


name = []
price = []
change_24h = []
market_cap=[]


for result in results[:10]:
    
    # For name
    try:
        name.append(result.find('p', {'class':'sc-1eb5slv-0 iworPT'}).get_text().strip()) 
    except:
        name.append('n/a')
    
    # For price
    try:
        price.append(result.find('div',{'class':'sc-131di3y-0 cLgOOr'}).get_text().strip())
    except:
        price.append('n/a')
    
    # For change_24h
    try:
        change_24h.append(result.find('span', {'class':'sc-15yy2pl-0 kAXKAX'}).get_text().strip())
    except:
        change_24h.append('n/a')

    # For market_cap
    try:
        market_cap.append(result.find('span', {'class':'sc-1ow4cwt-0 iosgXe'}).get_text().strip())
    except:
        market_cap.append('n/a')

#----------------------------------------Printing data using Dataframe(dataframe module)-------------------
FinalData = pd.DataFrame({'Coin': name, 'Price':price, 'Change 24h':change_24h ,'MarketCap':market_cap})
print(FinalData)

FinalData.to_excel('data.xlsx', index=False) #To Store in Excel


