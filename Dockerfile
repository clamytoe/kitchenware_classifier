FROM python:3.10-slim

# Create metada labels for the image
LABEL com.ogsapien.vendor="OG Sapien"
LABEL com.ogsapien.image.author="clamytoe@gmail.com"
LABEL version="1.0.0"
LABEL description="Kitchenware Classifier"

# Install pipenv to manage dependencies
RUN pip install pipenv

# Set working directory
WORKDIR /app

# Install the required files into the system
# and not into a virtual environment
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

# Copy required files
COPY api.py kw_router.py fastai_model.pkl favicon.ico /app/

# Expose the needed port and start the server
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
