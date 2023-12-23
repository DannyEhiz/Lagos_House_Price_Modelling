import pandas as pd
from bs4 import BeautifulSoup
import requests
import pickle
import warnings
warnings.filterwarnings('ignore')

# Create Scrapping Function 
def scrapper(search_url, start_page, stop_page):
    base_url = 'https://nigeriapropertycentre.com/'
    house_links = []

    for page_number in range(start_page, stop_page):
        page = requests.get(f'{search_url}{page_number}')

        # instantiate the beautiful soup class 
        soup = BeautifulSoup(page.content, 'lxml')

        # Capture the parent DIV of all the targets 
        house_list = soup.find_all('div', class_='wp-block-body')

        # Capture the end point(the sites) of all the targets
        for targets_div in house_list: # ...................................... Iterate through the general parent div of the targets
            for target_address in targets_div.find_all('a', href =True): # .... Extract the targets' individual endpoint(targets' site address)
                # The code above will normal return just the endpoint of the target without the host url, so we add them and save into a list 
                house_links.append(f"{base_url}{target_address['href']}") 
            
    scraped_data = []
    for links in house_links:
        b = requests.get(links)
        soups = BeautifulSoup(b.content, 'lxml')

        try:
            name = soups.find('h4', class_='content-title').text.strip()
            location = soups.find_all('address')[0].text.strip()
            price = int(soups.find_all('span', class_='price')[1].text.strip().replace(',', ''))
            bedrooms = soups.find('i', class_='fal fa-bed').find_next('span').text
            bathrooms = soups.find('i', class_='fal fa-bath').find_next('span').text
            toilet = soups.find('i', class_='fal fa-toilet').find_next('span').text
        except AttributeError:
            bedrooms = 'No Info'
            bathrooms = 'No Info'
            toilet = 'No Info'
        except IndexError:
            bedrooms = 'No Info'
            bathrooms = 'No Info'
            toilet = 'No Info'
        except ValueError:
            price = 'No Info'

        # create a dictionary to save these information 
        house_data = {
            'Type': name,
            'Location': location,
            'Price': price,
            'Bedroom': bedrooms,
            'Bathrooms': bathrooms,
            'Toilet': toilet
        }
        scraped_data.append(house_data)
    return pd.DataFrame(scraped_data)    

# Creating Cleaning Function 
def cleaner(data):
    data['Location Area'] = data['Location'].apply(lambda x: x.split(',')[0])
    data['State'] = data['Location'].apply(lambda x: x.split(',')[-1])
    data['Location'] = data['Location'].apply(lambda x: x.split(',')[-2])
    data.drop('Type', axis = 1, inplace = True)
    return data



# Scrapping Data For IKOYI Lagos 
search = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/ikoyi/showtype?page='
ikoyi = scrapper(search, 1, 6) # ............................ Call the scrapper function
ikoyi.to_csv('Ikoyi_house_price_raw.csv') # ................. Save the raw data to csv
ikoyis = ikoyi.copy() # ..................................... Copy the raw data
cleaner(ikoyis) # ........................................... Call the cleaner function

# Scrapping Data For LEKKI Lagos 
search = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/lekk/showtype?page='
lekki = scrapper(search, 1, 10) # ............................ Call the scrapper function
lekki.to_csv('lekki_house_price_raw.csv') # ................. Save the raw data to csv
lekkis = lekki.copy() # ..................................... Copy the raw data
cleaner(lekkis) # ........................................... Call the cleaner function

# Scrapping Data For IKEJA Lagos 
search = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/ikeja/showtype?page='
ikeja = scrapper(search, 1, 6) # ............................ Call the scrapper function
ikeja.to_csv('Ikeja_house_price_raw.csv') # ................. Save the raw data to csv
ikejas = ikeja.copy() # ..................................... Copy the raw data
cleaner(ikejas) # ........................................... Call the cleaner function

# Scrapping Data For Vicotria Island Lagos 
search = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/victoria-island/showtype?page='
vi = scrapper(search, 1, 15) # ............................ Call the scrapper function
vi.to_csv('vi_house_price_raw.csv') # ................. Save the raw data to csv
vis = vi.copy() # ..................................... Copy the raw data
cleaner(vis) # ........................................... Call the cleaner function

# Scrapping Data For YABA Lagos 
search = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/yaba/showtype?page='
yaba = scrapper(search, 1, 15) # ............................ Call the scrapper function
yaba.to_csv('yaba_house_price_raw.csv') # ................. Save the raw data to csv
yabas = yaba.copy() # ..................................... Copy the raw data
cleaner(yabas) # ........................................... Call the cleaner function

# Scrapping Data For AGEGE Lagos 
search = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/agege/showtype?page='
agege = scrapper(search, 1, 15) # ............................ Call the scrapper function
agege.to_csv('agege_house_price_raw.csv') # ................. Save the raw data to csv
ageges = agege.copy() # ..................................... Copy the raw data
cleaner(ageges) # ........................................... Call the cleaner function

# Scrapping Data For AJAH Lagos 
search = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/ajah/showtype?page='
ajah = scrapper(search, 1, 15) # ............................ Call the scrapper function
ajah.to_csv('ajah_house_price_raw.csv') # ................. Save the raw data to csv
ajahs = ajah.copy() # ..................................... Copy the raw data
cleaner(ajahs) # ........................................... Call the cleaner function