from transformers import T5Tokenizer, MT5ForConditionalGeneration

model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)

tokenizer.save_pretrained("./mt5_model")
model.save_pretrained("./mt5_model")
