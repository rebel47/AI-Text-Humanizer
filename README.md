# **AI Text Humanizer**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**AI Text Humanizer** is a Streamlit-based web application that uses Google Gemini Flash 1.5 to rewrite AI-generated text, making it sound more human-like while preserving its meaning and length. The app is designed for learning purposes and demonstrates the capabilities of large language models (LLMs) and natural language processing (NLP).

---

## **Features**
- **Humanize AI-Generated Text**: Rewrites text to make it sound more natural and human-like.
- **Preserve Length**: Ensures the output text has the same length as the input.
- **Tone Selection**: Allows users to choose the tone of the rewritten text (e.g., Casual, Formal, Persuasive, Neutral).
- **Large Text Support**: Processes large texts by splitting them into smaller chunks.
- **Download Humanized Text**: Provides an option to download the rewritten text as a `.txt` file.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- A Google Gemini API key (available from [Google Cloud](https://cloud.google.com/))

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/rebel47/AI-Text-Humanizer.git
   cd ai-text-humanizer
   ```

2. Create a `.env` file in the root directory and add your Google Gemini API key:
   ```
   GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Running the Application**
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

---

## **How to Use**
1. **Paste Your Text**: Copy and paste your AI-generated text into the input box.
2. **Select a Tone**: Choose the desired tone for the rewritten text (e.g., Casual, Formal, Persuasive, Neutral).
3. **Humanize Text**: Click the "Humanize Text" button to process the text.
4. **View and Download**: The humanized text will appear in the output box. You can download it as a `.txt` file using the download button.

---

## **Folder Structure**
```
ai-text-humanizer/
│
├── app.py                # Streamlit application code
├── .env                  # Environment variables (API key)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## **Technologies Used**
- **Streamlit**: For building the web application interface.
- **Google Gemini Flash 1.5**: For rewriting and humanizing text.
- **Python-dotenv**: For managing environment variables (API key).

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- [Google Gemini](https://cloud.google.com/)) for providing the powerful language model.
- [Streamlit](https://streamlit.io/)) for making it easy to build and share web apps.


Enjoy using the **AI Text Humanizer**! If you find this project useful, please give it a ⭐ on GitHub.


