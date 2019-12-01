import os
from Crypto.Hash import SHA256
from flask import Flask, render_template, request, send_from_directory, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return "hello world!"

@app.route('/<path:path>')
def serve(path):
	print("serve")
	if path != "" and os.path.exists("./templates" + path):
		return send_from_directory('./templates', path)
	else:
		return send_from_directory('./templates', 'index.html')

@app.route('/sha', methods=['POST'])
def sha():
	m = request.get_json()
	h = SHA256.new()
	h.update(m['data'].encode('utf-8'))
	return jsonify({'sha_value': h.hexdigest()})

@app.route('/test', methods=['GET','POST'])
def test():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug='true')
	# app.run(host='0.0.0.0', port='80', debug='true')