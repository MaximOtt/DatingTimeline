import subprocess

def build_docker_image():
    # Execute the Docker build command to create or update the image
    subprocess.run(['docker', 'build', '-t', 'aab', '.'])

def run_docker_container():
    # Run a Docker container from the image
    subprocess.run(['docker', 'run', '-d', '-p', '8000:8000', '--name', 'aaa', 'aab'])

# Build the Docker image
build_docker_image()

# Run the Docker container
run_docker_container()
