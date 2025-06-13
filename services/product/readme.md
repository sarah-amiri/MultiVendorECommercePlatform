# Microservice: Product
This is *Product* microservice of Multi-Vendor E-Commerce Platform project.


## Installation
### Using Pip
#### Steps
1. **Clone the project**
```shell
git clone https://github.com/sarah-amiri/MultiVendorECommercePlatform.git
cd cd MultiVendorECommercePlatform/services/product
```
2. **Install dependencies**
```shell
pip intall -r requirements
```
3. **Build `.env` file**
```shell
cp .env.example .env
```
Made any changes in `.env` if you need.
4. **Start the application**
```shell
python wsgi.py
```
This will run the application on port 8003 on address 0.0.0.0
### Using Docker
#### Steps
1. **Clone the project**
```shell
git clone https://github.com/sarah-amiri/MultiVendorECommercePlatform.git
cd cd MultiVendorECommercePlatform/services/product
```
2. **Build `.env` file**
```shell
cp .env.example .env
```
Made any changes in `.env` if you need.
3. **Start the application**
```shell
docker compose up --build -d
```
You can access the application on `localhost:8003`.
### Environment Variables Guide
To run the application, you need to set up a `.env` file in the root of the project.
You can do this by copying `.env.example` file (as `.env`) in the root directory of the project or make your own file.
Here is a description of any environment variable that is included in this file:
- `APP_NAME`
  - You can set name of the app in this variable. 
  - It is **optional**.
  - Default value is `Product`.
- `APP_VERSION`
  - You can set current version of your app in this variable.
  - It is **optional**.
  - Default value is `1.0.0`.
- `APP_DESCRIPTION`
  - This variable stores description about your app.
  - It is **optional**.
  - Default value is `Product microservice for Multi-Vendor E-Commerce Platform app`.
- `APP_HOST`
  - You can set the host you want the app runs on it in this variable.
 - It is **optional**. 
 - Default value is `localhost`.
- `APP_PORT`
  - You can set the port you want the app runs on it in this variable.
  - It is **optional**.
  - Default value is `8003`.
- `APP_PORT_EXPOSE`
  - You should set this port if you want to run the application using Docker. It is the port that app exposes on docker.
  - It is **optional**.
  - Default value is `8003`.

## Endpoints