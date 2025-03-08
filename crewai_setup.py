# crewai_setup.py
from crewai import Agent, Task, Crew, Process
from langchain_community.chat_models import ChatOpenAI
import os

class SalesforceEmailProcessor:
    def __init__(self, openai_api_key=None):
        if openai_api_key:
            os.environ["OPENAI_API_KEY"] = openai_api_key
        
        # Initialize the language model
        self.llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.2
        )
        
        # Create the agents
        self.email_analyzer = Agent(
            name="Email Analyzer",
            role="Analyzes emails to extract key information",
            goal="Extract meaningful information from customer emails",
            backstory="An expert in parsing and understanding customer email content",
            verbose=True,
            llm=self.llm
        )
        
        self.query_classifier = Agent(
            name="Query Classifier",
            role="Classifies customer queries into primary and secondary types",
            goal="Accurately categorize customer issues",
            backstory="Extensive experience in customer service and query categorization",
            verbose=True,
            llm=self.llm
        )
        
        self.email_summarizer = Agent(
            name="Email Summarizer",
            role="Creates concise summaries of multiple emails",
            goal="Generate a comprehensive yet concise summary of all related emails",
            backstory="Expert in extracting the essential information from lengthy text",
            verbose=True,
            llm=self.llm
        )
    
    def process_emails(self, emails):
        # Define tasks for the agents
        analyze_emails_task = Task(
            description="""
            Analyze the following customer emails:
            
            {emails}
            
            Extract key information such as:
            1. Customer name
            2. Main concerns or issues
            3. Any specific requests
            4. Timeline or urgency indicators
            5. Any other relevant details
            
            Format your response as a structured analysis.
            """,
            expected_output="A structured analysis of the emails",
            agent=self.email_analyzer
        )
        
        classify_query_task = Task(
            description="""
            Based on the email analysis:
            
            {email_analysis}
            
            Determine the primary and secondary query types.
            
            Primary query types include:
            - Account Management
            - Billing Inquiry
            - Data Delivery
            - Technical Support
            - Product Information
            - Complaint
            - Other (specify)
            
            Secondary query types include:
            - Missing Information
            - Access Issues
            - Format Problems
            - Deadline Concerns
            - Quality Issues
            - Incorrect Data
            - Missing Files
            - Other (specify)
            
            Format your response as a JSON with the following structure:
            {
                "primary_query_type": "Your classification",
                "secondary_query_type": "Your classification",
                "confidence": "High/Medium/Low",
                "reasoning": "Brief explanation for this classification"
            }
            """,
            expected_output="A JSON with query classifications",
            agent=self.query_classifier
        )
        
        summarize_emails_task = Task(
            description="""
            Create a comprehensive summary of these related emails:
            
            {emails}
            
            Your summary should:
            1. Capture the overall situation
            2. Include important details from all emails
            3. Be concise but complete
            4. Be written in a professional tone
            5. Be suitable for inclusion in a customer service case
            
            The summary should be no more than 3 paragraphs.
            """,
            expected_output="A concise summary of all the emails",
            agent=self.email_summarizer
        )
        
        # Set up dependencies between tasks
        classify_query_task.context = {"email_analysis": "{analyze_emails_task.output}"}
        
        # Create and run the crew
        crew = Crew(
            agents=[self.email_analyzer, self.query_classifier, self.email_summarizer],
            tasks=[analyze_emails_task, classify_query_task, summarize_emails_task],
            verbose=True,
            process=Process.sequential
        )
        
        # Execute the crew
        result = crew.kickoff(inputs={"emails": emails})
        
        # Process the results
        outputs = {
            "email_analysis": result[0],
            "query_classification": result[1],
            "summary": result[2]
        }
        
        return outputs
