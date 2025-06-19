from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'summary': request.form['summary'],
        'education': request.form['education'],
        'skills': request.form['skills'],
        'projects': request.form['projects'],
        'experience': request.form['experience'],
        'certifications': request.form['certifications']
    }

    # Render HTML with data
    rendered = render_template('resume_template.html', **data)

    # Configure wkhtmltopdf path
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')  # ← your wkhtmltopdf path

    # Generate PDF from rendered HTML
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    # Send PDF as downloadable file
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'

    return response


if __name__ == '__main__':
    app.run(debug=True)
