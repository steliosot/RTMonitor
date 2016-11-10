chmod 600 key.pem
scp -i key.pem c170.csv ubuntu@147.27.50.177:/var/www
ssh -i key.pem ubuntu@147.27.50.177 chmod 777 /var/www/c170.csv
