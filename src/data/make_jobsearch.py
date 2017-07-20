# -*- coding: utf-8 -*-
import os
from dotenv import find_dotenv, load_dotenv
import socket
from indeed import IndeedClient

# Create the directory cursor to navigate directory
project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

def get_ip():
    return socket.gethostbyname(socket.gethostname())

# Set static user parameters
load_dotenv(find_dotenv())
indeed_pub_id = os.environ.get("INDEED_PUB_ID")
user_agent = os.environ.get("DEF_USER_AGENT")
static_params = {
    'userip' : get_ip(),
    'useragent' : user_agent
}

# Set the indeed client
client = IndeedClient(indeed_pub_id)

# Script that pulls job search data using Indeed's api
def job_search(params):
    # query and location parameters are required
    if "q" not in params:
        print("Please include query parameter")
        return None
    if "l" not in params:
        print("Please include location parameter")
        return None
    params.update(static_params)
    search_response = client.search(**params)
    return search_response

def job_details(keys):
    details_response = client.jobs(jobkeys = (keys))
    return details_response
