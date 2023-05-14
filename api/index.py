# Import Flask and request libraries
from flask import Flask, request
# Import Anthropic Claude API
import anthropic

# from customized_linkedinAPI import LinkedIn
import os

from LinkedInAPI import MyLinkedInAPI

app = Flask(__name__)

# Create a Claude instance with your API key
claude = anthropic.Client(os.environ.get('ANTHROPIC_API_KEY'))

USERNAME = "shahjaidev"
PASSWORD = os.environ.get('LINKEDIN_PASSWORD')


# linkedinAPIinstance = MyLinkedInAPI(USERNAME, PASSWORD)

# Define a route for the app
@app.route("/", methods=["POST"])
def index():
    # Get the input paragraph from the request body
    paragraph = request.get_json().get("paragraph")
    # Call the Claude API to extract keywords and types
    keywords = claude.extract_keywords(paragraph)
    # Return the keywords and types as a list of tuples
    return str(keywords)


# Define a route for getting recommended profiles
# @app.route("/recommended_profiles", methods=["GET"])
def recommended_profiles():

    return recommended_profiles


# Define a route for generating a cover letter
@app.route("/cover-letter", methods=["POST"])
def cover_letter():
    # Get the input text from the request body
    text = request.get_json().get("text")

    #APPEND the text to 

    #Get the job posting from the request body
    job_posting = request.get_json().get("job_posting")

    # Create a prompt for Claude to generate a cover letter
    prompt = f"Write a cover letter based on the following information about the candidate and the job posting:\n\n" \
                f"Candidate: {text}\n\n" \
                f"Job Posting: {text}" \
                "Cover Letter: "
    
    print(prompt)
    
    # Call the Claude API to generate a cover letter
    cover_letter = claude.generate_text(prompt)

    # Return the cover letter as a PDF file
    return cover_letter

@app.route("/intro", methods=["POST"])
def intro():
    candidate_summary = request.get_json().get("candidate_summary")
    lead_summary = request.get_json().get("lead_summary")
    aspiration = request.get_json().get("aspiration")

    prompt = f"Pretend like you are a warm and welcoming recruiter.  Write a concise introduction message from a candidate to a lead." \
             f"Here are the descriptions for each the candidate and the lead:\n\n" \
                f"Candidate: {candidate_summary}\n\n" \
                f"Lead: {lead_summary}" \
                f"And here is the candidate's aspiration: {aspiration}"
    
    # Call the Claude API to generate an intro
    max_tokens_to_sample: int = 1000
    resp = claude.completion(
        prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}",
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-v1",
        max_tokens_to_sample=max_tokens_to_sample,
    )

    return resp['completion']


def summarize_linkedin_profile(profile_dict):
    #Use Claude to summarize the profile

    keys_to_keep = ['industryName', 'lastName', 'firstName', 'geoLocationName', 'headline', 'experience', 'education', 'projects']
    filtered_profile_dict = {key: profile_dict[key] for key in profile_dict if key in keys_to_keep}

    # the values of the dictionary
    profile_summary = str(filtered_profile_dict) 

    #Create a prompt for Claude to summarize the profile
    prompt = f"Summarize the following LinkedIn profile to capture the key parts:\n\n" \
                f"{profile_summary}\n\n" \
                "Summary: "   
    
    #Call the Claude API to summarize the profile
    summary = claude.generate_text(prompt)

    #Return the summary
    return summary
