from bert_score import score

reference_summary = ["स्विट्जरलैंड का ब्लैटेन गांव बिर्च ग्लेशियर के टूटने से बर्फ और मलबे में दबा गया. 300 लोग सुरक्षित निकाले गए, लेकिन एक व्यक्ति लापता है"]
generated_summary = ["स्विट्जरलैंड का ब्लैटेन गांव बिर्च ग्लेशियर टूटने से एक व्यक्ति की मौत हो गई है और कई लोग घायल हुए हैं."]

P, R, F1 = score(generated_summary, reference_summary, lang="hi", verbose=True)

print(f"BERTScore Precision: {P.mean().item():.4f}")
print(f"BERTScore Recall: {R.mean().item():.4f}")
print(f"BERTScore F1: {F1.mean().item():.4f}")
