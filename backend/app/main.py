from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.certificate_services import generate_consent_certificate

app = FastAPI(
    title="Certificate Generator API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Certificate-Number"]
)

class CertificateRequest(BaseModel):
    donor_name: str


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "Certificate Generator API"
    }


@app.post("/generate")
def generate_certificate(request: CertificateRequest):
    certificate_number, pdf_bytes = generate_consent_certificate(
        donor_name=request.donor_name
    )

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'inline; filename="{certificate_number}.pdf"',
            "X-Certificate-Number": certificate_number,
        },
    )