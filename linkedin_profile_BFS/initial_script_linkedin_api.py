#commands to set password
#export LINKEDIN_PASSWORD="password"


from linkedin_api import Linkedin
import os
import pickle

password = os.environ.get('LINKEDIN_PASSWORD')

# Authenticate using any Linkedin account credentials
api = Linkedin('shahjaidev99@gmail.com', password)

PUBLIC_PROFILE = "saksham-beotra"
profile_response = api.get_profile(PUBLIC_PROFILE)
print(profile_response.keys())

profile_id = profile_response['profile_id']
print(f"Profile ID: {profile_id}")


#parse profile_urn to get the actual urn after the third colon
profile_urn_string = profile_response['profile_urn']
profile_urn = profile_urn_string.split(":")[3]
print(f"Profile URN: {profile_urn}")

print(f"Profile Response: \n {profile_response}")

# GET all connected profiles (1st, 2nd and 3rd degree) of a given profile

connections = api.get_profile_connections(profile_id)

print("*********************************************************************************************")
print("CONNECTIONS \n")
print(connections)

"""
#For the first connection, get the profile id and then get the profile
first_connection = connections[2]
first_connection_name = first_connection['name']
first_connection_public_id = first_connection['public_id']
first_connection_urn_id = first_connection['urn_id']
first_connection_profile = api.get_profile(first_connection_public_id)

print(f"First Connection Profile is: \n {first_connection_profile}")
print(f"Keys of First Connection Profile are: \n {first_connection_profile.keys()}")
#first_connection_urn_string = first_connection_profile['profile_urn']
#first_connection_urn_id = first_connection_urn_string.split(":")[3]

#Fetching the connections of the first connection
first_connection_connections = api.get_profile_connections(first_connection_urn_id)
print("*********************************************************************************************")
print(f"First Connection Connections are: \n {first_connection_connections}")


"""