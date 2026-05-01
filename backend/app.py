from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

app = Flask(__name__)

CORS(app)

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

PROPERTIES = [
    {
        "id": 1,
        "owner_name": "Robert Chen",
        "property_address": "1420 Market St",
        "city": "Austin",
        "state": "TX",
        "property_type": "Office Building",
        "sq_ft": 12400,
        "years_owned": 31,
        "assessed_value": 4200000
    },
    {
        "id": 2,
        "owner_name": "Margaret Sullivan",
        "property_address": "892 Congress Ave",
        "city": "Austin",
        "state": "TX",
        "property_type": "Retail Strip",
        "sq_ft": 8200,
        "years_owned": 24,
        "assessed_value": 2800000
    },
    {
        "id": 3,
        "owner_name": "Harold Nguyen",
        "property_address": "305 6th Street",
        "city": "Austin",
        "state": "TX",
        "property_type": "Mixed Use",
        "sq_ft": 15600,
        "years_owned": 19,
        "assessed_value": 5100000
    },
    {
        "id": 4,
        "owner_name": "Dorothy Kaplan",
        "property_address": "77 Wacker Dr",
        "city": "Chicago",
        "state": "IL",
        "property_type": "Office Building",
        "sq_ft": 22000,
        "years_owned": 38,
        "assessed_value": 9400000
    },
    {
        "id": 5,
        "owner_name": "Frank Deluca",
        "property_address": "210 N Michigan Ave",
        "city": "Chicago",
        "state": "IL",
        "property_type": "Retail Strip",
        "sq_ft": 6800,
        "years_owned": 27,
        "assessed_value": 3600000
    },
    {
        "id": 6,
        "owner_name": "Evelyn Park",
        "property_address": "540 N Wells St",
        "city": "Chicago",
        "state": "IL",
        "property_type": "Warehouse",
        "sq_ft": 31000,
        "years_owned": 22,
        "assessed_value": 6700000
    },
    {
        "id": 7,
        "owner_name": "George Watkins",
        "property_address": "4100 Main St",
        "city": "Houston",
        "state": "TX",
        "property_type": "Office Building",
        "sq_ft": 18500,
        "years_owned": 33,
        "assessed_value": 7200000
    },
    {
        "id": 8,
        "owner_name": "Patricia Mendez",
        "property_address": "1850 Westheimer Rd",
        "city": "Houston",
        "state": "TX",
        "property_type": "Retail Strip",
        "sq_ft": 9400,
        "years_owned": 41,
        "assessed_value": 3100000
    },
    {
        "id": 9,
        "owner_name": "Leonard Brooks",
        "property_address": "620 Travis St",
        "city": "Houston",
        "state": "TX",
        "property_type": "Mixed Use",
        "sq_ft": 11200,
        "years_owned": 29,
        "assessed_value": 4800000
    },
    {
        "id": 10,
        "owner_name": "Barbara Steinberg",
        "property_address": "3200 McKinney Ave",
        "city": "Dallas",
        "state": "TX",
        "property_type": "Office Building",
        "sq_ft": 14700,
        "years_owned": 36,
        "assessed_value": 5900000
    },
    {
        "id": 11,
        "owner_name": "Charles Okafor",
        "property_address": "710 Commerce St",
        "city": "Dallas",
        "state": "TX",
        "property_type": "Warehouse",
        "sq_ft": 42000,
        "years_owned": 18,
        "assessed_value": 8300000
    },
    {
        "id": 12,
        "owner_name": "Helen Russo",
        "property_address": "415 N Akard St",
        "city": "Dallas",
        "state": "TX",
        "property_type": "Retail Strip",
        "sq_ft": 7600,
        "years_owned": 44,
        "assessed_value": 2400000
    }
]


@app.route("/api/properties", methods = ["GET"])
def get_properties():

    city = request.args.get("city","").strip().lower()

    if not city:
        return jsonify({"error" : "Please provide a city"}), 400
    
    results = [p for p in PROPERTIES if p['city'].lower() == city] 

    if not results:
        return jsonify({"error" : f"No result for the city with value {city.title()}"}), 404
    
    return jsonify(results)



@app.route("/api/generate-outreach", methods = ["POST"])
def generate_outreach():
    data = request.json 

    owner = data.get('owner_name')
    property = data.get('property_address')
    city = data.get('city')
    state = data.get('state')
    property_type = data.get('property_type')
    sq_ft = data.get('sq_ft')
    years_owned = data.get('years_owned')
    assessed_value = data.get('assessed_value')

    prompt = f""" You are a commercial real estate broker.
        Write a short, personlized cold call voicemail script for this property owner:

        Owner: {owner}
        Property: {property}
        Years Owned: {years_owned}
        Estimated Value: {assessed_value}

        Rules:
        - Sound human and conversational, not salesy or robotic
        - Mention how long they have owned the property naturally
        - Keep it under 30 seconds when spoken (70 words)
        - End with your name (Alex Carter) and a callback number (512-800-9821)
        - Write ONLY the voicemail  script,  nothing else.
    """

    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        messages= [{"role":"user", "content":prompt}]
    )

    script = response.choices[0].message.content

    return jsonify({"script": script})


if __name__ == '__main__':
    app.run(debug=True, port=5000)