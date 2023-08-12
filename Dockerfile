FROM python:3.10-slim

RUN mkdir /my_spending_bot

COPY requirements.txt /my_spending_bot/

RUN python -m pip install -r /my_spending_bot/requirements.txt

COPY . /my_spending_bot/

WORKDIR /my_spending_bot

# RUN python bot_authorization.py

ENTRYPOINT ["python", "main.py"]
