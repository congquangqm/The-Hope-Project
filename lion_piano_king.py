'''
# The Hope Project
# This project aims to raise awareness about global issues
# and to inspire people to take action and make a difference.

# Imports
import requests
import json
import os

# Variables
base_url = 'https://api.hope.org/'

# Constants
CAMPAIGN_TYPES = ['fundraiser', 'petition', 'volunteer', 'social_action']

# Functions
def get_campaigns_by_type(types):
    """Returns a list of campaigns of the given types from the hope API"""
    results = []

    for t in types:
        url = base_url + 'campaigns?type=' + t
        response = requests.get(url)
        data = json.loads(response.text)
        results.extend(data['results'])

    return results

def get_campaign_details(campaign_id):
    """Returns the details of a campaign from the hope API"""
    results = []
    url = base_url + 'campaigns/' + campaign_id
    response = requests.get(url)
    data = json.loads(response.text)
    results.extend(data)

    return results

def list_campaigns():
    """Lists all campaigns from the hope API"""
    url = base_url + 'campaigns'
    response = requests.get(url)
    data = json.loads(response.text)
    
    for campaign in data['results']:
        print(f"Campaign Name: {campaign['name']}")
        print(f"  Type: {campaign['type']}")
        print(f"  Description: {campaign['description']}")
        print("")

def get_campaign_updates(campaign_id):
    """Returns a list of updates for the given campaign from the hope API"""
    results = []
    url = base_url + 'campaigns/' + campaign_id + '/updates'
    response = requests.get(url)
    data = json.loads(response.text)
    results.extend(data['results'])

    return results

def list_campaign_updates(campaign_id):
    """Lists updates for the given campaign from the hope API"""
    updates = get_campaign_updates(campaign_id)
    for update in updates:
        print(f"Update Title: {update['title']}")
        print(f"  Description: {update['description']}")
        print("")

def print_campaign_details(campaign_id):
    """Prints the details of a campaign from the hope API"""
    details = get_campaign_details(campaign_id)
    print(f"Campaign Name: {details['name']}")
    print(f"Description: {details['description']}")
    print(f"Location: {details['location']}")
    print(f"Start Date: {details['start_date']}")
    print(f"End Date: {details['end_date']}")
    print(f"Type: {details['type']}")

def create_campaign(name, description, location, start_date, end_date, type, goal):
    """Creates a new campaign in the hope API"""
    url = base_url + 'campaigns'
    body = {
        "name": name,
        "description": description,
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "type": type,
        "goal": goal
    }
    response = requests.post(url, json=body)
    data = json.loads(response.text)
    return data

def update_campaign(campaign_id, name, description, location, start_date, end_date, type, goal):
    """Updates an existing campaign in the hope API"""
    url = base_url + 'campaigns/' + campaign_id
    body = {
        "name": name,
        "description": description,
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "type": type,
        "goal": goal
    }
    response = requests.put(url, json=body)
    data = json.loads(response.text)
    return data

def delete_campaign(campaign_id):
    """Deletes an existing campaign from the hope API"""
    url = base_url + 'campaigns/' + campaign_id
    response = requests.delete(url)
    data = json.loads(response.text)
    return data

def add_campaign_update(campaign_id, title, description):
    """Adds an update to the given campaign in the hope API"""
    url = base_url + 'campaigns/' + campaign_id + '/updates'
    body = {
        "title": title,
        "description": description
    }
    response = requests.post(url, json=body)
    data = json.loads(response.text)
    return data

def delete_campaign_update(update_id, campaign_id):
    """Deletes an existing campaign update from the hope API"""
    url = base_url + 'campaigns/' + campaign_id + '/updates/' + update_id
    response = requests.delete(url)
    data = json.loads(response.text)
    return data

# Main
if __name__ == '__main__':
    os.system('clear')
    campaigns = get_campaigns_by_type(CAMPAIGN_TYPES)
    print("Campaigns:")
    list_campaigns()

    # Get a specific campaign
    selected_campaign = input("Enter the ID of a campaign to view: ")
    print("Campaign Details:")
    print_campaign_details(selected_campaign)

    # Get the updates for a campaign
    print("Campaign Updates:")
    list_campaign_updates(selected_campaign)