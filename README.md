Install Monitor Engine (Ubuntu 14.04-CENTOS)

1. Install python psutil library
	
	-Ubuntu
	
	sudo apt-get install python-psutil
	
	-CentOS:
	
	curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
	
	python get-pip.py
	
	sudo yum install gcc python-devel
	
	pip install psutil
	
2. Install python numpy library
	-Ubuntu
	
	sudo apt-get install python-numpy

	-CentOS
	
	sudo yum install numpy scipy

3. Create the monitor.py

Make sure you change the filename in the script (e.g. c170.csv).


4. Create the key.pem

-----BEGIN RSA PRIVATE KEY-----

-----END RSA PRIVATE KEY-----

5. Change key.pem permissions
	chmod 600 key.pem
	
6. Create the c170.csv file (empty)

7. Copy the file to the cloud service
	scp -i key.pem c170.csv ubuntu@147.27.50.177:/var/www
	
8. Change permissions to the uploaded file
	ssh -i key.pem ubuntu@147.27.50.177 chmod 777 /var/www/c170.csv
	
9. Check that your data is available
	http://147.27.50.177/c170.csv

10. Enjoy!
