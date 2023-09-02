import functools

from zplanedesigner.cook import generate_z_plane, generate_freq_resp

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from zplanedesigner.db import get_db

bp = Blueprint('designer', __name__, url_prefix='/designer')

@bp.route('/main', methods = ["GET","POST"])
def main():

    if request.method == "POST":

        zeros_1_x = float(request.form['zero_1_x'])
        zeros_1_y = float(request.form['zero_1_y'])

        poles_1_x = float(request.form['pole_1_x'])
        poles_1_y = float(request.form['pole_1_y'])

        if zeros_1_y != 0:
            zeros = [(zeros_1_x, zeros_1_y), (zeros_1_x,-zeros_1_y)]
        else:
            zeros = [(zeros_1_x,zeros_1_y)]

        if poles_1_y != 0:
            poles = [(poles_1_x, poles_1_y), (poles_1_x,-poles_1_y)]
        else:
            poles = [(poles_1_x,poles_1_y)]

        zplane_route = generate_z_plane(zeros, poles)
        freq_resp_rout = generate_freq_resp(zeros, poles)

        return redirect(url_for('designer.main'))

    return render_template('designer/main.html')