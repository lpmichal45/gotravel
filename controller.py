#! /usr/bin/python3

'''
    Module: controller.py

    Description: To serve as a traffic router and request maintainer from the
                 start to end of an API call

'''

import lib.interfaces.skyscanner as scan

HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 403
HTTP_CONFLICT = 409

def do_authorization():
    '''
        Validates an http request is authorized
    '''

def check_flights(outdate, indate, cabin, adults, children, infants, country,
                  currency, locale, originplace, destinationplace):
    '''
        Searches for all available flights within the search
        parameters and returns a list of flights that fit that criteria
    '''
    result = scan.create_session(outdate, indate, cabin, adults, children,
                                 infants, country, currency, locale,
                                 originplace, destinationplace)
    return HTTP_OK

def book_flights(outdate, indate, cabin, adults, children, infants, country,
                 currency, locale, originplace, destinationplace):
    '''
        Books a flight for the destination
    '''
    message = 'success'
    return HTTP_OK

def health_check():
    '''
        Validates that the service is up and running
    '''
    message = 'success'
    return HTTP_OK, message
