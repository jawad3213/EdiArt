from flask import Flask, render_template, jsonify
from forms import RegisterForm
import random
import io
import base64
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from flask import Flask, request, render_template, send_file, redirect, url_for
from PIL import Image, ImageFilter, ImageOps
import os
from werkzeug.utils import secure_filename

# Configure Matplotlib for non-interactive environments
matplotlib.use('Agg')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jawad'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['AUDIO_FOLDER'] = os.path.join('static', 'audio')
# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['AUDIO_FOLDER']):
    os.makedirs(app.config['AUDIO_FOLDER'])












def generate_random_shapes(n=30):
    shapes = []
    for _ in range(n):
        shape_type = random.choice(["circle", "square", "triangle", "mandelbrot", "julia"])
        x = random.randint(50, 300)
        y = random.randint(50, 300)
        size = random.randint(30, 70)
        color = [random.randint(0, 255) for _ in range(3)]

        if shape_type == "mandelbrot":
            shape = {
                "type": "mandelbrot",
                "x": x,
                "y": y,
                "size": size,
                "color": f"rgb({color[0]}, {color[1]}, {color[2]})",
                "max_iter": random.randint(50, 200)
            }
        elif shape_type == "julia":
            shape = {
                "type": "julia",
                "x": x,
                "y": y,
                "size": size,
                "color": f"rgb({color[0]}, {color[1]}, {color[2]})",
                "c_real": random.uniform(-1, 1),
                "c_imag": random.uniform(-1, 1),
                "max_iter": random.randint(50, 200)
            }
        else:
            shape = {
                "type": shape_type,
                "x": x,
                "y": y,
                "size": size,
                "color": f"rgb({color[0]}, {color[1]}, {color[2]})"
            }
        shapes.append(shape)

    return shapes

# Route pour générer des formes aléatoires
@app.route("/generate_shapes")
def generate_shapes_route():
    shapes = generate_random_shapes()
    return jsonify(shapes)

# Helper function to generate random shapes


# Routes
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/Art')
def Artpage():
    return render_template('Art.html')



@app.route('/Log In')
def Loginpage():
    return render_template('LogIn.html')

@app.route('/register')
def registerpage():
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route('/Data v1')
def Datapage():
    n_points = 100
    df = pd.DataFrame({"Value": np.random.randint(10, 100, size=n_points)})
    theta = np.linspace(0, 4 * np.pi, n_points)
    r = df["Value"].values + np.random.uniform(0, 5, size=n_points)

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection='polar')
    scatter = ax.scatter(theta, r, c=r, cmap='magma', alpha=0.7, s=r*2, edgecolor='white')
    
    ax.set_facecolor("#111111")
    ax.grid(False)
    ax.spines['polar'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title("Abstract Polar Swirl", color='white', fontsize=16, pad=20)

    cbar = plt.colorbar(scatter, pad=0.1)
    cbar.set_label("Data Value", color='white')
    cbar.outline.set_edgecolor('white')
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', facecolor='#111111')
    plt.close()
    plot_data = base64.b64encode(buf.getvalue()).decode("utf-8")

    return render_template("Data.html", plot_data=plot_data)

@app.route('/Data v2')
def Datapage1():
    n_points = 300
    t = np.linspace(0, 4 * np.pi, n_points)
    radius = np.linspace(0.5, 2.5, n_points) + np.random.rand(n_points) * 0.3
    x, y, z = radius * np.cos(t), radius * np.sin(t), t
    color_values = radius * z

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=color_values, cmap='magma', alpha=0.8, s=15)

    ax.set_facecolor("black")
    fig.patch.set_facecolor('black')
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    plt.title("3D Spiral Art", color='white', fontsize=16, pad=20)

    cbar = plt.colorbar(scatter, shrink=0.65, pad=0.1)
    cbar.set_label('Abstract Color Scale', color='white')
    cbar.outline.set_edgecolor('white')
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')

    ax.view_init(elev=20, azim=120)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', facecolor=fig.get_facecolor())
    plt.close(fig)
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template("Data1.html", plot_data=plot_data)
# audiooooooooooooooooooooooooo
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from pydub import AudioSegment
import os
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
from pydub import AudioSegment

from pydub import AudioSegment
from pydub.utils import which
UPLOAD_FOLDER = 'static/uploads'
MODIFIED_FOLDER = 'static/modified'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MODIFIED_FOLDER'] = MODIFIED_FOLDER

# Extensions de fichiers audio autorisés
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg', 'flac'}

# Fonction pour vérifier l'extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Si un fichier est téléchargé
            if 'audio_file' in request.files:
                file = request.files['audio_file']
                if file.filename == '':
                    return 'No selected file', 400
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)

                    # Charger l'audio original
                    audio = AudioSegment.from_file(filepath)

                    # Sauvegarder l'audio original
                    original_filepath = os.path.join(app.config['MODIFIED_FOLDER'], f"original_{filename}")
                    audio.export(original_filepath, format="mp3")

                    # Renvoyer la page avec l'audio original
                    return render_template('Audio.html', audio_url_original=f'uploads/{filename}', audio_url_modified=None)

            # Si le bouton "Apply Modification" est cliqué
            if 'apply_modification' in request.form:
                filename = request.form['filename']  # Récupérer le filename du formulaire
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # Vérifier si le fichier existe
                if not os.path.exists(filepath):
                    return 'File not found', 404

                # Charger l'audio
                audio = AudioSegment.from_file(filepath)

                # Appliquer des modifications
                speed = float(request.form.get('speed', 1.0))
                volume = float(request.form.get('volume', 0))  # Volume en dB
                effects = request.form.get('effects', 'none')
                layer_audio = request.files.get('layer_audio')  # Pour ajouter un fichier audio supplémentaire à superposer

                # Appliquer les effets
                if speed != 1.0:
                    audio = audio.speedup(playback_speed=speed)

                if volume != 0:
                    audio = audio + volume  # Modifier le volume en dB

                if effects == 'echo':
                    audio = audio.reverse()  # Exemple d'effet (echo simple)

                # Superposition de sons
                if layer_audio:
                    layer_filename = secure_filename(layer_audio.filename)
                    layer_filepath = os.path.join(app.config['UPLOAD_FOLDER'], layer_filename)
                    layer_audio.save(layer_filepath)

                    # Charger le clip à superposer
                    overlay_audio = AudioSegment.from_file(layer_filepath)

                    # Superposer les sons
                    audio = audio.overlay(overlay_audio)

                # Sauvegarder l'audio modifié
                modified_filename = f"modified_{filename}"
                modified_filepath = os.path.join(app.config['MODIFIED_FOLDER'], modified_filename)

                # Vérifier si le dossier existe, sinon le créer
                if not os.path.exists(app.config['MODIFIED_FOLDER']):
                    os.makedirs(app.config['MODIFIED_FOLDER'])

                audio.export(modified_filepath, format="mp3")

                # Afficher l'audio modifié
                return render_template('Audio.html', audio_url_original=f'uploads/{filename}', audio_url_modified=f'modified/{modified_filename}')

        except Exception as e:
            print(f"Error: {str(e)}")
            return f"An error occurred: {str(e)}", 500

    return render_template('Audio.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/modified/<filename>')
def modified_file(filename):
    return send_from_directory(app.config['MODIFIED_FOLDER'], filename)







@app.route('/Audio')
def Audiopage():
    return render_template('Audio.html')



@app.route('/Image')
def Imagepage():
    return render_template('Image.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    effect = request.form.get('effect')
    filename = secure_filename(file.filename)
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(original_path)

    image = Image.open(original_path)

    if effect == 'grayscale':
        image = ImageOps.grayscale(image)
    elif effect == 'sepia':
        image = ImageOps.colorize(ImageOps.grayscale(image), '#704214', '#C0A080')
    elif effect == 'invert':
        image = ImageOps.invert(image)
    elif effect == 'blur':
        image = image.filter(ImageFilter.BLUR)
    elif effect == 'pixelate':
        image = image.resize((image.width // 10, image.height // 10), resample=Image.BILINEAR)
        image = image.resize((image.width * 10, image.height * 10), resample=Image.NEAREST)

    processed_filename = f'processed_{filename}'
    processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
    image.save(processed_path)

    return render_template('Image.html', 
                           original_image=url_for('static', filename=f'uploads/{filename}'), 
                           processed_image=url_for('static', filename=f'uploads/{processed_filename}'),
                           download_link=url_for('download_file', filename=processed_filename))

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
     
   
      app.run(debug=True)
