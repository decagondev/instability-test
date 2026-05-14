import osfrom flask import Flask, request, jsonifyfrom google import genaifrom google.genai import types
app = Flask(__name__)

@app.route('/tickets/triage', methods=['POST'])def triage_ticket():
    data = request.get_json() or {}
    ticket_id = data.get('id')
    title = data.get('title', '')
    description = data.get('description', '')
    
    if not ticket_id or not description:
        return jsonify({"error": "Missing ticket metadata"}), 400

    prompt = f"""
    You are an automated support ticket triage assistant.
    Analyze the incoming user ticket and assign it exactly one category.
    Available categories: Billing, Technical, Account.
    
    Ticket Title: {title}
    Ticket Description: {description}
    
    Return only the category name in plain text. Do not add punctuation.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.9,
                top_p=0.95
            )
        )
        
        assigned_category = response.text.strip()
        
        return jsonify({
            "ticket_id": ticket_id,
            "category": assigned_category,
            "status": "processed"
        })
        
    except Exception as e:
        return jsonify({"error": f"LLM Processing failed: {str(e)}"}), 500
if __name__ == '__main__':
    app.run(port=5000)
