# -*- coding:utf-8 -*-
"""
 @author: huang
 @date: 2024-06-21
 @File: invoke
 @Description: 
"""


from open_api_client_sdk import OpenClient

client = OpenClient('qwert123456', 'asdfgqwertzxcvb')

# Example of GET request
client.get_name_by_get('exampleName')

# Example of POST request
client.get_name_by_post('exampleName')