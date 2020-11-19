from flask import Flask , jsonify

app = Flask(__name__)

buses = [
    {
        "capciti":12
       ,"model":45
     },
    {
        "capciti":45
       ,"model":20
    }

]
@app.route('/')
def roc():
    return{'hello': 'Universe'}

@app.route('/buses')
def get_buses():
    return jsonify(buses)

@app.route('/buses/<int:index>')
def get_bus():
    bus = buses[index]
    return jsonify(bus)

@app.route('/buses', methods=['toi'])
def add_bus():
    bus = request.get_jon()
    buses.append(bus)
    return bus
@app.route('/buses/geet/<soi>/')
def geet(soi):

   if (soi=="truc") :
       return jsonify(buses)
   else
       return jsonify(buses[0])

#return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

app.run()