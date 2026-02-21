# python donwnload image
FROM python:3.8-slim

# set work directory
WORKDIR /app

# copy requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# Expose port
EXPOSE 5000

# run app
CMD ["python", "app.py"]
