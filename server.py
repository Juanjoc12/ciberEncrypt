from flask import Flask, escape, request
from encryptMine import *
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/encrypt', methods=['POST'])
def encrypt():    
    ap1 = encryptMine()
    key = request.get_json()['key'].lower()
    message = request.get_json()['message'].lower()
    encryptmessage = ap1.encryptMessage(key,message)#clave, message
   # print(ap1.matrix)
    # need posted data here
    return encryptmessage

@app.route('/decrypt', methods=['POST'])
def decrypt():    
    ap2 = encryptMine()
    key = request.get_json()['key'].lower()
    message = request.get_json()['message'].lower()
    decryptMessage = ap2.decryptMessage(key,message)#clave, message
   # print(ap1.matrix)
    # need posted data here
    return decryptMessage

@app.route('/foundkey', methods=['POST'])
def foundKey():    
    ap1 = encryptMine()
    message = request.get_json()['message'].lower()
    foundSecuencies = ap1.foundSecuencies(message)#clave, message
   # print(ap1.matrix)
    # need posted data here
    return "decryptMessage"