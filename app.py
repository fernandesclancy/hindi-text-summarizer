from flask import Flask, request, jsonify, render_template
from transformers import T5Tokenizer, MT5ForConditionalGeneration
import re

app = Flask(__name__)

# Load mT5 model (can be local or online)
model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '').strip()

    if not text:
        return jsonify({'error': 'कोई इनपुट टेक्स्ट नहीं मिला'}), 400

    # Prepare input for the model
    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary with tuned parameters
    summary_ids = model.generate(
    inputs,
    max_length=300,       
    min_length=120,       #  force richer output
    num_beams=8,
    length_penalty=0.8,
    repetition_penalty=2.5,
    no_repeat_ngram_size=3,
    early_stopping=True
)


    # Decode model output
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Hallucination cleanup
    hallucinated_phrases = [
        "यह भी पढ़ें", "बीबीसी", "कार्यक्रम", "एक मुलाक़ात",
        "हाई प्रोफ़ेशनल", "टेलीविज़न", "ऑस्ट्रेलियाई"
    ]
    for phrase in hallucinated_phrases:
        summary = summary.replace(phrase, "")

    # Grammar and punctuation cleanup
    summary = re.sub(r"''", "", summary)
    summary = re.sub(r"\([^)]*\)", "", summary)
    summary = re.sub(r"[।!?]{2,}", "।", summary)
    summary = re.sub(r"\s+", " ", summary).strip()

    return jsonify({'summary': summary})



if __name__ == '__main__':
    app.run(debug=True)