import re

# Define the documents
documents = {
    "Document 1": "The quick brown fox jumped over the lazy dog.",
    "Document 2": "The lazy dog slept in the sun.",
    "Document 3": "The fox is quick and clever."
}

# Create an empty inverted index
inverted_index = {}

# Build the inverted index
for document_id, text in documents.items():

    # Convert text to lowercase
    text = text.lower()

    # Extract words and remove punctuation
    words = re.findall(r'\b\w+\b', text)

    # Add words to inverted index
    for word in words:

        if word not in inverted_index:
            inverted_index[word] = []

        if document_id not in inverted_index[word]:
            inverted_index[word].append(document_id)


# Display the inverted index
print("INVERTED INDEX")
print("-" * 40)

for word in sorted(inverted_index):
    print(word, "->", ", ".join(inverted_index[word]))


# Document retrieval function
def retrieve_documents(query):
    query = query.lower().strip()

    if query in inverted_index:
        return inverted_index[query]
    else:
        return []


# Accept search term
search_term = input("\nEnter a word to search: ")

# Retrieve documents
result = retrieve_documents(search_term)

# Display result
if result:
    print("\nDocuments containing", search_term, ":")
    for document in result:
        print(document)
else:
    print("\nNo documents found for:", search_term)



# ==============================================================================
# COMPLETE BLOCK-BY-BLOCK EXPLANATION OF THE CODE
# ==============================================================================

# --- BLOCK 1: Importing Regular Expressions & Defining Corpus ---
# - `import re`: Imports Python's built-in Regular Expression module used for 
#   pattern-based text tokenization and punctuation removal[cite: 2].
# - `documents = {...}`: Defines a sample document collection (corpus) as a 
#   dictionary mapping unique document IDs (`"Document 1"`, `"Document 2"`, 
#   `"Document 3"`) to their text strings[cite: 2].

# --- BLOCK 2: Initializing & Building the Inverted Index ---
# - `inverted_index = {}`: Initializes an empty dictionary where each key will be 
#   a unique term (word) and its value will be a list of document IDs (postings 
#   list) containing that word[cite: 2].
# - `for document_id, text in documents.items():`: Iterates over each document in 
#   the corpus[cite: 2].
# - `text = text.lower()`: Normalizes text to lowercase so `"The"` and `"the"` 
#   are indexed as the exact same term[cite: 2].
# - `words = re.findall(r'\b\w+\b', text)`: Extracts only alphanumeric word tokens 
#   bounded by word boundaries (`\b`), automatically stripping punctuation like 
#   periods[cite: 2].
# - Nested loop (`for word in words:`):
#   - `if word not in inverted_index:`: Creates an empty postings list for a newly 
#     encountered word[cite: 2].
#   - `if document_id not in inverted_index[word]:`: Appends `document_id` only if 
#     it isn't already recorded for that word, preventing duplicate document IDs 
#     when a word appears twice in the same document (like `"the"` in Document 1)[cite: 2].

# --- BLOCK 3: Displaying the Inverted Index ---
# - Loops through `sorted(inverted_index)` to print every indexed term in 
#   alphabetical order alongside its comma-separated postings list[cite: 2].

# --- BLOCK 4: Document Retrieval Function & User Search ---
# - `def retrieve_documents(query):`: Normalizes the user's query using `.lower()` 
#   and `.strip()` (removing leading/trailing spaces), then performs a direct O(1) 
#   dictionary lookup in `inverted_index`[cite: 2]. Returns the matching list of 
#   document IDs or an empty list `[]` if not found[cite: 2].
# - `search_term = input(...)`: Prompts the user to enter a single search keyword[cite: 2].
# - Calls `retrieve_documents(search_term)` and prints all matching document IDs, 
#   or displays a "No documents found" message if the list is empty[cite: 2].
# ==============================================================================


# ==============================================================================
# EXTERNAL VIVA QUESTIONS & ANSWERS (COMPLETE PRACTICAL)
# ==============================================================================

# Q1: What is the main objective of this practical?
# A1: To implement an Inverted Index data structure for a collection of text 
#     documents and use it to perform fast keyword-based document retrieval[cite: 2].

# Q2: What is an Inverted Index, and why is it used in Information Retrieval?
# A2: An Inverted Index is a hash-map/dictionary structure that maps every unique 
#     word (term) in a corpus to the list of documents (postings list) in which 
#     that word appears[cite: 2]. Instead of scanning every document linearly during a 
#     search (which takes O(N) time), it allows instant O(1) term lookup—making it 
#     the core data structure behind search engines.

# Q3: What is the difference between a Forward Index and an Inverted Index?
# A3: A Forward Index maps Document ID -> List of words inside that document (like 
#     our initial `documents` dictionary)[cite: 2]. An Inverted Index flips this mapping 
#     to Word -> List of Document IDs containing that word[cite: 2].

# Q4: What does the regex pattern `r'\b\w+\b'` do in `re.findall()`?
# A4: `\w+` matches one or more word characters (letters, digits, underscores), 
#     and `\b` asserts a word boundary. Together, `re.findall(r'\b\w+\b', text)` 
#     extracts clean words while ignoring spaces and punctuation marks like `.`[cite: 2].

# Q5: Why is `if document_id not in inverted_index[word]:` necessary?
# A5: A word can appear multiple times within the same document (for example, `"the"` 
#     appears twice in Document 1)[cite: 2]. This check ensures each `document_id` is 
#     stored only once in that word's postings list, avoiding duplicate search results[cite: 2].

# Q6: What is a "Postings List" and a "Dictionary/Vocabulary" in IR terminology?
# A6: In an inverted index, the collection of all unique indexed terms (the keys 
#     of `inverted_index`) is called the Dictionary or Vocabulary, and the list of 
#     document IDs associated with each term (the values) is called its Postings List[cite: 2].

# Q7: Why did we normalize both the document text and the search query with `.lower()`?
# A7: To achieve case-insensitive indexing and retrieval[cite: 2]. Without `.lower()`, 
#     searching for `"the"` would miss `"The"` at the start of `"Document 1"`[cite: 2].

# Q8: What happens if a user enters a multi-word query (e.g., "quick fox") in this code?
# A8: Because `retrieve_documents()` treats the entire input string as a single 
#     dictionary key (`if query in inverted_index`), a multi-word query will not 
#     match any single-word key and will return "No documents found"[cite: 2].

# Q9: How would you extend this code to support Boolean queries like "quick AND fox" or "quick OR slept"?
# A9: Tokenize the query into individual terms, look up each term's postings list 
#     in `inverted_index`, convert those lists to Python `set` objects, and use 
#     set intersection (`&`) for `AND`, set union (`|`) for `OR`, or set difference 
#     (`-`) for `NOT`.

# Q10: How can this basic inverted index be improved for real-world search engines?
# A10: By adding stop-word removal and stemming during indexing, storing term 
#      frequencies (TF) and word positions inside the postings list (for phrase 
#      queries and TF-IDF ranking), and sorting postings lists for fast merging.
# ==============================================================================