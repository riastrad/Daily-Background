#!/usr/bin/env python3
#
# @Author: Josh Erb <josh.erb>
# @Date:   10-Apr-2017 12:04
# @Email:  josh.erb@excella.com
# @Last modified by:   josh.erb
# @Last modified time: 24-Apr-2017 15:04


#####
# IMPORTS
#####

import os
import requests
import random
from glob import glob
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
    assert query.status_code == 200, 'Failed to retrieve a proper response from the Unsplash API.'

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

def clean(path=out_path):
    """
    Remove old background photos (so I don't have a crazy large background folder)
    """
    # grab all picture files
    fotos = glob(os.path.join(out_path, '*.jpg'))

    # I want to maintain a portfolio of around 25 background pictures
    if len(fotos) > 25:
        # Don't want to be prejudiced so I'll just drop a random one each time
        rd_indx = random.randrange(len(fotos))
        os.remove(fotos[rd_indx])
        # Want to keep track of what gets deleted, just for kicks
        with open(os.path.join(out_path, '.cron', 'removal_log.txt'), 'a') as f:
            f.write(dt.utcnow().strftime('%Y-%b-%d') + ': removed ' + fotos[rd_indx] + '\n')

def main():
    """
    Main execution function for foto_fetcher.py.
    """
    img = fetch()
    save_me(img)
    clean()

#####
# EXECUTION
#####

if __name__ == '__main__':
    main()
