sudo docker image build -t bot:0.1 .
sudo docker container run --env-file .env --rm  --name bb bot:0.1
