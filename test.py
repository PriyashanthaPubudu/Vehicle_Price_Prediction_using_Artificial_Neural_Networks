import requests
from bs4 import BeautifulSoup


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
            content_car = s_car.find_all('a')
            print('')
            print('')
            print((type(content_car)))
            for line in content_car:
                # ad_url = line.get('href')
                # print(ad_url)
                ad_url = line.get('href')
                if ad_url != "/en/promotions":
                    ad_url = "https://ikman.lk" + ad_url

                    print(ad_url)

                    car_array = []
                    other_details = []
                    # car_array_attributes = ['Brand', 'Model', 'Year', 'Condition', 'Body_Type', 'Fuel_Type', 'Price']
                    check_url = requests.get(ad_url)
                    if check_url.status_code == 200:
                        # soup_price = BeautifulSoup(check_url.content, 'html.parser')

                        soup2 = BeautifulSoup(check_url.content, 'html.parser')
                        soup2 = soup2.find('div',
                                           class_='ad-meta--17Bqm justify-content-flex-start--1Xozy align-items-normal--vaTgD flex-wrap-wrap--2PCx8 flex-direction-row--27fh1 flex--3fKk1')
                        span_tags = soup2.find_all('span')
                        for span in span_tags:
                            car_array.append(span.text)

                        if len(car_array) == 5:
                            temp = car_array[4]
                            car_array[4] = "None"
                            car_array.append(temp)

                        if car_array[4] == 'Saloon':
                            car_array[4] = 'Sedan'

                        soup_price = BeautifulSoup(check_url.content, 'html.parser')
                        soup_description = soup_price
                        soup_others = soup_price
                        soup_price = soup_price.find('div', class_='amount--3NTpl')
                        vehicle_price = soup_price.text
                        # print(soup_price.text)
                        price = str(soup_price.text)[3:]
                        car_array.append(price)

                        soup_description = soup_description.find('div', class_='description--1nRbz')
                        description = soup_description.find_all('p')
                        final_description = ""

                        for sentence in description:
                            final_description = final_description + sentence.text

                        # print(final_description)

                        # Finding the owner by using the vehicle description
                        keywords_found = extracting_para_keywords(final_description)

                        soup_others = soup_others.find_all('div', class_='word-break--2nyVq value--1lKHt')
                        for details in soup_others:
                            soup_others = details.text
                            other_details.append(soup_others)

                        if len(other_details) == 9:
                            temp2_array = other_details[0:2]
                            temp_array = other_details[2:]
                            trim_edition = "not specified"
                            other_details = temp2_array
                            other_details.append(trim_edition)
                            other_details = other_details + temp_array

                        print(car_array)
                        print(len(car_array))
                        print(vehicle_price)
                        print(keywords_found)
                        print(other_details)
                        print(len(other_details))

                        # for t in range(5):
                        #     print(car_array_attributes[t] + " : " + car_array[t])

                    count += 1

        print("")
        print("Total car count :" + str(count))
        print("Successfully retrieved the data !!")

    else:
        print("Web Page Loading Failed !")

    return


def car_price(url):
    car_array = []
    # car_array_attributes = ['Brand', 'Model', 'Year', 'Condition', 'Body_Type', 'Fuel_Type']
    check_url = requests.get(url)
    if check_url.status_code == 200:
        # soup_price = BeautifulSoup(check_url.content, 'html.parser')
        soup = BeautifulSoup(check_url.content, 'html.parser')
        soup = soup.find('div',
                         class_='ad-meta--17Bqm justify-content-flex-start--1Xozy align-items-normal--vaTgD flex-wrap-wrap--2PCx8 flex-direction-row--27fh1 flex--3fKk1')
        span_tags = soup.find_all('span')
        for span in span_tags:
            car_array.append(span.text)
        print(car_array)

        # for t in range(5):
        #     print(car_array_attributes[t] + " : " + car_array[t])

    return


def extracting_para_keywords(paragraph):
    keywords = ['1st owner', '2nd owner', '3rd owner', 'first owner', 'second owner', 'third owner']
    owner_type = []
    paragraph = paragraph.lower()
    for word in keywords:
        if word in paragraph:
            owner_type.append(word)

    if len(owner_type) == 0:
        none = 'not specified'
        owner_type.append(none)
    else:
        return owner_type
    return owner_type


car_home_url = "https://ikman.lk/en/ads/sri-lanka/cars"
cars = "https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page="

car_details(cars, car_home_url)

# my_url = "https://ikman.lk/en/ad/honda-fit-2012-for-sale-colombo-1143"
# car_price(my_url)
