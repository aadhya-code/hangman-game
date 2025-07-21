import requests
import random

def get_words_by_difficulty(level):
    # Alternative API: Datamuse (no API key required)
    difficulty_map = {
        'easy': {'max': 5},
        'medium': {'min': 6, 'max': 8},
        'hard': {'min': 9}
    }

    params = difficulty_map.get(level, {'max': 5})
    words = []

    try:
        length_filter = ""
        if 'min' in params:
            length_filter += f"&sp={'?' * params['min']}"
        if 'max' in params:
            length_filter += f"&sp={'?' * params['max']}"

        # Query Datamuse API for random common words
        url = f"https://api.datamuse.com/words?topics=everyday&max=100{length_filter}"
        response = requests.get(url)
        if response.status_code == 200:
            for item in response.json():
                word = item.get('word', '')
                if word.isalpha():
                    words.append(word.lower())
    except Exception as e:
        print("[Fallback to local word list due to API issue]", e)

    if len(words) < 5:
        fallback = {
            'easy': ["cat", "dog", "sun"],
            'medium': ["castle", "planet", "mirror"],
            'hard': ["awkward", "zombie", "dazzling"]
        }
        return fallback.get(level, fallback['easy'])

    return random.sample(words, 10)