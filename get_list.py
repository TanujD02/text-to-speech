import edge_tts
import asyncio


# Function to get the list of available Indian voices
async def get_indian_voices():
    voices = await edge_tts.list_voices()

    # Filter voices to include only those with 'IN' in the language code (Indian voices)
    indian_voices = [voice for voice in voices if 'IN' in voice['ShortName']]
    return indian_voices


# Function to fetch and return the list of Indian voices
def get_voice_list():
    loop = asyncio.get_event_loop()
    indian_voices = loop.run_until_complete(get_indian_voices())
    return indian_voices
