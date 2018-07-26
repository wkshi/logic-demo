# Project logic-demo

### Base on django-rest-framework, to implement following logic:
* stringClean
* maxBlock
* reorderBlock

### Structure Overview
```bash
# tree .
.
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── logic
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── logic_demo
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```
### Details
* **docker-compose.yml:** Configure file for docker-compose, which
* **Dockerfile:** Configure file for docker build
* **logic:** main djangog directory for logic app
* **logic_demo:** main django entry for logci_demo project
* **manage.py:** manager tool
* **requirements.txt:** required package

### Deployment
* Install docker(Reference to [official doc](https://docs.docker.com/install/linux/docker-ce/centos/))
```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo  https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
systemctl enable docker
systemctl start docker
```
* Install docker-compose(Reference to [official doc](https://docs.docker.com/compose/install/))
```bash
curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version
```
* Execute installation
```bash
git clone https://github.com/wkshi/logic-demo.git
cd logic-demo
docker-compose up
```

### Usage
You'd use httpie
```bash
pip install httpie
```
```bash
http POST http://[YourHost]:8000/logic/ function="xxx" input_string="xxx"
```
