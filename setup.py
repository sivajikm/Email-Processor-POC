# setup.py
import os

def create_env_file():
    """Creates a .env file with the OpenAI API key."""
    if os.path.exists('.env'):
        print("A .env file already exists. Do you want to overwrite it? (y/n)")
        choice = input().lower()
        if choice != 'y':
            print("Setup cancelled.")
            return
    
    print("Please enter your OpenAI API key:")
    api_key = input()
    
    with open('.env', 'w') as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")
    
    print(".env file created successfully!")

def setup_project():
    """Sets up the project structure."""
    # Create directories
    os.makedirs('templates', exist_ok=True)
    
    # Create .env file
    create_env_file()
    
    print("\nProject setup complete! You can now run the application with:")
    print("python app.py")

if __name__ == "__main__":
    setup_project()
