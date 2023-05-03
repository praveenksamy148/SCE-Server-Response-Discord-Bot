FROM python:3.8
ADD serverMonitor.py . 
RUN pip install requests 
WORKDIR /discord_notifications
COPY package.json . 
COPY package-lock.json . 
# EXPOSE 5000 
CMD [ "python", "serverMonitor.py" ]
