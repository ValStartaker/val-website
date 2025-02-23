from flask import Flask, request, send_file, jsonify
from parliamentarch import get_svg_from_attribution, SeatData
import json
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('parliament.html')

@app.route('/generate-parliament', methods=['POST'])
def generate_parliament():
    try:
        data = request.json
        
        # Convert the party data to SeatData objects
        seat_data = {}
        for party in data['attrib']:
            seats = party.pop('nseats', 1)
            # Ensure border_size is converted to float
            if 'border_size' in party:
                party['border_size'] = float(party['border_size'])
            seat_data[SeatData(**party)] = seats
        
        # Replace the attrib list with the seat_data dictionary
        data['attrib'] = seat_data
        
        # Generate the SVG
        svg = get_svg_from_attribution(**data)
        
        return svg, 200, {'Content-Type': 'image/svg+xml'}
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000)