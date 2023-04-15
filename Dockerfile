FROM python:3.8-buster

# Xopy source and install dependencies
RUN mkdir -p /opt/sandy_inspires/space_invaders/
COPY . /opt/sandy_inspires/space_invaders/
WORKDIR /opt/sandy_inspires/space_invaders/
RUN pip install --upgrade pip

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Start the application - this is for dev purpose only
CMD ["pygbag", "/opt/sandy_inspires/space_invaders/"]