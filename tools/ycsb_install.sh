#Installing dependencies
apt-get install default-jdk, maven, git -y

#Cloning the git repo
git clone git://github.com/brianfrankcooper/YCSB.git
cd YCSB

#Building the package using maven
mvn clean package
