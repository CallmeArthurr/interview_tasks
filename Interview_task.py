from flask import Flask, jsonify
from power_grid import run_simulation


app = Flask(__name__)


@app.route('/grid-power-analysis/')
def grid_power_analysis():
    # Run the simulation
    net = run_simulation()

    # Initialize the response dictionary
    result = {
        "Load": {},
        "generators": {},
        "external_grid": {},
        "sgenerators": {}
    }

    # Populate the response dictionary with the active and reactive power values for each node
    for load in net.load.index:
        result["Load"][load] = (net.res_load.p_mw[load], net.res_load.q_mvar[load])
    for gen in net.gen.index:
        result["generators"][gen] = (net.res_gen.p_mw[gen], net.res_gen.q_mvar[gen])
    for ext_grid in net.ext_grid.index:
        result["external_grid"][ext_grid] = (net.res_ext_grid.p_mw[ext_grid], net.res_ext_grid.q_mvar[ext_grid])
    for sgen in net.sgen.index:
        result["sgenerators"][sgen] = (net.res_sgen.p_mw[sgen], net.res_sgen.q_mvar[sgen])

    # Return the response as JSON
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
