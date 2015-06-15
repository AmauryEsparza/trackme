from flask import request, jsonify, abort, Response
from bson.json_util import dumps
from trackme import app
from . import db

rutasColl = db.ruta

@app.route('/api/rutas', methods=['GET'])
def get_routes():
	if request.method == 'GET':
		json_results = []
		for result in rutasColl.find():
			json_results.append(result)
			print(json_results)
		return Response(dumps(json_results), mimetype='application/json')

@app.route('/api/rutas/<int:index>', methods=['GET'])
def get_route(index):
	print(index)
	if request.method == 'GET':
		json_result = []
		for result in rutasColl.find({'numero': str(index)}):
			json_result.append(result)
			print(json_result)
		return Response(dumps(json_result), mimetype='application/json')

@app.route('/api/track/rutas/<int:index>', methods=['GET'])
def get_last_position(index):
	if request.method == 'GET':
		json_result = []
		for result in db.ruta.find({'numero': str(index)}, {'coordenadas':{'$slice':-1}}):
			if result["coordenadas"]:
				print(result["coordenadas"])
				dbRef = result["coordenadas"].pop()
				print(dbRef)
				print(db.dereference(dbRef))
				json_result.append(db.dereference(dbRef))
		return Response(dumps(json_result), mimetype='application/json')

#for result in rutasColl.find({'numero': str(index)}, {'coordenadas':{'$slice': -1}}):
#			json_result.append(result)
#			print(result)
#		return Response(dumps(json_result), mimetype='application/json')
