# README: LanguageAid - AI-Powered Grant Proposal Assistant

## Overview

LanguageAid is a backend application designed to assist non-profit organizations in creating, refining, and optimizing grant proposals using AI-driven technology. The application employs large language models (LLMs) to simplify the proposal writing process, making it more effective for users seeking funding from various sources.

### Key Features

1. **Proposal Generation**: 
   - LanguageAid provides an endpoint to generate initial drafts of grant proposals based on user-input details, leveraging the capabilities of OpenAI's GPT models.

2. **Proposal Refinement**: 
   - The application offers a way to refine existing proposals to enhance clarity, persuasiveness, and impact, again utilizing AI to provide effective language improvements.

### System Components

- **Backend Framework**: 
  - The application is built using Flask, a lightweight Python web framework, to handle HTTP requests and responses.

- **Artificial Intelligence**: 
  - OpenAI's GPT models serve as the core of LanguageAid's AI capabilities, enabling the generation and refinement of proposal content.

- **Endpoints**:
  - `/generate-draft`: Accepts project details from users and produces a draft proposal.
  - `/refine-proposal`: Takes an existing proposal and refines its content to improve effectiveness.

### Required Dependencies

- Flask
- OpenAI Python API

Dependencies can be found in the `requirements.txt` file and are necessary for setting up the development environment properly.

### Setup Instructions

1. **Environment Setup**: 
   - Ensure Python is installed on your machine.
   - Use the command `pip install -r requirements.txt` to install required packages.

2. **Configuration**: 
   - Securely set your OpenAI API key in the environment variable `OPENAI_API_KEY`.

3. **Run the Application**: 
   - Start the Flask application by executing `python app.py` in the terminal.
   - Access the endpoints through tools like Postman for API testing or by developing a frontend that interfaces with these endpoints.

4. **Usage**: 
   - Send JSON requests with necessary data to the `/generate-draft` and `/refine-proposal` endpoints to generate or refine proposals.

### Future Developments

Further enhancements to the LanguageAid application may include:

- Implementing a user-friendly web interface for non-technical users.
- Integration with databases for managing templates and version history.
- Enabling real-time collaboration and compliance checks.

LanguageAid presents an innovative solution to the challenges faced by non-profits in securing funding, by providing an AI-driven platform to simplify and optimize grant proposal writing.
