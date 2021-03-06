import markovify

with open('corpus_data.txt', encoding='utf-8') as corpus:
    text = corpus.read()

text_model = markovify.Text(text)

for i in range(10):
    print(text_model.make_short_sentence(120, tries=25))
