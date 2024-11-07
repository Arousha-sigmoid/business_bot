import google.generativeai as genai

GOOGLE_AI_STUDIO = 'AIzaSyDRc7gCPtzWCMYzxnqY6KDFzEp4LaYaLRk'
genai.configure(api_key=GOOGLE_AI_STUDIO)

prompt = """
Given below is a list of valid questions that can be asked by a user.
List of valid questions:
- 'Provide total cost to serve the German market in 2023.',
- 'Provide commentary on how these costs have evolved compared to 2022?',
- 'What are the drivers of increase in transport costs?',
- 'What are the drivers of increase in secondary transport costs?',
- 'What are the levers using which the average pallets per trip can be controlled / improved.',
- 'Explore reduction of SLA of top 40 customers and generate scenarios to identify cost savings.',
- 'Explore reduction of SLA of top 20 customers and generate scenarios to identify cost savings.',
- 'Specify cost savings for Customer ID Dir_239',
- 'Specify cost savings for Customer ID Dir_121'

Suppose a user has asked "{ques}".
Can the question asked by the user be mapped to any one of the above given valid questions? Return only the valid question if it exists.
If the user's question cannot be mapped to any of the valid questions, return NULL.

"""

# Load a pre-trained LLM model
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(query):
    response = model.generate_content(prompt.format(ques=query))
    return response.text