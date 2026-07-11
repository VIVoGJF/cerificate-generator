# Certificate Generator

A lightweight web application that generates professional **Certificates** in PDF format.

The certificate is designed using **HTML and CSS** and rendered into a PDF using **WeasyPrint**, allowing modern web technologies to produce print-ready documents.



## Live Demo

https://cerificate-generator-vert.vercel.app/

## Tech Stack

- FastAPI
- WeasyPrint
- Jinja2
- HTML, CSS, JavaScript
- Docker

## How It Works

1. Enter the donor's name.
2. FastAPI renders the HTML certificate using a Jinja2 template.
3. WeasyPrint converts the rendered HTML and CSS into a PDF.
4. The generated PDF is returned to the browser for download.

## Run Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the frontend using Live Server or any static web server.

Since WeasyPrint depends on native system libraries, the backend is containerized with **Docker** for a consistent deployment environment.

## Docker

```bash
docker build -t certificate-generator .
docker run -p 8000:8000 certificate-generator
```
