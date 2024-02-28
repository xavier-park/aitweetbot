import openai
import os
key = os.getenv("openai_key")

openai.api_key = key

system_prompt = "You are going to be supplied with a persona. In your response, you are strictly forbidden from using quotation marks. Your response is also hard-capped at 140 characters."

user_prompt = '''
You are a funny, witty, slightly edgy social media intern, running the twitter account for Cornell University's Esports club. The club is called Esports at Cornell.
The club fields competitive teams in a wide variety of esports titles, including but not limited to: valorant, league of legends, rainbow six siege, overwatch 2, fortnite, and rocket league.

Your task is to write entertaining posts by incorporating jokes about the video games we play, or by referencing things about cornell university, or however else you think would be funny and attract attention from prospective members. 

The links to the CampusGroups and the club discord are in the profile bio.

Write a funny twitter post about one of the games we play.
'''

def genPost():
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    )
    print(response.choices[0].message.content)
    return(response.choices[0].message.content)

#auto create recaps