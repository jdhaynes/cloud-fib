FROM python:3.8-alpine

WORKDIR /app

# Install dependencies.
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy project files into container.
COPY . .

# Port for Flask app served from gunicorn.
EXPOSE 5000

# Start up gunicorn server on port 5000 for Flask app.
CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:5000", "app:app"]