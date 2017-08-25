#!/usr/bin/env python3
#
# @Author: Josh Erb <josh.erb>
# @Date:   10-Apr-2017 12:04
# @Email:  josh.erb@excella.com
# @Last modified by:   josh.erb
# @Last modified time: 10-Apr-2017 13:04


#####
# IMPORTS
#####

import os
import requests
from urllib import parse
from datetime import datetime as dt

#####
# CONSTANTS
#####

api_url = 'http://source.unsplash.com/random/2560x1600'
out_path = os.path.join(os.path.expanduser('~'), 'pictures/backgrounds')

#####
# FUNCTIONS
#####


def fetch(url=api_url):
    """
    Takes a url string as an argument and performs a request for a
    random photo on the Unsplash API.
    """
    # Query the Unsplash API for a random background image
    query = requests.get(url)

    # Here in case I run into trouble while running the code
    assert query.status_code == 200, 'Unsuccessful connection to the Unsplash API.'

    # hand the query back
    return query


def save_me(response, path=out_path):
    """
    Save the returned value of fetch() as a .jpg file in the specified output
    path.
    """
    # set the name as the day the photo was pulled
    fn = dt.utcnow().strftime('%Y-%b-%d') + '.jpg'

    # save the file to the designated backgrounds folder
    with open(os.path.join(path, fn), 'wb') as f:
            f.write(response.content)


def main():
    """
    Main execution function for foto_fetcher.py.
    """
    img = fetch()
    save_me(img)

#####
# EXECUTION
#####


if __name__ == '__main__':
    main()
