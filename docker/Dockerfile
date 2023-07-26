FROM mcr.microsoft.com/playwright/python:v1.36.0-jammy

WORKDIR /app

ARG PORT=5000
ENV FLASK_APP "project"
ENV FLASK_DEBUG "1"
ENV PORT=${PORT}

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# running Flask as a module, we sleep a little here to make sure that the DB is fully instanciated before running our app'
CMD sh -c "sleep 5" && python3 -m flask run --host 0.0.0.0 --port ${PORT}
