#!/bin/sh

#Install Dependencies for Crawler
sudo apt-get install python-bs4
wget https://bootstrap.pypa.io/get-pip.py
chmod +x get-pip.py
python3 get-pip.py --user
pip install wikipedia --user
sudo apt-get install sqlite3

#Clone git repo
#git clone https://github.com/Raag079/Web-Crawler.git

#Download and configure Apache Spark
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz
tar -xvzf spark-2.0.0-bin-hadoop2.7.tgz
echo 'export SPARK_HOME=$PWD/spark-2.0.0-bin-hadoop2.7' >> ~/.bashrc
echo 'export PATH=\$PATH:\$SPARK_HOME/bin' >> ~/.bashrc

#Install Java9
sudo apt-add-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java9-installer

#Clean Up downloaded files
rm get-pip.py
rm spark-2.0.0-bin-hadoop2.7.tgz

#Test Spark
spark-2.0.0-bin-hadoop2.7/bin/spark-submit spark-2.0.0-bin-hadoop2.7/examples/src/main/python/pi.py 10

#Run WebCrawler
cd nammaMysuru/
python nammaMysuru.py
