from flask import Flask,render_template,jsonify
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
import random

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_adress= StringField(label='email address')
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    submit=SubmitField(label='submit')
    

 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jawad'  

# generate forrms 
def generate_random_shapes(n=10):
    shapes = []
    for _ in range(n):
        shape_type = random.choice(["circle", "square", "triangle"])
        x = random.randint(50, 300)  
        y = random.randint(50, 300)  
        size = random.randint(30, 70)
        color = [random.randint(0, 255) for _ in range(3)]

        shape = {
            "type": shape_type,
            "x": x,
            "y": y,
            "size": size,
            "color": f"rgb({color[0]}, {color[1]}, {color[2]})"
        }
        shapes.append(shape)

    return shapes
 
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/Art')
def Artpage():
    return render_template('Art.html')

@app.route('/Data')
def Datapage():
    return render_template('Data.html')

@app.route('/Image')
def Imagepage():
    return render_template('Image.html')

@app.route('/Audio')
def Audiopage():
    return render_template('Audio.html')

@app.route('/register')
def registerpage():
    form=RegisterForm()
    return render_template('register.html',form=form)
@app.route("/generate_shapes")
def generate_shapes():
    shapes = generate_random_shapes()
    return jsonify(shapes)


if __name__ == "__main__":
    app.run(debug=True)