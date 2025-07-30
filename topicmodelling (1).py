
import pandas as pd
from google.colab import files
from gensim.models import LdaModel

uploaded = files.upload()


df =pd.read_excel("df_cleaned_greek_data (7).xlsx")


import nltk
import gensim
from gensim import corpora
from nltk.corpus import stopwords
import pandas as pd  # For handling data and exporting to Excel

# Download NLTK resources (if needed)
nltk.download('punkt')  # For tokenizing words

custom_stopwords= ["ναι", "οχι", "και", "αλλα", "μη", "ομως", "μα", "i", "γεια", "σας", "καλησπερα", "στο", "στη", "το", "τη", "τα", "τους", "οι", "ο", "η", "καλημερα"]

def preprocess(text):
    # Tokenize, remove stopwords, and retain only alphabetic characters
    tokens = nltk.word_tokenize(text.lower())  # Tokenize using NLTK
    tokens = [word for word in tokens if word.isalpha()]
    tokens=[word for word in tokens if word not in custom_stopwords]
    return tokens

# Step 2: Prepare the data
processed_sentences = [preprocess(sentence) for sentence in sentences]
   
# Step 3: Create Dictionary
dictionary = corpora.Dictionary(processed_sentences)

# Step 5: Create Corpus
corpus = [dictionary.doc2bow(text) for text in processed_sentences]

# Step 4: Train LDA Model
lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=17,      # Adjust based on your dataset
    passes=10,
    iterations=100,
    alpha='auto',       # Auto-tune alpha
    eta='auto'          # Auto-tune beta (optional)
)

# Step 5: Store Topics in a List
topics = []
for idx, topic in lda.print_topics(num_words=3):
    topic_words = topic.split(" + ")
    words = [word.split("*")[1].strip().replace('"', '') for word in topic_words]
    topics.append({"Topic Number": idx, "Words": ", ".join(words)})

# Step 6: Convert the topics list to a pandas DataFrame
df_topics = pd.DataFrame(topics)

df_topics.to_excel("topic_modelling_20topics1.xlsx")

# Download the file to your local machine
files.download("topic_modelling_20topics1.xlsx")
