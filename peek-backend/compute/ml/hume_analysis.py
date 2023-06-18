# Calls Hume Sentiment Analysis on the summary of the data
# Used in protos/responseBuilder to add emoji to response
import asyncio

from hume import HumeStreamClient
from hume.models.config import LanguageConfig

emotion_emojis = {
    'Admiration': '😍',
    'Adoration': '😊',
    'Aesthetic Appreciation': '🎨',
    'Amusement': '😄',
    'Anger': '😡',
    'Annoyance': '😒',
    'Anxiety': '😰',
    'Awe': '😲',
    'Awkwardness': '😳',
    'Boredom': '😴',
    'Calmness': '😌',
    'Concentration': '🧠',
    'Confusion': '😕',
    'Contemplation': '🤔',
    'Contempt': '😒',
    'Contentment': '😌',
    'Craving': '😋',
    'Determination': '💪',
    'Disappointment': '😞',
    'Disapproval': '👎',
    'Disgust': '🤢',
    'Distress': '😫',
    'Doubt': '🤷‍♂️',
    'Ecstasy': '😵',
    'Embarrassment': '😳',
    'Empathic Pain': '😢',
    'Enthusiasm': '🤩',
    'Entrancement': '😍',
    'Envy': '😒',
    'Excitement': '😃',
    'Fear': '😨',
    'Gratitude': '🙏',
    'Guilt': '😔',
    'Horror': '😱',
    'Interest': '😮',
    'Joy': '😄',
    'Love': '❤️',
    'Nostalgia': '🕰️',
    'Pain': '😣',
    'Pride': '😊',
    'Realization': '😮',
    'Relief': '😌',
    'Romance': '💑',
    'Sadness': '😢',
    'Sarcasm': '😏',
    'Satisfaction': '😌',
    'Desire': '😍',
    'Shame': '😳',
    'Surprise (negative)': '😮😱',
    'Surprise (positive)': '😮😲',
    'Sympathy': '😔',
    'Tiredness': '😴',
    'Triumph': '🎉'
}



async def get_emoji(samples):
    client = HumeStreamClient("FGBc2uC2KiT6hOrOFJaVumvfAPTWKR8rKaw5uvuuV6Qh89Lo")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            # print(emotions)
            # for emotion in emotions:
            #     print(emotion)

            max_emotion = max(emotions, key=lambda x: x['score'])
            max_emotion_name = max_emotion['name']
            print(max_emotion)
            return emotion_emojis[max_emotion_name]
            # print(f"{max_emotion_name} {emotion_emojis[max_emotion_name]}")
            # print(max(emotions, emotions))

def humeAnalysis(summary):
    return "🤓"
    return asyncio.run(get_emoji([summary]))