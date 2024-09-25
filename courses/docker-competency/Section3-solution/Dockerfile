# Use AlmaLinux as the base image
FROM almalinux:9

# Set the working directory
WORKDIR /app

# Install Python 3, curl, and build dependencies
RUN dnf install -y python3 python3-devel && \
    dnf clean all

# Install Flask
RUN pip install Flask

# Copy the project files (including pyproject.toml and poetry.lock) into the container
COPY ./simpleapi /app

# Expose port 5000 to allow access to the Flask service
EXPOSE 5000

# Run the Flask app
CMD [ "python3", "app.py"]
