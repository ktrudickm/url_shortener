# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of your project into the container
COPY . /code/

# Set the PYTHONPATH environment variable
ENV PYTHONPATH /code

# Command to run the application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]



