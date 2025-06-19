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
    
    rendered = render_template('resume_template.html', name=name, email=email)

    # ✅ Detect platform and set wkhtmltopdf path
    if os.name == 'nt':  # Windows (local)
        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    else:  # Render (Linux)
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    pdf = pdfkit.from_string(rendered, False, configuration=config)

    return (
        pdf,
        200,
        {'Content-Type': 'application/pdf', 'Content-Disposition': 'inline; filename=resume.pdf'}
    )

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))  # Render dynamically gives this
    app.run(host='0.0.0.0', port=port)

