
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Base prompt
base_prompt = """You are a YouTube video transcript organizer. You will be taking the transcript text
and structuring it into clear, organized sections or bullet points. Please provide the structured text
for the given transcript: """

# Getting the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"Error extracting transcript for {youtube_video_url}: {e}")
        return ""

# Getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return ""

st.title("YouTube Transcript to Detailed Notes Converter")

youtube_links = st.text_area("Enter YouTube Video Links (separated by commas):")
custom_prompt = st.text_area("Enter Custom Instructions or Preferences (optional):", value="")
content_length = st.slider("Desired Summary Length (words):", 50, 1000, 250)

if youtube_links:
    video_ids = [link.split("=")[1] for link in youtube_links.split(",") if "=" in link]
    for video_id in video_ids:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    combined_transcript = ""
    youtube_links_list = youtube_links.split(",")
    
    for youtube_link in youtube_links_list:
        youtube_link = youtube_link.strip()
        if youtube_link:
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text:
                combined_transcript += " " + transcript_text
                st.write(f"Added transcript for video: {youtube_link}")

    if combined_transcript:
        # Create the final prompt
        final_prompt = base_prompt
        if custom_prompt:
            final_prompt += "\n\n" + custom_prompt
        final_prompt += f"\n\nPlease summarize the content in approximately {content_length} words."

        summary = generate_gemini_content(combined_transcript, final_prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
    else:
        st.warning("No transcript data could be extracted.")
