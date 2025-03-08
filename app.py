# app.py
from flask import Flask, render_template, request, jsonify
import json
from crewai_setup import SalesforceEmailProcessor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_emails', methods=['POST'])
def process_emails():
    data = request.json
    emails = data.get('emails', [])
    
    # Combine emails into a single string for processing
    emails_text = "\n\n--- NEW EMAIL ---\n\n".join(emails)
    
    # Initialize and run the CrewAI processor
    processor = SalesforceEmailProcessor()
    try:
        results = processor.process_emails(emails_text)
        
        # Try to parse the query classification as JSON
        try:
            query_classification = json.loads(results["query_classification"])
        except:
            # If it's not valid JSON, just use the string
            query_classification = {
                "primary_query_type": "Could not parse",
                "secondary_query_type": "Could not parse",
                "raw_output": results["query_classification"]
            }
        
        response = {
            "success": True,
            "email_analysis": results["email_analysis"],
            "query_classification": query_classification,
            "summary": results["summary"]
        }
    except Exception as e:
        response = {
            "success": False,
            "error": str(e)
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
