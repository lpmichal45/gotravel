#! /usr/bin/python3

import requests

URL = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0'

HEADERS = {
    'x-rapidapi-host': 'skyscanner-skyscanner-flight-search-v1.p.rapidapi.com',
    'x-rapidapi-key': 'abd754eb9amsh6e385f53dbfbd00p1c831ejsna3b421348526',
    'content-type': 'application/x-www-form-urlencoded'
}


def create_session(start_date, end_date, cabin_class, adults, children, infants,
                country, currency, locale, origin_place, destination_place):
    '''
        Calls Skyscanner and searches for flights for specified location and
        specified dates
    '''
    payload = ('outboundDate=' + start_date + '&inboundDate=' + end_date +
               '&cabinClass=' + cabin_class + '&adults=' + str(adults) +
               '&children=' + str(children) + '&infants=' + str(infants) +
               '&country=' + country + '&currency=' + currency +
               '&locale=' + locale + '&originPlace=' + origin_place +
               '&destinationPlace=' + destination_place)

    response = requests.request('POST', url=URL, data=payload, headers=HEADERS)

    print(response.text)
    print(response.status_code)
    print(response.json())
