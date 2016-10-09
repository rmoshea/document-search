# Document Search
The goal of this exercise is to create a working program to search a set of documents for the given search term or phrase (single token), and return results in order of relevance. Relevancy is defined as number of times the exact term or phrase appears in the document.

### Instructions
Create three methods for searching the documents:
- Simple string matching
- Text search using regular expressions
- Preprocess the content and then search the index

Prompt the user to enter a search term and search method, execute the search, and return results. For instance:
Three files have been provided for you to read and use as sample search content.
Run a performance test that does 2M searches with random search terms, and measures execution time. Which approach is fastest? Why?
Provide some thoughts on what you would do on the software or hardware side to make this program scale to handle massive content and/or very large request volume (5000 requests/second or more).
