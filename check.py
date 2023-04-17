from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files
    # process the uploaded file here
    print(request.files,request.form)
    a=request.form
    bookname = a["bookname"]
    authorname = a["authorname"]
    category = a["category"]
    contentst = a["contentst"]
    contentend = a["contentend"]
    upload=file['upload'].filename
    pdfname = file['pdfphoto'].filename



    response = jsonify({'message': 'File uploaded successfully!'})
    return response
@app.route('/api/my-endpoint')
def my_endpoint():
    # Your endpoint logic here
    response = jsonify({'message': 'Hello, world!'})

    # Set the Access-Control-Allow-Origin header to allow requests from any domain
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    app.run(debug=True)
