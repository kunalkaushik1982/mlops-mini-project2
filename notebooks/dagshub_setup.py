import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/kunalkaushik1982/mlops-mini-project2.mlflow')
dagshub.init(repo_owner='kunalkaushik1982', repo_name='mlops-mini-project2', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)