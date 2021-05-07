from ast import literal_eval
import io

import numpy as np
from flask import Flask, render_template, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns

from Main import Main

app = Flask(__name__)


@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        points = request.form['points']
        points = [literal_eval(coord) for coord in points.split()]
        degree = int(request.form['deg'])
        main = Main()
        main.create_lists_web(points, degree)
        fig = create_figure(main.x_list, main.y_list, main.get_model_result_web(), degree)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
    else:
        return render_template("index.html")


def create_figure(x_vals, y_vals, soln_matrix, degree):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    sns.set_theme(palette='deep')
    sns.axes_style("darkgrid")
    sns.set_style("white")
    t = np.arange(min(x_vals) - 1, max(x_vals) + 1, 0.1)
    axis.plot(t, reg(t, soln_matrix, degree), 'red', x_vals, y_vals, 'bo')
    return fig


def reg(t, soln_matrix, degree):
    eqn = soln_matrix[0]
    for x in range(1, degree + 1):
        eqn = eqn + soln_matrix[x] * t ** x
    return eqn


if __name__ == "__main__":
    app.run(debug=True)
