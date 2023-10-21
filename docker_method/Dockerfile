FROM python:3.9-slim

# Set directory in the container
WORKDIR /htmlproject

# Copy HTML file into the container (here we have called it index, this is a default)
COPY data_table.html /htmlproject
COPY index.html /htmlproject


# Expose port 8000... standard
EXPOSE 8000

# Start web server
CMD ["python", "-m", "http.server", "8000"]

#in this case we are using a very simply python web server but we can upgrade it to another ie apache if needed later
