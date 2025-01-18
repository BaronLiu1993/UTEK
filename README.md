Hurricane Damage Reporter 
Team Member: Baron Liu
Team Number: Unknown for now IG

Project Overview

The Hurricane Damage Reporter is a web-based application designed to allow users to report and visualize hurricane damage in their area. Users can submit details such as:

Name of the affected location

Address of the location

Severity of the damage (scale 1-10)

Category of the damage (e.g., Flood, Fire, Wind Damage, Other)

All submissions are stored in a PostgreSQL database and displayed on an interactive map using Folium, integrated with Streamlit.


Installation and Execution Instructions

Prerequisites

Python Version: Python 3.8 or higher

PostgreSQL: Installed and running

Dependencies: Install libraries listed in the Dependencies section

Setup Instructions

Clone the repository:

git clone https://github.com/your-repo/hurricane-damage-reporter.git

Navigate to the project directory:

cd hurricane-damage-reporter

Install required libraries:

pip install -r requirements.txt

Set up the PostgreSQL database:

Create a database named utek.

Create the required table:

CREATE TABLE reported_locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100), or TEXT
    address VARCHAR(255), or TEXT
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    severity INT,
    category VARCHAR(50), or TEXT
);

Run the application:

streamlit run app.py

Dependencies and Libraries Used

The project uses the following libraries:

Streamlit: For building the web application interface.

Folium: For creating interactive maps.

Streamlit-Folium: For embedding Folium maps into the Streamlit app.

Geopy: For geocoding addresses into latitude and longitude.

Psycopg2: For interacting with the PostgreSQL database.

Pygame: For playing sounds after successful submissions.

Install all dependencies using:

pip install -r requirements.txt

Brief Explanation of Files

app.py: The main application file. Contains the Streamlit code for reporting and visualizing hurricane damage.

requirements.txt: A file listing all required Python libraries and their versions.

Project_Documentation.pdf: A PDF containing team details, project overview, and other relevant information.

lmao.mp3: Audio file played upon successful submission of a report.

Project Documentation

Project Overview

This project enables users to report hurricane-related damage and visualize the information on a map. It provides essential tools for disaster management and assessment.
