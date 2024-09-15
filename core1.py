import os
import whisper
import yt_dlp
from transformers import pipeline

# Function to download and extract audio from a YouTube video using yt-dlp
def download_youtube_video(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'input.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    print("Video downloaded and audio extracted: input.mp3")
    return 'input.mp3'

# Function to transcribe audio to text using Whisper
def audio_to_text(audio_file, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_file)
    transcript = result['text']
    print(f"Transcription: {transcript}")
    return transcript

# Function to summarize text using Hugging Face transformers
def summarize_text(text, max_length=100, min_length=30):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    print(f"Summary: {summary[0]['summary_text']}")
    return summary[0]['summary_text']

# Function to classify text using Hugging Face transformers
def classify_text(text):
    classifier = pipeline("text-classification")
    classification = classifier(text)
    print(f"Classification: {classification}")
    return classification

# Main workflow
def process_youtube_video(youtube_url):
    # Step 1: Download and extract audio from YouTube video
    audio_file = download_youtube_video(youtube_url)
    
    # Step 2: Transcribe audio to text
    transcript = audio_to_text(audio_file)
    
    # Step 3: Summarize the transcript
    summary = summarize_text(transcript)
    
    # Step 4: Classify the context of the transcript
    classification = classify_text(transcript)
    
    return {
        "transcript": transcript,
        "summary": summary,
        "classification": classification
    }

# Example usage
if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=v26CcifgEq4"  # Replace with the actual YouTube URL
    results = process_youtube_video(youtube_url)
    
    # Output the results
    print("=== Final Results ===")
    print("Transcript:", results['transcript'])
    print("Summary:", results['summary'])
    print("Classification:", results['classification'])
