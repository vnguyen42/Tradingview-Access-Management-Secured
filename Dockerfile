# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies files to the working directory
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . /app/

# Expose the port your application runs on (if applicable)
EXPOSE 3000

# Set the default command to run your application
CMD ["poetry", "run", "python", "main.py"]

# Pass env of coolify
ARG API_KEY=10f3c175-d949-4827-9f7f-9690b383c379
ARG tvpassword=@SdfjeXI8362$$
ARG tvusername=ukomeiz