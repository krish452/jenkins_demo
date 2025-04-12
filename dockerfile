# Step 1: Use an official Python image as a base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Step 4: Copy the entire project into the container
COPY . /app/

# Step 5: Expose the port your app will run on
EXPOSE 5000

# Step 6: Command to run your app
CMD ["python", "app.py"]
