

#from linkedin_api import Linkedin
from linkedin_api import Linkedin
import os
import pickle

GLOBAL_PROFILE_DICT_PATH = './global_dict_all_profiles.pickle'

PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

class MyLinkedInAPI:
    def __init__(self, username, password):
        self.api = Linkedin('shah.jaidev00@gmail.com', password)
        self.username = username
        self.password = password
        self.api = Linkedin(username, password)
        self.global_profile_dict = pickle.load(open(GLOBAL_PROFILE_DICT_PATH, "rb"))
        self.this_profile_id = None 
        self.this_profile_json = None

    #def process_global_profile_dict(self):

    def display_global_profile_dict(self):
        print("Profile Names in global profile dict:")
        print(self.global_profile_dict.keys())
    
    def get_api_response_and_process_profile(self, profile_id):
        profile_response = self.api.get_profile(profile_id)
        self.this_profile_urn = profile_response['profile_id']
        self.this_profile_response_dict = dict(profile_response)



    def get_profile_urn(self, profile_response):
        profile_urn_string = profile_response['profile_urn']
        profile_urn = profile_urn_string.split(":")[3]
        return profile_urn
    
    def get_profile_connections(self, profile_urn, keywords=None):
        connections = self.api.get_profile_connections(profile_urn)
        return connections
    
    def second_degree_connections_with_keywords(self, profile_urn, keywords=None):
        
        connections_with_filter = self.api.get_profile_connections(self.this_profile_id, network_depths=['F', 'S'], keywords = ["computer science"])
        second_degree = []
        for connection in connections_with_filter:
            second_degree.extend(self.api.get_profile_connections(connection['urn_id']) )

        print(second_degree)
