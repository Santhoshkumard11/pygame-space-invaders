FROM python

# Set the working directory
WORKDIR /usr/src/app

# Install the application dependencies
RUN pip install -r requirements.txt

# Copy the application source code to the working directory
COPY . .

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["pygbag", ".\space_invaders"]