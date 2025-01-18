# Hurricane Damage Reporter

## Team Details
- **Team Member**: Baron Liu  
- **Team Number**: Unknown for now  

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
- **Dependencies**: Install libraries listed in the Dependencies section

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/hurricane-damage-reporter.git
Navigate to the project directory:
cd into it
### Install required libraries:
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
python -m venv myenv
./myenv/Scripts/activate

### Run the application:
streamlit run app.py

### and then ur chilling
