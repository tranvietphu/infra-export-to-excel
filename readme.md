# Descripption:
This project build a tool which can export AWS current running infrastructure to excel file.<br/>


# Build steps:

## pip install pandas

## pip install openpyxl

## pip install flatten_json

## python test.py


## exe化: https://www.pyinstaller.org/
pip install pyinstaller<br/>
pyinstaller test.py<br/>
pyinstaller --onefile test.py<br/>

## vpcs
aws ec2 describe-vpcs --query "Vpcs[]" | test.exe -f "test.xlsx" -s VPC<br/>

## ec2
aws ec2 describe-instances --query "Reservations[].Instances[]" | test.exe -f "test.xlsx" -s EC2<br/>

## NACL
aws ec2 describe-network-acls --query "NetworkAcls[]" | test.exe -f "test.xlsx" -s NACL<br/>

## SG
aws ec2 describe-security-groups --query "SecurityGroups[]" | test.exe -f "test.xlsx" -s SG<br/>

## 自分が作ったimages 
aws ec2 describe-images --query "Images[]" --owners self | test.exe -f "test.xlsx" -s AMI<br/>

## ebs volume
aws ec2 describe-volumes --query "Volumes[]" | test.exe -f "test.xlsx" -s EBS<br/>

## IAM User
aws iam list-users --query "Users[]" | test.exe -f "test.xlsx" -s USER<br/>

## RDS
aws rds describe-db-instances --query "DBInstances[]" | test.exe -f "test.xlsx" -s DB<br/>


# aws cli:
https://docs.aws.amazon.com/cli/latest/reference/rds/<br/>


## Git push:
git remote add origin https://github.com/tranvietphu/infra-export-to-excel.git<br/>
git push -u origin master<br/>