FROM python:3

COPY echo_bot_sample.py config.py requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "echo_bot_sample.py"]