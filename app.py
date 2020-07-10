from unittest.main import main
from flask import Flask, request
from flask.json import jsonify
from db import create_tech_db, get_tech_db


web_app = Flask('web_app')

@web_app.route('/tech/<string:nome>')
def get_tech(nome):
  return jsonify('Ok'), 200

@web_app.route('/tech', methods=['POST'])
def create_tech():
  nome = request.json.get('nome')
  descricao = request.json.get('descricao')
  create_tech_db(nome, descricao)
  return jsonify('Ok'), 201


if __name__ == "__main__":
    web_app.run()