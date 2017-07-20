# -*- coding: utf-8 -*-
import os
from dotenv import find_dotenv, load_dotenv
import socket
from indeed import IndeedClient

# create the directory cursor
project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

# load up the .env entries as environment variables
load_dotenv(find_dotenv())
indeed_pub_id = os.environ.get("INDEED_PUB_ID")
user_agent = os.environ.get("DEF_USER_AGENT")
_query = "python"
_loc = "atlanta"

# set the client
client = IndeedClient(indeed_pub_id)

# Script that pulls job search data using Indeed's api
def job_search(extra_params):

    params = {
        'q' : _query,
        'l' : _loc,
        'userip' : get_ip(),
        'useragent' : user_agent
    }
    params.update(extra_params)
    search_response = client.search(**params)
    return search_response

def job_details(keys):
    details_response = client.jobs(jobkeys = (keys))
    return details_response

def get_ip():
    return socket.gethostbyname(socket.gethostname())
