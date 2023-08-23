# Grupo Dinamita Code
## Reto 3: Crecimiento económico.

## Introduction:
The project involves working with data related to commercial activities in Barcelona using Python. Our team participated in a hackathon and developed a Python script to process and analyze the data. The goal was to extract meaningful insights from the data and organize it for further analysis.

## Data:
**Data Source**:
The data is stored in a CSV file named "2019_censcomercialbcn_detall.csv." This file contains detailed information about various commercial attributes, such as activity codes, sector names, business names, addresses, and more.

**Data Processing**:
The team wrote code to process the CSV file and extract relevant information. The code reads the CSV file line by line, splits each line into individual data elements, and converts certain string values to numbers if possible. The function convert_str_num is used for this conversion.

**Data Storage**:
The processed data is stored in a Pandas DataFrame, a popular data manipulation library in Python. The DataFrame allows for easy manipulation, filtering, and analysis of the data.

**Database Integration**:
Our code uses a module called "Database" to connect and manage the data. The main_db object from this module is used to connect to a database cluster. The data from the CSV file is read and processed within the context of this database connection.

**Data Analysis and Transformation**:
We performed various data analysis and transformation tasks on the DataFrame. For example, we filtered the DataFrame to select specific columns of interest, such as activity codes, sector names, business names, addresses, and more. We also modified some values, like replacing certain business names with standardized values ("Altres" and "Grup no definit" become "0").

**Data Export**:
The processed data is then stored in a JSON format using the json.dump function. This JSON file, named "datos.json," contains a mapping of activity codes to corresponding sector names.

**Additional Features**:
You also created a test script to print and analyze specific columns and their unique values from the DataFrame. This helps to gain insights into the distribution and uniqueness of values in the data.

### Team members:
* Angel Forlano (angel12345leo@gmail.com) (https://www.linkedin.com/in/angel-forlano/)
* Shima Naderi (shima.naderii@gmail.com) (https://www.linkedin.com/in/shima-naderi/)
* Alejandra Morales Cuitiño (https://www.linkedin.com/in/alemcuitino/)
* Alejandro Fernández Vidal (https://www.linkedin.com/in/alejandrofernandezvidal/)
* Gabriela Barajas Moreno (https://www.linkedin.com/in/gabrielabarajas/)
* Mari Carmen Chueco Oviedo (https://www.linkedin.com/in/maricarmenchueco/)
