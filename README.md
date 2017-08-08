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
MIIEogIBAAKCAQEAzdqyoIhfB3i+J7kilgI5PQdfN9we5OnFWPzYjlML0BQr3RT7
6yPA4JZlP9LmOwrT0CIPjXmzrNx4Qedu6RIV1hKf+tvxL+TyS3v57INH4T+bn8gv
6Yq3kdKoxKFIFoeCRV/fhRzW8pr97RLS7N80JhGY+AC14YJdnhtHaUetdaEuOGqr
HxEmaHGdUqRAWUYZSbfQg3gnff/89BuJQbZQIEW2UmYm32U7WZufYDdiuVJvLmpe
+o/1S1TGerapQJnvsSMO1FiKHDrY4sipOYfSYZA6wrnx80r1hfiZDiptdG3Vi7lD
J0XwPpoj/b++CgEMVjTrpZP1RUvOUgvW/7AsSQIDAQABAoIBACkaiBxh3ofBZkbM
QsmtO/yhojOnMkwHGa7BHgSdNHih7nhAnmS/SN4Pabwqwmn7qXufsXdQW74ib6jJ
K25CfDW4llUi4a/siSzlXmwJcqrZZpuq/1Ykqq7lX2mTwq8s86gikqEjtw/OPvG9
lnxRvTn0vZSXn7mdrE/LpqCw/UPFRaUJ7Mz3lA0jNVPeDnYpvJJDChy7N7JJb6Qo
E/A30lq3a9rfSQ/a2UaLdQzFQ6R3NcJ0kYK4B/ftCZVlb8rBFEtBVHTO8LImP2cC
RoiUBYr3UkR7PfFwmp8oVr10xXgPT30ftFgOD7TU6652gxEPR1rRNGk/iFI0LoB0
qHhSSlkCgYEA5+pBGJ5U8q60tRYF67zIXs29kq/BqJ6M3D3tVe0Ah0j26Tk9bGOb
Ixmmlo3GyCd6B9KvZBBa7zFFcx1Z8CFUlBEmw3lGdDmOKOzse1MDUKMKYEuLBqwZ
tLM50IG5snpETbMvqSeHE9ZwZwW1RfyEZNa7WtpsCrZb01/9ZHmCt6cCgYEA4zuW
CDcDyEWqjE8tGBRUW667M9q6wH8Zkf0e+o24lyQJsaBQ/XvUju4hfUGDBiG7uFrx
A3VO6WJiPiZo3jWsRv/F1j/j2TgbWAUqIHavbOj1GlygYCIrMAD5HzdZ8OpXFPbM
KjiqZyEjMbF0Rjb+HQepKFumBu4A1GToNA9qeo8CgYBTFNKZNS+NeRT3wpoAZ7MI
c4A0ao5gD9y6kdzSaYNE89iwmHbuu4g6PNg3GzdZQPswjkOS/2D0S5xrrtoncmlQ
Wgye/nVE8dGBy860J3sKij4PXUDC9SiIWaSek7qou7B4fXbXjHeRncLKxXq5RctQ
LLUVySXneIjQ4pRuSDGSBQKBgEzEq7pYw8lcZ/MBKM3yyFE1Jf+tzNwN1JiyuE2T
paJCRZgh/lq1BCnJn7zObjKbIO12o+g0MJW+bExs847m+S3/aVopuZOAVhSVohbX
ogqcZXojgvcXdBnCqmd2bsdqlEL74hv9iuxOkLJQLmUuXQl3thlxZRUAQX2AHcbA
0otXAoGAJci97UJ0PKnNIO5w5KhkxzrCOnC69b2TvendM73gYVgZv9LVqoZp8f1Y
zgX6+M/zaxIRyuA5wH0AtvXzkRqaSntDtKiyg0WwyYRUxVhislCRe6WdDUjFmYJc
la09tztzh5lzX5D4s7mEc0JpwcvAcAW2A4QWaQJSo2wNOin7Dw=
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
