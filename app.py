import os
import pdfkit
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = {
        "name": request.form.get('name', ''),
        "email": request.form.get('email', ''),
        "phone": request.form.get('phone', ''),
        "address": request.form.get('address', ''),
        "photo": request.form.get('photo', ''),
        "theme": request.form.get('theme', 'light'),
        "about": request.form.get('about', ''),
        "education": request.form.get('education', ''),
        "skills": request.form.get('skills', ''),
        "projects": request.form.get('projects', ''),
        "experience": request.form.get('experience', ''),
        "internships": request.form.get('internships', ''),
        "certifications": request.form.get('certifications', ''),
        "languages": request.form.get('languages', ''),
        "interests": request.form.get('interests', ''),
        "achievements": request.form.get('achievements', ''),
        "links": request.form.get('links', '')
    }

    # Choose template based on theme
    template_file = "resume_template_dark.html" if data["theme"] == "dark" else "resume_template_light.html"

    # Render the HTML using selected theme
    rendered_html = render_template(template_file, **data)

    # Configure PDF generation (based on OS)
    wkhtml_path = (
        'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe' if os.name == 'nt'
        else '/usr/bin/wkhtmltopdf'
    )
    config = pdfkit.configuration(wkhtmltopdf=wkhtml_path)

    # Generate PDF from rendered HTML
    pdf = pdfkit.from_string(rendered_html, False, configuration=config)

    print("✅ PDF generated successfully")

    return (
        pdf,
        200,
        {
            'Content-Type': 'application/pdf',
            'Content-Disposition': f'inline; filename={data["name"].replace(" ", "_")}_resume.pdf'
        }
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
