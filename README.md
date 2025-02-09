# Gallery Web Application

A multi-functional gallery web application built with Flask. This project showcases a variety of creative features including:
- **Homepage Details:** The homepage serves as the central hub for the application. It presents an attractive, easy-to-navigate interface that highlights our services and features.
- **Random Art Generation:** Generates random shapes and fractals.
- **Audio Processing:** Upload, modify (change speed, volume, add effects), and download audio files.
- **Data Visualization:** Displays interactive data plots .
- **Image Processing:** Upload images and apply visual effects such as grayscale, sepia, invert, blur, and pixelate.
- **User Authentication:** Includes login and registration pages (requires additional configuration for full functionality).
- **Contact Page:** A dedicated page for users to reach out with inquiries or feedback. 

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Application Routes](#application-routes)
- [Dependencies and Tools](#dependencies-and-tools)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)


## Prerequisites
  - **Git :**  To control your versions and to have your bash shell.
  - **Python:** Version 3.7 or above.
  - **pip:** Python package installer.
  - **FFmpeg:** Required for audio processing with [Pydub](https://github.com/jiaaro/pydub). Ensure FFmpeg is installed and available in your system PATH.

## Installation

  1. **Clone the Repository:**
  
     In your git bash tap the following:
     git clone https://github.com/jawad3213/EdioArt.git
     cd EdioArtGallery
  
  2. **Create a Virtual Environment:**
      python -m venv venv
     Activate the virtual environment: On Windows-->venv\Scripts\activate
                                       On macOS/Linux-->source venv/bin/activate
3. **Install Required Packages:**
    pip install 

## Setup Instructions
    pip install Pygame matplotlib seaborn Pandas PIL pyDub flask pillow plotly

   **Directory Structure:**
     The application expects the following directory structure for storing files:
        **static/uploads** — For storing uploaded files (images and audio).
        **static/modified** — For storing modified audio files.
     The application code will automatically create these folders if they do not exist. However, ensure your environment allows the application to create directories in the project path.
   **Configuration:**
     The Flask application's secret key is set within the code (app.config['SECRET_KEY'] = 'jawad').
     Audio and image upload paths are configured under app.config['UPLOAD_FOLDER'] and app.config['MODIFIED_FOLDER'].
     For audio processing, make sure FFmpeg is installed and correctly configured.

## Running the Application
  To start the Flask development server, simply run: **python main.py**
  The application will start on **http://127.0.0.1:5000/.** Open this URL in your web browser to access the gallery.
    
## Application Routes

Here is a brief overview of the key routes:

!Home Page
- **`/` or `/home`** — Landing page of the application.

!Art Gallery
- **`/Art`** — Displays art-related content.

!Audio Gallery
- **`/Audio`** — Page to upload and process audio files.

!Data Visualizations
- **`/Data `** — For visualizind Data

!Image Processing
- **`/Image`** — Upload images and apply various effects.
- **`/upload`** — Handles image processing requests.
- **`/download/<filename>`** — Allows downloading of processed images.

!User Authentication
- **`/Log In`** — Login page.
- **`/register`** — Registration page (uses a custom `RegisterForm`).

!Utility Route
- **`/generate_shapes`** — Returns a JSON array of randomly generated shapes.

!Contact Page
- **`/Contact`** — Displays a contact form or contact information so users can send inquiries or feedback.

> **Note:** The contact page is designed to be simple and can be enhanced further (for example, by integrating email services or storing messages in a database).

## Dependencies and Tools

    Flask: A lightweight web framework for building web applications.
    Matplotlib: A comprehensive visualization library for creating static, animated, and interactive plots.
    Pandas: A powerful library for data manipulation and analysis.
    NumPy: A library for numerical computing with support for large, multi-dimensional arrays.
    Pillow (PIL): A modern fork of the Python Imaging Library for image processing.
    Pydub: A library for audio manipulation and processing.
    Werkzeug: A utility library for secure file uploads and other web utilities (installed as a Flask dependency).
    Pygame: A set of Python modules designed for game development, handling graphics and sound.
    Seaborn: A statistical data visualization library built on top of Matplotlib.
    Plotly: A graphing library for creating interactive, publication-quality visualizations.

 ## Troubleshooting
 
  **Missing Dependencies:**
    If you encounter errors regarding missing packages, ensure all dependencies are installed. Use pip list to verify.
  **FFmpeg Issues:**
    For audio processing errors, check that FFmpeg is installed and available in your system PATH. You can download FFmpeg from FFmpeg.org.
  **File Permissions:**
    Ensure that the application has write permissions for the static/uploads and static/modified directories. 
  **Port Conflicts:**
    If the default port 5000 is in use, you can specify a different port when running the application by tapping the following in yoiur Terminal:
    python app.py --port 8000

 ## Contact  
    Our Names – El hail Jaouad and Nichan Said 
    Project Link: https://github.com/jawad3213/EdioArt

   

   

   

   

   
