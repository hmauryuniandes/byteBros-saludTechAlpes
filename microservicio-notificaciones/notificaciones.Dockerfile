
FROM python:3.10

EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir "pip<24.1" setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/src

CMD ["flask", "--app", "src.api.notificaciones", "run", "--host=0.0.0.0"]




