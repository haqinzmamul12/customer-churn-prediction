# Use base python image 
FROM python:3.13.2-slim

# create default directory 
WORKDIR /app 

# copy code from source to destination 
COPY . . 

# upgrade pip & install dependencies 
RUN pip install pip --upgrade pip && pip install -r requirements.txt 

# Expose streamlit port
EXPOSE 8501 

# Run streamlit app
CMD ["streamlit", "run", "app.py", "--server.headless", "true"]