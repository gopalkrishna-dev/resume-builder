import os
import pdfkit
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Collect form data (adjust as needed)
    name = request.form['name']
    email = request.form['email']

    # Render resume with provided data
    rendered = render_template('resume_template.html', name=name, email=email)

    # Use wkhtmltopdf from the standard Linux path on Render
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    # Generate PDF from HTML
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    return (
        pdf,
        200,
        {'Content-Type': 'application/pdf', 'Content-Disposition': 'inline; filename=resume.pdf'}
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
