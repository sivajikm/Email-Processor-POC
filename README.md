# Email Processing POC

This is a proof of concept application that demonstrates how to process multiple customer emails, classify query types, and generate summaries using CrewAI and LLMs.

## Overview

This application simulates a workflow where:
1. Multiple customer emails are received
2. Emails are analyzed to extract key information
3. Query types (primary and secondary) are identified
4. A comprehensive summary is generated

## Features

- Process multiple emails in a single case
- Extract key information from emails
- Classify queries into primary and secondary types
- Generate concise summaries
- Simple web interface for demonstration

## Prerequisites

- Python 3.9 or higher
- OpenAI API key (for GPT-4 access)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/email-processor-poc.git
cd email-processor-poc
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your OpenAI API key

Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

Alternatively, you can export it as an environment variable:

```bash
# On Windows
set OPENAI_API_KEY=your_api_key_here

# On macOS/Linux
export OPENAI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. Enter email content in the provided text areas
2. Click "Add Another Email" to add more emails if needed
3. Click "Process Emails" to start the analysis
4. View the results:
   - Email Analysis
   - Query Classification (Primary and Secondary)
   - Email Summary

## Example Emails for Testing

You can use these example emails for testing:

**Email 1:**
```
Subject: Missing Files in Data Delivery

Dear Support Team,

Thank you for sending over the customer data files we requested. However, after reviewing the files, we've noticed that several important files seem to be missing from the package. Specifically, we were expecting to receive the Q4 sales reports and customer feedback surveys, but these aren't included in what we received.

Could you please check and send these missing files as soon as possible? We need to complete our analysis by the end of the week.

Best regards,
John Smith
Data Analytics Team
```

**Email 2:**
```
Subject: Re: Missing Files in Data Delivery

Hello,

Just following up on my previous email about the missing files. Our deadline is approaching, and we still haven't received the Q4 sales reports and customer feedback surveys. 

Could you please provide an update on when we can expect to receive these files?

Thank you,
John
```

## Extension Possibilities

- Connect to Salesforce API to create and update cases
- Implement authentication for secure access
- Add support for email attachments
- Implement feedback mechanism to improve classification accuracy
