import string
from collections import Counter
from hashpart1 import HashTable

def preprocess_text(text):
    """Preprocess the input text by removing punctuation and converting to lowercase."""
    text = text.truncate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words = text.split()
    return words

class WordFrequencyCounter:
    def __init__(self):
        self.hash_table = HashTable()
    
    def add_words(self, words):
        """Add words to the hash table and count their frequencies."""
        for word in words:
            current_count = self.hash_table.get(word)
            if current_count is None:
                self.hash_table.insert(word, 1)
            else:
                self.hash_table.insert(word, current_count + 1)
    
    def get_top_n_words(self, n=10):
        """Get the top N most frequent words."""
        word_frequencies = []
        for bucket in self.hash_table.buckets:
            current_node = bucket
            while current_node:
                word_frequencies.append((current_node.key, current_node.value))
                current_node = current_node.next
        
        # Sort the words by frequency in descending order and return the top N
        word_frequencies.sort(key=lambda x: x[1], reverse=True)
        return word_frequencies[:n]

# Read the text file
with open('thelostrace.txt', 'r') as file:
    text = file

# Preprocess the text
words = preprocess_text(text)

# Create a word frequency counter
word_counter = WordFrequencyCounter()

# Add words to the counter
word_counter.add_words(words)

# Get the top 10 most frequent words
top_words = word_counter.get_top_n_words(10)

# Print the top 10 words with their frequencies
print("Top 10 most frequent words:")
for word, frequency in top_words:
    print(f"{word}: {frequency}")