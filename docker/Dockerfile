# 1. Use an official lightweight Python image
FROM python:3.11-slim
# You aren't choosing the version based on what you have installed locally;
# you are choosing the version that is most stable and guaranteed to work
# everywhere you deploy your application.

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file (we will create this in a moment)
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your source code
COPY . .

# 6. Define the command to run your app
CMD ["python", "src/main.py"]