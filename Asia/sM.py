from flask import Blueprint,render_template
sM = Blueprint("sM", __name__, static_folder="static",template_folder="template" )

@sM.route("/Asia")

def Hasia():
    return render_template('home.html')

@sM.route('/helpline')
def helpline():
    return render_template('')