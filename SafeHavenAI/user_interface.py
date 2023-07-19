from flask import Flask, render_template, request
import json

app = Flask(__name__)

INTERFACE_DATA = {}

@app.route('/')
def render_interface():
    return render_template('index.html', data=INTERFACE_DATA)

@app.route('/user-settings', methods=['POST'])
def update_user_settings():
    INTERFACE_DATA['user_settings'] = request.get_json()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/report-section', methods=['GET'])
def get_report():
    return json.dumps(INTERFACE_DATA['report_data']), 200, {'ContentType':'application/json'} 

@app.route('/real-time-detection', methods=['GET'])
def get_real_time_detection():
    return json.dumps(INTERFACE_DATA['real_time_detection_data']), 200, {'ContentType':'application/json'} 

@app.route('/automated-response', methods=['GET'])
def get_automated_response():
    return json.dumps(INTERFACE_DATA['automated_response_data']), 200, {'ContentType':'application/json'} 

@app.route('/support-section', methods=['GET'])
def get_support():
    return json.dumps(INTERFACE_DATA['support_data']), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(debug=True)