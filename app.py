import os
import pdfkit
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    about = request.form.get('about', '')
    education = request.form.get('education', '')
    skills = request.form.get('skills', '')
    projects = request.form.get('projects', '')
    experience = request.form.get('experience', '')
    certifications = request.form.get('certifications', '')

    rendered = render_template(
        'resume_template.html',
        name=name,
        email=email,
        phone=phone,
        about=about,
        education=education,
        skills=skills,
        projects=projects,
        experience=experience,
        certifications=certifications
    )

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    return (
        pdf,
        200,
        {'Content-Type': 'application/pdf', 'Content-Disposition': 'inline; filename=resume.pdf'}
    )



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
