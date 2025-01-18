# Hurricane Damage Reporter

## Team Details
- **Team Member**: Baron Liu  
- **Team Number**: Unknown for now  
- **Why I used what I used**: I'll be honest Streamlit is the GOAT of making projects as fast as possible, also python is easy to write in and postgresql because I was just familiar with it.
---

## Project Overview
The Hurricane Damage Reporter is a web-based application designed to allow users to report and visualize hurricane damage in their area. Users can submit details such as:

- **Name of the affected location**
- **Address of the location**
- **Severity of the damage** (scale 1-10)
- **Category of the damage** (e.g., Flood, Fire, Wind Damage, Other)

All submissions are stored in a PostgreSQL database and displayed on an interactive map using Folium, integrated with Streamlit.
---

## Installation and Execution Instructions

### Prerequisites
- **Python Version**: Python 3.8 or higher
- **PostgreSQL**: Installed and running
- **Dependencies**:
  ```bash
     import streamlit as st
   from streamlit_folium import st_folium
   import folium
   from geopy.geocoders import Nominatim
   import psycopg2
   from psycopg2.extras import RealDictCursor
   import pygame

### Setup Instructions
**Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/hurricane-damage-reporter.git
Navigate to the project directory:
cd into it

### Install required libraries:
 ```bash
   pip install -r requirements.txt

### Create a database named utek:
### PostgreSQL Table Schema

The following SQL script creates the `reported_locations` table used in this project:

```sql
CREATE TABLE reported_locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    severity INT,
    category VARCHAR(50)
);

### Create virtual enviroment:
```bash
   python -m venv myenv
```bash
   ./myenv/Scripts/activate

### Run the application:
```bash
   streamlit run app.py

### and then ur chilling
