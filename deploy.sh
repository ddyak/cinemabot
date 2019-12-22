sudo docker image build -t bot:0.1 .
sudo docker container run -e BOT_TOKEN=${BOT_TOKEN} --rm  --name bb bot:0.1
