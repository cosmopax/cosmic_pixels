# Project Hand-off: Cosmic Pixels / Newsletter OS

**To:** Jules
**From:** Patrick

### 1. Objective
This is the initial prototype of "Newsletter OS," an LLM-powered content curation and newsletter automation platform for the "Cosmic Pixels" publication.

**Repo:** `https://github.com/cosmopax/cosmic_pixels`

### 2. Current Status
- The initial version is now stable and pushed to this repo.
- The Streamlit app launches and all modules are functional.
- It can gather content, summarize it via the Gemini API, store it, and allow for curation and publishing.

### 3. Setup for Your Local Environment

**A. Clone & Set up Environment:**
```bash
# Clone the repository
git clone https://github.com/cosmopax/cosmic_pixels.git
cd cosmic_pixels

# Create and activate the conda environment
conda create --name newsletter_env python=3.11 -y
conda activate newsletter_env

# Install dependencies from the requirements file
pip install -r requirements.txt

# Download the necessary SpaCy model
python -m spacy download en_core_web_sm
```

**B. Configure API Keys:**
You'll need to create your own `config.ini` file. Create it in the project root and paste this template, filling it with your own API keys.
```ini
[API_KEYS]
BEEHIIV_API_KEY = YOUR_BEEHIIV_API_KEY
BEEHIIV_PUBLICATION_ID = YOUR_BEEHIIV_PUBLICATION_ID
NEWS_API_KEY = YOUR_NEWS_API_KEY
GOOGLE_API_KEY = YOUR_GOOGLE_GEMINI_API_KEY
GOOGLE_CSE_ID = YOUR_Google Search_ENGINE_ID
```

**C. Run the App:**
```bash
streamlit run app.py
```
