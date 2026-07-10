from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
from datetime import datetime
from weasyprint import HTML
import secrets

load_dotenv()

env = Environment(
    loader=FileSystemLoader("app/templates")
)


def _generate_certificate_number() -> str:
    year = datetime.now().year
    random_suffix = secrets.token_hex(3).upper()

    return f"BDP-{year}-{random_suffix}"

def _render_template(donor_name: str, certificate_number: str, issued_date: str,):
    
    template = env.get_template("certificate.html")

    return template.render(
        donor_name=donor_name,
        certificate_number=certificate_number,
        issued_date=issued_date,
    )


def generate_consent_certificate(donor_name: str):
    
    certificate_number = _generate_certificate_number()
    issued_date = datetime.now().strftime("%d %B %Y")
    
    html = _render_template(donor_name = donor_name, certificate_number = certificate_number, issued_date = issued_date,)
       
    pdf_bytes = HTML(string= html).write_pdf()
    
    
    return certificate_number, pdf_bytes



if __name__ == "__main__":
    certificate_number, storage_path = generate_consent_certificate(
        donor_name="Vivek Mandal"
    )

    print(certificate_number)
    print(storage_path)