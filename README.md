# Cosmic Pixels: Newsletter OS

> An LLM-powered content curation and newsletter automation platform.

## Overview

Cosmic Pixels is a powerful, semi-autonomous tool for producing the "Cosmic Pixels" publication. It provides a Streamlit-based web interface to gather, curate, and publish content to a Beehiiv newsletter. The application leverages the Gemini 1.5 Flash API for content summarization and keyword extraction, and it uses various data sources like Google Search, NewsAPI, and ArXiv to gather content.

## Features

- **Modular Data Fetching**: Gathers content from Google Search, NewsAPI, and ArXiv.
- **LLM Digestion**: Uses the Gemini 1.5 Flash API to generate concise summaries and extract relevant keywords for each piece of content.
- **Persistent Storage**: A local SQLite database (`content_library.db`) stores all articles, preventing duplicate processing.
- **Streamlit UI**: A functional web interface provides a three-step workflow: Gather, Curate, and Publish.
- **Visual Enhancement**: Integrates Google Image Search to find and attach relevant images to curated articles.
- **Beehiiv Integration**: Assembles the final content into Markdown and pushes a completed **draft** to Beehiiv via their API.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cosmopax/cosmic_pixels.git
   cd cosmic_pixels
   ```

2. **Create a Conda environment:**
   ```bash
   conda create --name newsletter_env python=3.11 -y
   conda activate newsletter_env
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. **Configure API Keys:**
   Create a `config.ini` file in the project root and populate it with your API keys. You can use the following template:
   ```ini
   [API_KEYS]
   google_api_key = YOUR_GOOGLE_API_KEY
   google_cse_id = YOUR_GOOGLE_CSE_ID
   news_api_key = YOUR_NEWS_API_KEY
   beehiiv_api_key = YOUR_BEEHIIV_API_KEY
   beehiiv_publication_id = YOUR_BEEHIIV_PUBLICATION_ID
   ```

## Usage

To run the application, use the following command:

```bash
streamlit run app.py
```

This will start the Streamlit web server and open the application in your browser.

## Contributing

We welcome contributions to Cosmic Pixels! Please follow these guidelines when submitting a pull request:

- **Code Style**: Please follow the PEP 8 style guide for Python code.
- **Testing**: If you add new features, please include tests.
- **Pull Requests**: Please create a pull request with a clear description of your changes.

## Roadmap & Scope

This is the initial prototype of the application. Here's a potential roadmap for expansion:

**Advanced Curation & Content Management:**
- **Summary Editor**: Add a text area in the UI to allow for manual editing of the LLM-generated summaries before publication.
- **Library View**: Build a new tab in the app to search, filter, and reuse all articles ever collected in the SQLite database.
- **Sentiment Analysis**: Integrate a library (like NLTK or SpaCy TextBlob) to add sentiment scores (positive/negative/neutral) to articles to aid in curation.

**Expanded Data Sources:**
- **RSS Feeds**: Add a module to ingest articles from a list of specified RSS feeds.
- **Social Media**: Integrate the X/Twitter API to fetch trending topics or links shared by key accounts.
- **YouTube Transcripts**: Add a module to take a YouTube URL, transcribe the video, and summarize the transcript.

**Deeper AI & Automation:**
- **Autonomous Mode**: Create a "magic button" that automatically selects the top N articles based on a scoring algorithm and generates a full draft with a synthesized introduction.
- **Tone & Style Control**: Add a dropdown to control the summary generation tone (e.g., "witty," "academic," "concise").

## GitHub Actions Integration

This repository uses GitHub Actions to automate CI/CD workflows.

### Gemini AI Assistant

This repository uses the [Gemini CLI Action](https://github.com/google-github-actions/run-gemini-cli) to provide an AI assistant that can be triggered by creating or editing issues and pull requests.

#### Secrets Configuration

To use the Gemini AI Assistant, you need to add your Google API key as a secret to your GitHub repository.

1.  Go to your repository's **Settings**.
2.  In the left sidebar, click **Secrets and variables**, then click **Actions**.
3.  Click **New repository secret**.
4.  Enter `GOOGLE_API_KEY` as the name of your secret.
5.  Enter your Google API key as the value of your secret.
6.  Click **Add secret**.

#### Usage Examples

You can trigger the Gemini AI Assistant by creating or editing an issue or pull request. The assistant will respond with a comment.

**Issue Comment:**

To ask the assistant a question, create a new issue with your question in the body.

**Pull Request Comment:**

The assistant will automatically comment on new pull requests with a summary of the changes.

## License

This project is licensed under the [MIT License](LICENSE).
