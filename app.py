from flask import Flask, request, render_template
from elasticsearch import Elasticsearch

# Initialize the Flask app
app = Flask(__name__)

# Initialize Elasticsearch
es = Elasticsearch()

# Index a document
@app.route('/index', methods=['POST'])
def index():
  # Get the document from the request
  document = request.json

  # Index the document in Elasticsearch
  es.index(index='my_index', doc_type='my_type', body=document)

  # Return a success response
  return {'status': 'success'}

# Search for documents
@app.route('/search', methods=['GET'])
def search():
  # Get the search query from the request
  query = request.args.get('q')

  # Search for documents that match the query
  results = es.search(index='my_index', q=query)

  # Return the search results
  return results

# Render the search page
@app.route('/', methods=['GET'])
def search_page():
  return render_template('search.html')
