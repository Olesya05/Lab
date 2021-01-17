1. Link to repo: https://hub.docker.com/repository/docker/olesia05/lab_4
2. Link to image django: https://hub.docker.com/layers/133599420/olesia05/lab_4/django/images/sha256-d7cf02670f2e2c937f77d2b7865e3383d5ce09f24465ca3f4dedee2f79922956?context=explore
3. Link to image monitoring: https://hub.docker.com/layers/133599499/olesia05/lab_4/monitoring/images/sha256-4735630e2204daa2319ff8734fe15f3a535bb25d5723ca0527a1c050b2717bfc?context=explore

4. Using commands: 1)docker -v, 2)docker -h, 3)docker run docker/whalesay cowsay Docker is fun
5. Using commands: 1)docker pull python:3.8-slim, 2)docker images, 3)docker inspect python:3.8-slim
6. Using commands: sudo docker build -t olesia05/lab_4:django ., sudo docker build --file Dockerfile.site -t olesia/lab_4:monitoring .
7. Using command docker run -it --name=django --rm -p 8000:8000 olesia05/lab_4:django
8. Using command: sudo docker run -it --net=host --name=monitoring --rm -v $(pwd)/server.log:/app/server.log olesia05/lab_4:monitoring 
