FROM python


WORKDIR /app


COPY requirements.txt .

RUN "pip install -r requirements.txt"

CMD [ "uvicorn", "app:app" ]

EXPOSE 8000