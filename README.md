# Instruction for setting up and running Library management app on frappe framework

This script used to steps to follow from create frappe app to running the app

## Installation

If you haven't installed Bench. goto this link and follow installation guide https://docs.frappe.io/framework/v14/user/en/installation

## Check bench install on your computer 

```bash
bench --version
5.23.0
```

## Create the frappe-bench directory

```bash
bench init frappe-bench
```

## Move your directory from root to frappe-bench

```bash
cd frappe-bench
```

## Create Library Management App(from frappe-bench directory)

```bash
bench new-app library_management
```

## Insert information on the prompt 

```bash
App Title (default: Library Management):
App Description: Library Management System
App Publisher: Abel Gezahegn
App Email: Abel@gmail.com
App Icon (default 'octicon octicon-file-directory'):
App Color (default 'grey'):
App License (default 'MIT'):
'library_management' created at /home/frappe/frappe-bench/apps/library_management

Installing library_management
bench build --app library_management
```

## Create a new site(from frappe-bench directory)
```bash
bench new-site library.localhost
MySQL root password:
Set Administrator password:
```
fill MySql root password or mariadb password depend form 
"Remember" for the first time password is empty so press simply enter and set your password

## Access site in your browser 
port number and site address different depend on your choice

```bash
library.localhost:8000
```

## Install app on site(from frappe-bench directory)

```bash
bench --site library.localhost install-app library_management
```

# Initialize app for running frappe(from frappe-bench directory)

## Starting Bench(from frappe-bench directory)
while running bench application don't close or terminate terminal 

```bash
bench start 
```

# Starting database(from frappe-bench directory)
This database command based on ubuntu on window(WSL) 

```bash
sudo service mariadb start
```

## Login to Desk 
Goto website and paste "library.localhost:8000" and fill the username and password on frappe login page then starting your magic 🫡
