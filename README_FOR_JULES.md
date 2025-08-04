# Project Hand-off & Roadmap: Cosmic Pixels / Newsletter OS

**To:** Jules
**From:** Patrick

### 1. Objective
This is the initial prototype of "Newsletter OS," an LLM-powered content curation and newsletter automation platform. The goal is to build a powerful, semi-autonomous tool for producing the "Cosmic Pixels" publication.

**Repo:** `https://github.com/cosmopax/cosmic_pixels`

### 2. Current Functionalities (v1.0)
- **Modular Data Fetching:** Gathers content from Google Search, NewsAPI, and ArXiv.
- **LLM Digestion:** Uses the Gemini 1.5 Flash API to generate concise summaries and extract relevant keywords for each piece of content.
- **Persistent Storage:** A local SQLite database (`content_library.db`) stores all articles, preventing duplicate processing.
- **Streamlit UI:** A functional web interface provides a three-step workflow: Gather, Curate, and Publish.
- **Visual Enhancement:** Integrates Google Image Search to find and attach relevant images to curated articles.
- **Beehiiv Integration:** Assembles the final content into Markdown and pushes a completed **draft** to Beehiiv via their API.

### 3. Setup for Your Local Environment
**Note:** The project is fully functional on my machine. The local `config.ini` is populated with my keys.
**A. Clone & Set up Environment:**
```bash
git clone [https://github.com/cosmopax/cosmic_pixels.git](https://github.com/cosmopax/cosmic_pixels.git) && cd cosmic_pixels
conda create --name newsletter_env python=3.11 -y && conda activate newsletter_env
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
**B. Configure API Keys:**
Create your own `config.ini` file in the project root and populate it with your API keys. The file is gitignored.
**C. Run the App:**
`streamlit run app.py`

### 4. Roadmap & Next Steps
This is where the project gets really interesting. Here is a potential roadmap for expansion:

**Advanced Curation & Content Management:**
- **Summary Editor:** Add a text area in the UI to allow for manual editing of the LLM-generated summaries before publication.
- **Library View:** Build a new tab in the app to search, filter, and reuse all articles ever collected in the SQLite database.
- **Sentiment Analysis:** Integrate a library (like NLTK or SpaCy TextBlob) to add sentiment scores (positive/negative/neutral) to articles to aid in curation.

**Expanded Data Sources:**
- **RSS Feeds:** Add a module to ingest articles from a list of specified RSS feeds.
- **Social Media:** Integrate the X/Twitter API to fetch trending topics or links shared by key accounts.
- **YouTube Transcripts:** Add a module to take a YouTube URL, transcribe the video, and summarize the transcript.

**Deeper AI & Automation:**
- **Autonomous Mode:** Create a "magic button" that automatically selects the top N articles based on a scoring algorithm and generates a full draft with a synthesized introduction.
- **Tone & Style Control:** Add a dropdown to control the summary generation tone (e.g., "witty," "academic," "concise").

### 5. A Note on Collaboration
As we work on this, let's practice self-documentation. When a significant feature is added or changed, please add a dated note to the **Changelog** section below.

### Changelog
- **2025-08-04**: Initial project commit. Core application is stable and functional.
- **2025-08-04**: Added this comprehensive hand-off and roadmap document.
