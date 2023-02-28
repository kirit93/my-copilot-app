# python 3.10 base image
FROM python:3.10

# create copy of src into /app to run
COPY src/ /app
WORKDIR /app

# install app requirements
COPY requirements.txt /app
RUN apt-get update && \
    pip install --upgrade pip && pip install -r requirements.txt

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install 

# run FastAPI app using gunicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]