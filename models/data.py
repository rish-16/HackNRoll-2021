import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com'}:
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]
    # fail?
    return None

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

def process_transcript(transcript):
    transcript_df = pd.DataFrame(transcript)
    transcript_df = transcript_df.replace('\n', ' ', regex=True)
    transcript_df = transcript_df.replace("\"", "")
    transcript_df['end'] = transcript_df['start'] + transcript_df['duration']
    return transcript_df

def get_data(url):
    # url = "https://www.youtube.com/watch?v=-DP1i2ZU9gk&list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA&index=27"
    video_id = extract_video_id(url)
    transcript = get_transcript(video_id)
    transcript_df = process_transcript(transcript)
    return transcript_df

if __name__ == "__main__":
    get_data()