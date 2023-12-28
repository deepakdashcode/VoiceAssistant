from bardapi import Bard
import os
os.environ['_BARD_API_KEY'] = 'eAjqg5Mk85aB8MERlO5zHXHG3aRGN-y_E9M5QTmSCdyqhlSRv8eor3IB7wEs3U8pK14inA.'


def getAnswer(prompt: str):
    ans = Bard().get_answer(prompt)
    return ans['content']
