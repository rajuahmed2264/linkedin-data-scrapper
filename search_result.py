import json

# Load HAR file
with open('results.har', 'r', encoding='utf-8') as f:
    har_data = json.load(f)

# Loop through entries
for entry in har_data['log']['entries']:
    url = entry['request']['url']
    
    # Check if the URL is a LinkedIn search page
    if 'linkedin.com/search/' in url:
        # Extract and print data (modify this part to suit your needs)
        print(f"URL: {url}")
        print(f"Method: {entry['request']['method']}")
        
        # If the response body contains the data you're interested in
        if '_response' in entry and 'content' in entry['_response'] and 'text' in entry['_response']['content']:
            print(f"Response Body: {entry['_response']['content']['text']}")