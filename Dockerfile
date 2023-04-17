FROM python:3.8-buster

RUN apt-get -y update && apt install -y ffmpeg
# Copy source and install dependencies
RUN mkdir -p /opt/sandy_inspires/space_invaders/
COPY . /opt/sandy_inspires/space_invaders/
WORKDIR /opt/sandy_inspires/space_invaders/
RUN pip install --upgrade pip

# Install the application dependencies
RUN pip install --trusted-host pypi.python.org  --trusted-host pypi.org --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Start the application - this is for dev purpose only
CMD pygbag --title "Sandy Inspires - Space Invaders" --app_name "Sandy Inspires - Space Invaders" /opt/sandy_inspires/space_invaders
