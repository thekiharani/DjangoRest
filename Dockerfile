FROM python:3.7.5-slim-buster

# export database host
ENV DATABASE_HOST=postgres
ENV DATABASE_PASSWORD=8NrQ5xJ9nu6eafbCKiqXtfPDQuWBrEpdV97aXvEg

WORKDIR app
COPY . .

# don't run in debug mode
ENV DEBUG=0

# # AfricasTalking configs
# ENV AT_USER_NAME=mjengosmart
# ENV AT_API_KEY=37050589873d72fdbccc4d2bdf07d50b54ef60ea683489b9a41035ec7054873b
# ENV AT_PREMIUM_SHORTCODE=22384
# ENV AT_PREMIUM_KEYWORD=mjengo
# ENV AT_SENDER_ID=MjengoSmart

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "--access-logfile", "-", "-w", "10", "-b", "-t", "180" "0.0.0.0:8000", "MaishaBeta.wsgi"]
