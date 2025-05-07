import random
from typing import List, Dict

LINKEDIN_CREDENTIALS: List[Dict[str, str]] = [
    # {
    #     "id": "seldomtopper@gmail.com",
    #     "password": "Alpha@12345"
    # },
    {
        "id": "welcomebackdevil1@gmail.com",
        "password": "Dharma@622"
    },
    {
        "id":"swapnilsuman65@gmail.com",
        "password":"Dharma@622"
    }
    # {
    #     "id":"deadevil386@gmail.com",
    #     "password": "Patel123@"
    # },
    # {
    #      "id":"sandys.3211@gmail.com",
    #     "password": "Shobhit12@"
    # }
]

def getRandomLoginCredential():
    return random.choice(LINKEDIN_CREDENTIALS)