from langchain_openai import AzureChatOpenAI
from openai import AzureOpenAI
#from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_experimental.agents import create_csv_agent
import pandas as pd
from prompts import *
import os

os.environ["AZURE_OPENAI_API_KEY"] = "706afaa560b44dbcb802ce2f94597b1b"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://rbcandlopenai.openai.azure.com/"
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-02-15-preview"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "gpt-4"

client = AzureOpenAI(
    api_key='706afaa560b44dbcb802ce2f94597b1b',
    api_version="2024-02-15-preview",
    azure_endpoint = 'https://rbcandlopenai.openai.azure.com/',
    )


# func to call the LLM with a query
def query_llm(query,client=client, deployment_name='gpt-4'):
    message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},\
                    {"role":"user","content":query}]

    response = client.chat.completions.create(
        model=deployment_name,
        messages=message_text,
        temperature=0,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    try:
        result = eval(response.choices[0].message.content.split('```')[1])
        return result
    except:
        return [#"cross_transfers_data",
                #"inbound_primary_shipment",
                "material_cost_month_level_data",
                #"outbound_data"
                ]


azure_chat = AzureChatOpenAI(
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],

)

def get_agent_response(query):
    prompt = rel_dataset_prompt.format(query = query)
    lis_f = query_llm(prompt)
    print("Relevant Files by LLM: ",lis_f)
    if lis_f[0] == "None":
        return "Sorry, The Given Query is not relevant to the data. Feel free to Try any other query."
    else:
        lis_f = ["data/"+x for x in lis_f]
        agent = create_csv_agent(azure_chat,
                                lis_f,
                                agent_type="tool-calling",
                                #agent_type='openai-functions',
                                #handle_parsing_errors=True,
                                max_iterations=10,
                                #agent_executor_kwargs={"handle_parsing_errors":"If successfully execute the plan then return summarize and end the plan. Otherwise, please call the API step by step."},
                                agent_executor_kwargs={"handle_parsing_errors":True},
                                verbose=True,)
        # df_lis = [pd.read_csv(path) for path in lis_f]        
        # agent = create_pandas_dataframe_agent(azure_chat,
        #                         df_lis, 
        #                         agent_type="tool-calling",
        #                         handle_parsing_errors=True,
        #                         max_iterations=10,
        #                         verbose=True,)
        try:
            response = agent.run(query)
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, could not find a valid response for the given query. Feel free to Try any other query."