
import json
import watson_developer_cloud


ASSISTANT_ID="<Enter your ASSISTANT_ID>"



assistant = watson_developer_cloud.AssistantV2(
    iam_apikey='<Enter your API key>',
    version='2018-11-08',
    url='<Enter your assistant url that you set while creating the assistant>'# eg:'https://gateway-lon.watsonplatform.net/assistant/api' for london server
)


#creates a session with the api
session = assistant.create_session("ASSISTANT_ID").get_result()
print(json.dumps(session, indent=2))



#send your query to the api
#response variable recieves the json object with the response from api and the intent and extent detected
response = assistant.message(
    assistant_id='ASSISTANT_ID',
    session_id=session["session_id"],
    input={
        'message_type': 'text',
        'text': 'When are you open'            
    }
).get_result()

print(json.dumps(response, indent=2))



#used to close the session
resp=assistant.delete_session("ASSISTANT_ID", session["session_id"]).get_result()
print(json.dumps(resp, indent=2))