''' This module contains helper methods. '''
import requests

def parser(api_response):
    ''' Parses the gists api response. '''
    parsed_list = []
    for each_gist in api_response:
        parsed_item = {}
        parsed_item['id'] = each_gist['id']
        parsed_item['url'] = each_gist['url']
        parsed_item['latest_forks'] = fetch_forks(each_gist['forks_url'])
        parsed_item['description'] = each_gist['description']
        parsed_item['owner_login'] = each_gist['owner']['login']
        parsed_item['owner_avatar_url'] = each_gist['owner']['avatar_url']
        parsed_item['files'] = []
        for file_name, file_data in each_gist['files'].items():
            parsed_item['files'].append(file_data)
        parsed_list.append(parsed_item)
    return parsed_list

def fetch_forks(forks_url):
    ''' Get last 3 user forks of a gist. '''
    forks_list = []
    headers = {'Accept': 'application/vnd.github.v3+json'}
    api_response = requests.get(forks_url, headers=headers)
    if api_response.status_code != 200:
        raise Exception('Cannot fetch all forks: {}'.format(api_response.status_code))
    # sort on the basis of timestamp
    api_response = api_response.json()
    api_response.sort(key = lambda x:x['created_at'])
    # get last 3 forks
    for i in range(3):
        if len(api_response) > 0:
            each_fork = api_response.pop()
            username_avatar_dict = {}
            username_avatar_dict[each_fork['owner']['login']] = each_fork['owner']['avatar_url']
            forks_list.append(username_avatar_dict)
    return forks_list
