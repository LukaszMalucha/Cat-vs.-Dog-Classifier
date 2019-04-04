FROM python:3.5
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.12.0-cp35-cp35m-linux_x86_64.whl
COPY . .
CMD ["python", "app.py"]