import argparse
import os
import subprocess
import sys

# Define the parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", action="store_true", help="Start the Docker container")
parser.add_argument("-t", "--stop", action="store_true", help="Stop the Docker container and remove the Docker image")

# Parse the arguments
args = parser.parse_args()

# Run the Docker container
if args.start:
    # Check if Docker is installed
    try:
        subprocess.run(["docker", "ps"], check=True)
    except subprocess.CalledProcessError:
        # Docker is not installed, install it
        print("Docker is not installed on your machine.")
        sys.exit(1)

    # Get the local directory from the command line
    local_directory = input("Enter the local directory: ")

    # Check if the local directory exists
    if not os.path.exists(local_directory):
        print("The local directory does not exist.")
        exit()

    # Create the Dockerfile
    with open(os.path.join(local_directory, "Dockerfile"), "w") as f:
        f.write("""
    FROM nginx

    WORKDIR /usr/share/nginx/html

    VOLUME /usr/share/nginx/html

    EXPOSE 80

    CMD ["nginx", "-g", "daemon off;"]
    """)

    # Build the Docker image
    subprocess.run(["docker", "build", "-t", "my-web-server", local_directory])
    # Run the Docker container
    subprocess.run(["docker", "run", "-d", "-p", "80:80", "-v", f"{local_directory}:/usr/share/nginx/html", "--name", "my-nginx-container", "my-web-server"])
    print("Open a web browser and navigate to http://localhost, and dont forget to point to your file. i.e. http://localhost/1.html")

# Stop the Docker container and remove the Docker image
if args.stop:
    subprocess.run(["docker", "stop", "my-nginx-container"])
    subprocess.run(["docker", "container", "rm", "my-nginx-container"])
    subprocess.run(["docker", "rmi", "my-web-server"])
    # Open a web browser and navigate to http://localhost
    print("Docker stopped, deleted and image removed")
