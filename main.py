import mlflow

with mlflow.start_run():
    mlflow.log_param("param1", 5) 
    mlflow.log_param("param2", 10) 
    mlflow.log_metric("metric1", 10) 
    mlflow.log_metric("metric2", 20) 
    mlflow.log_metric("metric3", 30)
    mlflow.log_artifact("example.txt") 