from flask import Flask, request, jsonify
import util 

app = Flask(__name__)
def add_cors_headers(response):
    """✅ Ensure CORS headers are always sent with responses."""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()  
        return jsonify({'locations': locations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
     
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        total_sqft = data.get('total_sqft')
        location = data.get('location')
        bhk = data.get('bhk')
        bath = data.get('bath')

        if not total_sqft or not location or not bhk or not bath:
            return jsonify({"error": "Missing required parameters"}), 400

        total_sqft = float(total_sqft)
        bhk = int(bhk)
        bath = int(bath)

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        return jsonify({'estimated_price': estimated_price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(port=5004, debug=True)
