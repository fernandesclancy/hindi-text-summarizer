# Hindi Text Summarizer

A web-based **Abstractive Hindi Text Summarization** system built using the **mT5 Transformer model**, fine-tuned on the [XL-Sum dataset](https://huggingface.co/datasets/csebuetnlp/xlsum) along with domain-specific Hindi corpora. This project aims to enhance summarization quality for **low-resource languages** like Hindi, producing concise, human-like summaries.

![Hindi Text Summarizer](Hindi%20Text%20summarizer.jpeg)

---

## 🚀 Features
- **Abstractive summarization** for Hindi text
- Supports **long input text** with contextual understanding
- Clean **Flask-based backend** and HTML/CSS/JavaScript frontend
- Optimized **SentencePiece tokenizer** for Hindi
- GPU-accelerated processing for faster inference

---

## 📊 Performance
Evaluated on 1,000+ Hindi documents:

| Metric | Score |
|---|---|
| ROUGE-1 | 86.5 |
| ROUGE-L | 41.7 |
| BERTScore | 0.87 |
| BLEU | 35.2 |

---

## 🔧 Tools & Stack
Python, mT5, HuggingFace Transformers, LSTM, Flask, AWS S3, BeautifulSoup, SentencePiece, Jupyter Notebook

---

## 📂 Project Structure
```
hindi-text-summarizer/
├── app.py                  # Flask app entry point
├── evaluate_metrics.py     # ROUGE / BERTScore evaluation
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend UI
├── static/                 # CSS/JS assets
└── README.md
```

---

## ⚙️ How It Works
1. User enters a Hindi passage into the web interface
2. Text is tokenized using a SentencePiece tokenizer optimized for Hindi
3. The fine-tuned mT5 model generates an abstractive summary
4. Post-processing cleans up repetition and hallucinated phrases
5. The final summary is returned and displayed instantly

---

## 🎯 Background
This project began as part of an NLP Research Internship at REVA University's R&D Cell, and was later extended into a full Master's thesis — covering the complete pipeline from Hindi document collection and ETL preprocessing, through model fine-tuning, evaluation, and deployment as a live web app.

---

## 📍 Status
Completed — deployed as a working Flask web application.

## 🔗 Contact
📧 fernandesclancy17@gmail.com
💼 [linkedin.com/in/clancyfernandes](https://linkedin.com/in/clancyfernandes)

---
Made with ❤️ using Flask & mT5 | © 2025
