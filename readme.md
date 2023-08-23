# Dinamite Code Group
## Reto 3: Crecimiento económico.

## **Project Introduction**: Tech4Good for Sustainability in Barcelona

Our project is a tech-driven initiative with a focus on sustainability, designed to empower local businesses and promote conscious consumerism within the vibrant city of Barcelona. Our primary goal is to encourage the "go local, shop local" ethos by leveraging cutting-edge technology to connect consumers with local businesses. This way, we aim to foster sustainable growth while contributing to the city's economic and environmental well-being.
The project involves working with data related to commercial activities in Barcelona using Python. Our team participated in a hackathon and developed a Python script to process and analyze the data. The goal was to extract meaningful insights from the data and organize it for further analysis.

**Key Objectives**:

**Empowering Local Businesses**: We're dedicated to creating a platform that gives local businesses in Barcelona a digital presence. By providing them with a space to showcase their products and services, we empower them to reach a wider audience and thrive in the digital age.

**Promoting Sustainability**: Sustainability is at the heart of our project. By promoting local businesses, we encourage sustainable practices and reduce the carbon footprint associated with global supply chains. This aligns with our commitment to making positive environmental contributions.

**Enhancing Consumer Engagement**: Through our user-friendly platform, we're enhancing consumer engagement by offering a seamless experience. Shoppers can easily discover and support local businesses, making informed decisions that positively impact their community.

## Technology Stack:

**Front-End: JavaScript and React**
We've developed an engaging and intuitive front-end using JavaScript and the React library. This modern framework allows us to build dynamic and interactive user interfaces, ensuring a smooth browsing experience for our platform users. The use of React also enables us to efficiently manage the application state and seamlessly update content.

**Back-End: Java**
The backbone of our platform is built using Java for the back-end. Java's robustness, scalability, and reliability make it an ideal choice for handling the complex business logic and data processing required to connect consumers with local businesses.

**Data Processing: Python and Related Libraries**
We leverage the power of Python, along with data manipulation libraries like Pandas, to process and analyze data related to local businesses and their products. This enables us to curate meaningful insights that guide our platform's functionality and user experience.

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

**Collaborative Approach**:
Our project is the result of collaborative efforts, bringing together individuals with diverse skill sets. Designers, developers, data scientists, and sustainability advocates work hand in hand to ensure that our platform aligns with its core objectives.

In summary, our tech-driven initiative, centered in Barcelona, leverages the synergies of JavaScript, React, Java, and Python to empower local businesses, promote sustainability, and provide consumers with a platform that encourages conscious consumption. Through this project, we're contributing to the community, the environment, and the advancement of sustainable practices in the modern age.

### Team members:
* Angel Forlano (angel12345leo@gmail.com) (https://www.linkedin.com/in/angel-forlano/)
* Shima Naderi (shima.naderii@gmail.com) (https://www.linkedin.com/in/shima-naderi/)
* Alejandra Morales Cuitiño (https://www.linkedin.com/in/alemcuitino/)
* Alejandro Fernández Vidal (https://www.linkedin.com/in/alejandrofernandezvidal/)
* Gabriela Barajas Moreno (https://www.linkedin.com/in/gabrielabarajas/)
* Mari Carmen Chueco Oviedo (https://www.linkedin.com/in/maricarmenchueco/)
