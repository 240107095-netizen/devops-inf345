FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PORT=8080

RUN useradd --system --create-home --uid 10001 app

WORKDIR /app

COPY app.py ./

USER app

EXPOSE 8080

CMD ["python3", "app.py"]
