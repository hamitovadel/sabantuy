#FROM ubuntu:18.04
FROM python:3.8.3
WORKDIR /app
COPY ./ /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install flask gunicorn
ENV PYTHONPATH=/app
CMD [ \
    "gunicorn", \
    "--bind", "0.0.0.0:8080", \
    "--workers", "2", \
    "--threads", "8", \
    "main:app" \
]
