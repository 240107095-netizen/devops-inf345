FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PORT=8080

RUN useradd --system --create-home --uid 10001 app

WORKDIR /app

COPY app.py ./

USER 10001:10001

EXPOSE 8080

CMD ["python3", "app.py"]
