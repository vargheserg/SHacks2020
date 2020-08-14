# Varghese George 2020
from wit import Wit
import os
# from nlp import secret

# Insert your Wit.AI token here
# client = Wit(secret.key)
client = Wit(os.environ['WIT_KEY'])

# Grabs the first occurence of an entity 
def first_entity(entities, entity):
    newEntity = entity + ':' + entity
    # If doesn't exist
    if newEntity not in entities:
        return "N/A"
    val = entities[newEntity][0]['value']
    # If doesn't exist
    if not val:
        return "N/A"
    # Now return if contains full, otherwise the base value
    return val['value'] if isinstance(val, dict) else val


# Break down the entities given the message process
def recievemessage(input):
    message = client.message(input)
    # Break the object down to the entities in the message
    entities = message['entities']
    # Grab each entity
    output = {}
    output['word'] = standardize(first_entity(entities, 'word'))
    output['text'] = message['text']
    output['intent'] = message['intents'][0]['name']
    return output
    # Output the labels from the text, in my application I categorize Contact, Name, and Message Subject
    # You will need to train your application on the website to cater to your needs
    # Outputs N/A if missing information
    
def standardize(toDefine):
    return toDefine.strip().capitalize()

