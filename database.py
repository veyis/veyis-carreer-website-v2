from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)

db_connection_string = "mysql+pymysql://3qwyizpth074usuub0eo:pscale_pw_U04E3xRyRIS3w0uuD0pGbslp1SKNkl9Xt1DpQ8mVCUq@us-east.connect.psdb.cloud/carreer-web?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    #print(result.all())
    jobs = []
    for row in result.all():
      jobs.append(row)
    return jobs
