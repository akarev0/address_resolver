FROM python:3.8.0

WORKDIR /app
COPY requirments.txt requirments.txt

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

RUN mkdir postal
RUN git clone https://github.com/openvenues/libpostal \
                                            && cd libpostal \
                                            && ./bootstrap.sh \
                                            && ./configure --datadir=/app/postal \
                                            && make \
                                            && make install
ENV LD_LIBRARY_PATH=/usr/local/lib
RUN pip3 install -r requirments.txt

COPY . .

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8888"]
