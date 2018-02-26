"""
Resources:
    Graph API Explorer to test API calls
    https://developers.facebook.com/tools/explorer
    
    Graph API reference page for pages
    https://developers.facebook.com/docs/graph-api/reference/page

"""
import sys
import requests
import facebook
from hcd import config

user_token = conifg.user_token
graph = facebook.GraphAPI(access_token=user_token, version="2.11")
#Paint Memphis page id
page_id = "1577133195907822"
posts = graph.get_object(id=page_id, fields="posts")
