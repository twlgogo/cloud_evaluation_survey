import os

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def html_index():
    return render_template("index.html")

@app.route('/post')
def html_get():
    matrix = request.args.get('matrix', default = '*', type = str)
    f = open("vectors.txt", "a+")
    f.write(matrix)
    f.write("\n")
    f.close()
    return "ok"

@app.route('/vectors.txt')
def html_vectors():
    return send_from_directory(app.root_path, 'vectors.txt', mimetype='text/plain')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8000.
    port = int(os.environ.get('PORT', 8000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
