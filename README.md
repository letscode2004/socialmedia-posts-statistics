# Ethereum Transaction Tracker

## Overview
This project tracks Ethereum transactions and logs them into MongoDB. 

## Prerequisites
- Python >= 3.8
- Docker & Docker Compose
- MongoDB
- An Infura.io account or another Ethereum node access point

## Setup

### Local Setup
1. Clone the repository:
    ```sh
    git clone [Your Repo Link]
    ```
2. Navigate into the project directory:
    ```sh
    cd [Your Project Directory]
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Setup environment variables: 
   - Copy `.env.example` to `.env` and fill the variables accordingly.
5. Run the application:
    ```sh
    python app.py
    ```

### Docker Setup
1. Navigate into the project directory:
    ```sh
    cd [Your Project Directory]
    ```
2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

## Usage

This application tracks Ethereum transactions and logs them into a MongoDB database.

### Local Usage
- Ensure MongoDB is running and accessible.
- Set the Ethereum node URL in the `.env` file.
- Run the application:
  ```sh
  python app.py

