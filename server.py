from flask import Flask, request, jsonify, render_template 
app = Flask(__name__) 
# Зберігаємо поточні дані про погоду 
weather_data = { 
"temperature": 0.0, 
"humidity": 0.0, 
"pressure": 0.0 
} 
@app.route('/update', methods=['POST']) 
def update_weather(): 
    global weather_data 
    data = request.json 
    weather_data['temperature'] = data.get('temperature', weather_data['temperature']) 
    weather_data['humidity'] = data.get('humidity', weather_data['humidity']) 
    weather_data['pressure'] = data.get('pressure', weather_data['pressure']) 
    return jsonify({"status": "success"}), 200 
@app.route('/current_weather', methods=['GET']) 
def get_weather(): 
    return jsonify(weather_data), 200 
@app.route('/') 
def index(): 
    return render_template('index.html') 
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')
