from flask import Flask, request, jsonify
import openai

# Assuming the use of OpenAI's GPT as our LLM
openai.api_key = 'your_openai_api_key'  # Secure this in environment variables

app = Flask(__name__)

# Endpoint to generate a draft proposal
@app.route('/generate-draft', methods=['POST'])
def generate_draft():
    data = request.json
    prompt = f"Generate a grant proposal draft for the following details: {data['details']}"
    
    try:
        completion = openai.Completion.create(
            engine="davinci",  # Use GPT-3 or a more appropriate model version
            prompt=prompt,
            max_tokens=1500  # Adjust based on need
        )
        proposal = completion.choices[0].text.strip()
        return jsonify({'proposal': proposal})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to improve language in an existing draft
@app.route('/refine-proposal', methods=['POST'])
def refine_proposal():
    data = request.json
    prompt = f"Refine this proposal to be more effective: {data['proposal']}"
    
    try:
        completion = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1500
        )
        refined_proposal = completion.choices[0].text.strip()
        return jsonify({'refined_proposal': refined_proposal})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
