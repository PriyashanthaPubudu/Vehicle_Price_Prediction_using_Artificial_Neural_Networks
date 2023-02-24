import requests
from bs4 import BeautifulSoup


# Getting the details of the cars
def car_details(ikman_cars, home_url):
    count = 0
    check_url = requests.get(home_url)
    if check_url.status_code == 200:
        for t in range(1, 2):
            ikman_cars = ikman_cars + str(t)
            car_url = requests.get(ikman_cars)
            # print(car_url.status_code)
            # print(car_url.url)
            soup_car = BeautifulSoup(car_url.content, 'html.parser')
            # print(soup.prettify())
            s_car = soup_car.find('ul', class_='list--3NxGO')
            content_car = s_car.find_all('li')
            for line in content_car:
                print(line.text)
                count += 1
            # print(content)
        print("")
        print("Total car count :" + str(count))
        print("Successfully retrieved the data !!")
    else:
        print("Web Page Loading Failed !")

    return


# Getting the details of the vans
def van_details(ikman_vans, home_url):
    check_url = requests.get(home_url)
    if check_url.status_code == 200:
        ikman_vans = ikman_vans + "1"
        van_url = requests.get(ikman_vans)
        print(van_url.status_code)
        print(van_url.url)
        soup_van = BeautifulSoup(van_url.content, 'html.parser')
        # print(soup.prettify())
        s_van = soup_van.find('ul', class_='list--3NxGO')
        content_van = s_van.find_all('li')
        for line in content_van:
            print(line.text)
        print("")
        print("")
        # print(content)
    else:
        print("Web Page Loading Failed !")
    return


# Getting the details of the three-wheelers
def tw_details(ikman_tw, home_url):
    check_url = requests.get(home_url)
    if check_url.status_code == 200:
        ikman_tw = ikman_tw + "1"
        tw_url = requests.get(ikman_tw)
        print(tw_url.status_code)
        print(tw_url.url)
        soup_tw = BeautifulSoup(tw_url.content, 'html.parser')
        # print(soup.prettify())
        s_tw = soup_tw.find('ul', class_='list--3NxGO')
        content_tw = s_tw.find_all('li')
        for line in content_tw:
            print(line.text)
        print("")
        print("")
        # print(content)
    else:
        print("Web Page Loading Failed !")
    return


car_home_url = "https://ikman.lk/en/ads/sri-lanka/cars"
cars = "https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page="

van_home_url = "https://ikman.lk/en/ads/sri-lanka/vans"
vans = "https://ikman.lk/en/ads/sri-lanka/vans?sort=date&order=desc&buy_now=0&urgent=0&page="

tws_home_url = "https://ikman.lk/en/ads/sri-lanka/three-wheelers"
tws = "https://ikman.lk/en/ads/sri-lanka/three-wheelers?sort=date&order=desc&buy_now=0&urgent=0&page="

car_details(cars, car_home_url)
# van_details(vans,van_home_url)
# tw_details(tws,tws_home_url)
