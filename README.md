# YT_Transcripter
# YouTube Transcript to Detailed Notes Converter

This Streamlit application converts transcripts from YouTube videos into detailed, organized notes using Google Gemini AI. The application allows users to input multiple YouTube links, customize the summarization instructions, and specify the desired length of the summary.

## Features

- **Multi-Video Input**: Accept multiple YouTube links for content aggregation.
- **YouTube Transcript API Integration**: Fetch transcripts from provided YouTube videos.
- **Google Gemini API Integration**: Utilize advanced language processing for coherent text generation.
- **Transcript Processing and Cleaning**: Clean and prepare transcripts for summarization.
- **Intelligent Script Generation**: Generate a cohesive summary of multiple videos based on custom user instructions.
- **Customization and Control**: Specify instructions, focus areas, and summary length.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Bhaskar-10/YT_Transcripter.git
    cd YT_Transcripter
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the root directory of the project and add your API key:

    ```dotenv
    GOOGLE_API_KEY=your_google_gemini_api_key
    ```

## Usage

1. **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

2. **Interact with the application**:

    - Enter YouTube video links separated by commas.
    - Optionally provide custom instructions or preferences for the summary.
    - Adjust the slider to set the desired summary length.
    - Click "Get Detailed Notes" to generate and view the summary.

## File Structure
The application is designed with a modular structure for scalability and ease of maintenance:
```bash
YT_Transcripter/
│
├── app.py # Main application code
├── requirements.txt # List of required Python packages
├── .env # Environment variables file (not included in the repository)
└── README.md # This readme file
```
## Libraries Used

- **Streamlit**: For building the interactive user interface.
    - **Library**: `streamlit`

- **Dotenv**: For loading environment variables from a `.env` file.
    - **Library**: `python-dotenv`

- **YouTube Transcript API**: To fetch the transcripts of the provided YouTube videos.
    - **Library**: `youtube-transcript-api`

- **Google Generative AI**: For generating organized and summarized content from video transcripts.
    - **Library**: `google-generative-ai`

- **os**: For accessing environment variables and handling other OS-level operations.
    - **Library**: `os` (standard Python library)
## Flowchart
                                      +----------------+
                                      |  User Input   |
                                      +----------------+
                                             |
                                             |
                                             v
                                      +----------------+
                                      |  Extract Video  |
                                      |  ID from Links  |
                                      +----------------+
                                             |
                                             |
                                             v
                                      +---------------------+
                                      |  Fetch Transcripts  |
                                      |  using YouTube API  |
                                      +---------------------+
                                             |
                                             |
                                             v
                                      +-----------------------+
                                      |  Combine Transcripts  |
                                      |  into a Single Text   |
                                      +-----------------------+
                                             |
                                             |
                                             v
                                      +-----------------------+
                                      |  Construct Prompt     |
                                      |  using Base Prompt,   |
                                      |  Custom Instructions, |
                                      |  and Desired Summary  |
                                      |  Length               |
                                      +-----------------------+
                                             |
                                             |
                                             v
                                      +---------------------------+
                                      |  Content Summarization    |
                                      |  using Google Generative  |
                                      |  AI to Summarize Text     |
                                      +---------------------------+
                                             |
                                             |
                                             v
                                      +--------------------+
                                      |  Display Summary   |
                                      |  in Streamlit App  |
                                      +--------------------+
## Video Demo
  

https://github.com/Bhaskar-10/YT_Transcripter/assets/116245937/e93e6388-95ef-4afd-b3a4-c469f5be8a13


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Streamlit for providing an excellent framework for building web applications.
- YouTube Transcript API for easy access to video transcripts.
- Google Gemini API for advanced language processing capabilities.

Feel free to contribute to this project by opening issues and submitting pull requests. Happy coding!
