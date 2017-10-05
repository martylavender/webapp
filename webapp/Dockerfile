FROM python:3.6

# Add code
ADD ./viewtracker /srv/viewtracker

# Install application requirements
ADD ./config/requirements.txt /srv/viewtracker/
RUN pip3 install -r /srv/viewtracker/requirements.txt

# Add start script
ADD ./config/start.sh /

# Add uWSGI config
ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Add database check script
ADD ./config/database-check.py /srv/config/database-check.py

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/viewtracker

# Execute start script
CMD ["./start.sh"]
