# import the apiai library and name it dialogflow
import apiai as dialogflow


def talk_to_agent(user_query):
    # access the Dialogflow api by using your agent's Client Access Token in the settings section on Dialogflow
    agent = dialogflow.ApiAI("8515a4a0e9c1437fb253e52541b73cb4")

    # build the request to be sent to dialogflow
    apirequest = agent.text_request()

    # set the language, session id, and the query (message) being sent to the agent
    apirequest.lang = 'en'
    apirequest.session_id = 'test'
    apirequest.query = user_query

    # send the request and store the response set back by .getresponse()
    response = apirequest.getresponse()

    # get the response from Dialogflow and put it into proper JSON form
    response = json.loads(response.read().decode('utf-8'))

    # print the message spoken by the agent
    print(response['result']['fulfillment']['speech'])


# until the user says "done" allow them to send a message to our agent
query = ""
while query is not "done":
    # get input from user
    query = raw_input()("What would you like to ask the bot? (or say done to exit)")
    # send user input to agent
    talk_to_agent(query)