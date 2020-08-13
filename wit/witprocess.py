# Varghese George 2020
from wit import Wit
import secret
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
def recievemessage(message):
    # Break the object down to the entities in the message
    entities = message['entities']
    print(message)
    # Grab each entity
    word = first_entity(entities, 'word')

    # Output the labels from the text, in my application I categorize Contact, Name, and Message Subject
    # You will need to train your application on the website to cater to your needs
    # Outputs N/A if missing information
    print("Word to define: " + word)


# Insert your Wit.AI token here
client = Wit(secret.key)
# Retrieves input, clientmessage() returns JSON, which recievemessage() processes
recievemessage(client.message(input("Ask your question: ")))