# Create and deploy API in Docker and kubernetes
 Overview This task involves on create and deploying Fast API using Flask on docker image then deploy it to kubernetes pod and get the API endpoint from the kubernetes service.

1. Install kubernetes environment in local (minikube - https://minikube.sigs.k8s.io/docs/start/).
2. Install Docker Desktop and create Mysql image in Docker.
3. Load data to MySQL table named spotify_top_songs in database named df_data (refer to Jupiter notebook in /script/load to mysql.ipynb).
4. Prepare an API using Flask in a python file (/script/song_api.py).
5. Verify the API run with curl or web browser.
6. Create a Dockerfile to build a docker image.
8. Deploy the image with deployment.yaml and service.yaml to minikube
