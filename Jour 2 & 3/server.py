from flask import Flask
from startCafe import myblockchain
from flask import jsonify, render_template, request, redirect
app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template(
        "index.html",
        blocks=myblockchain.get_all()
    )


@app.route('/block/<blockIndex>')
def block_element(blockIndex):
    block = myblockchain.get_block(int(blockIndex))
    res = block.__dict__ if block != False else jsonify(error="ce block  n'existe pas")
    return res

@app.route('/block/view/<blockIndex>')
def block_element_view(blockIndex):
    return render_template(
        "block.html",
        block=myblockchain.get_block(int(blockIndex))
    )

@app.route('/block/form')
def block_element_add():
    return render_template("add.html")

@app.route('/block', methods=['POST', 'GET'])
def add_block():
    if request.method == 'POST':
        body = request.form['block_body']
        myblockchain.add(body)
        return redirect("/", code=201)
    elif request.method == 'GET':
        return jsonify(myblockchain.get_all())
    return 'yolo'