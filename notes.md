# fiap_tech_challenge_03

WSL

https://docs.localstack.cloud/user-guide/integrations/devcontainers/#vscode

https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04
sudo apt-get install firefox
sudo apt install libffi-dev
sudo ldconfig

https://gist.github.com/trongnghia203/9cc8157acb1a9faad2de95c3175aa875

git clone https://github.com/yyuu/pyenv-virtualenv.git $HOME/.pyenv/plugins/pyenv-virtualenv

pyenv install -l

pyenv install 3.13.0

pyenv virtualenv 3.13.0 venv_3.13.0
--
source venv_3.13.0/bin/activate
pyenv virtualenvs           
pip3.13 install poetry 

pyenv global 3.13.0

pip install --upgrade pip

pip3 install selenium
pip3 install bs4
pip3 install requests
pip3 install pandas
pip3 install lxml
pip3 install boto3
pip3 install awscli
pip3 install fastparquet

https://stackoverflow.com/questions/64086810/navigate-pagination-with-selenium-webdriver
https://stackoverflow.com/questions/63881801/element-is-not-clickable-at-point-because-another-element-obscures-it
https://stackoverflow.com/questions/75688714/python-selenium-how-to-click-element-in-pagination-that-is-not-a-button-a-hr
https://stackoverflow.com/questions/30002313/finding-elements-by-class-name-with-selenium-in-python

aws s3api create-bucket --bucket dados-brutos --endpoint=http://localhost:4566
aws s3 ls --endpoint=http://localhost:4566

aws configure
local | local
us-east-1
json

docker logs -f localstack-main

pip freeze > requirements.txt

poetry install
poetry lock
poetry run python3.13 src/main.py
aws lambda create-function --function-name lambda-scrapper1 --runtime python3.9 --role arn:aws:iam::000000000000:role/lambda-exec --zip-file fileb://app_package.zip --endpoint=http://localhost:4566
aws lambda list-functions --endpoint=http://localhost:4566 | grep lambda-scrapper
aws lambda get-function --function-name lambda-scrapper --endpoint=http://localhost:4566
aws iam put-role-policy --role-name lambda-exec --policy-name AssumeRolePolicyDocument --policy-document '{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "*", "Resource": "*" }] }' --endpoint=http://localhost:4566
aws iam list-role-policies --role-name lambda-exec

SELECT schema_name FROM information_schema.schemata
SELECT table_schema, table_name FROM information_schema.tables
