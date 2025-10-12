FROM python:3.10

WORKDIR /messaging_app

# Copy app files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

