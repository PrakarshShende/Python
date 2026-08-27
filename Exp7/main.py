'''Word Tokenization'''

# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download('punkt_tab')

# text = "I love learning Python and Artificial Intelligence"

# words = word_tokenize(text)

# print("Original Text: ",text)
# print("Words Token: ",words)

'''Sentence Tokenization'''

# import nltk
# from nltk.tokenize import sent_tokenize

# nltk.download('punkt_tab')

# text = "Python is easy to learn. NLP is very interesting. I love AI."

# senten_ = sent_tokenize(text)

# print("Original Sentence: ",text)
# print("Sentence Token: ",senten_)

'''Stemming'''

# from nltk.stem import PorterStemmer

# ps = PorterStemmer()

# words = ["easily",
# "easier",
# "connected",
# "connection",
# "connecting"]

# for word in words:
#     print(word, "->",ps.stem(word))

'''Lemmatization'''

# import nltk
# from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')

# lemmatizer = WordNetLemmatizer()

# words = ["dogs", "cats", "running", "playing", "studies"]

# for word in words:
#     print(word,"->",lemmatizer.lemmatize(word))

'''StopWord Removal'''

# import nltk 
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('punkt_tab')

# text = "I am learning Python and I am enjoying the course."

# words = word_tokenize(text)

# stopwords = set(stopwords.words('english'))

# result = []

# for word in words:
#     if word.lower() not in stopwords:
#         result.append(word)

# print("Original: ",words)
# print("After removal of stopwords: ",result)

'''Lower Case'''

# text = "HELLO Python WORLD"

# result = text.lower()

# print("Original:", text)
# print("Lowercase:", result)

'''Remove punctuation'''

# import string

# text = "Hello, world! I love python"

# result = ""

# for char in text:
#     if char not in string.punctuation:
#         result+=char

# print("Original:", text)
# print("Without punctuation:", result)

'''Remove Numbers'''

# text = "I have 2 books and 3 pens."

# result = ""

# for char in text:
#     if not char.isdigit():
#         result += char

# print("Original:", text)
# print("Without numbers:", result)

