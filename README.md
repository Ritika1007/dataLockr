<div align="center">
<img src="https://github.com/Ritika1007/dataLockr/assets/72782573/7483bceb-635c-47fd-92b7-18e7766c2132" alt="Security Icon">

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
[![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/-Django%20Rest%20Framework-092E20?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)
[![JWT Tokens](https://img.shields.io/badge/-JWT%20Tokens-000000?style=flat&logo=json-web-tokens)](https://jwt.io/)
[![HTML](https://img.shields.io/badge/-HTML-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/-CSS-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
![Sweetify](https://img.shields.io/badge/-Sweetify-FF6B6B)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=flat&logo=swagger&logoColor=white)

🔒 DataLockr empowers you with a robust and elegant data management system, ensuring the security and accessibility of your valuable files. Our seamlessly integrated technologies and rich features redefine the way you handle and safeguard your data.

</div>


## Features

### 🛡️ Advanced Security

Your data's security is our priority. User authentication using JWT tokens guarantees only authorized access to your files.

### 🎨 Intuitive Frontend

The elegantly designed frontend, built with HTML, CSS, and JavaScript, ensures a smooth and delightful experience while managing your data.

### 📂 Organized Data Storage

Create folders for microservices, easily categorizing and managing files according to your needs.

### 📝 File Management

Effortlessly create, edit, and delete files within their designated folders, keeping your data organized and up-to-date.

### 🚀 Instant Notifications

Our integrated alert system, powered by Sweetify, provides intuitive and visually appealing notifications for actions like file updates.

### 🔍 Search Folders and Files

Easily search for folders or files by typing the name in the search bar. The results will dynamically update to match your query.

### ⚙️ CLI (python script) for CRUD Operations

   Manage your DataLockr data with ease using our Python CLI. Perform Create, Read, Update, and Delete operations from the command line.
   In your project directory just run " python dataLockr_cli.py "

## Installation

Experience the power of DataLockr with a simple installation process.

1. **Clone the Repository**: Begin by cloning the repository: `https://github.com/Ritika1007/dataLockr.git`

2. **Navigate and Activate**: Move to the project directory and activate the virtual environment.

   ```bash
   cd dataLockr
   python3 -m venv venv
   source venv/bin/activate   # macOS and Linux
   venv\Scripts\activate      # Windows
   
3. **Install Dependencies, run migrations and create superuser**.

    ```bash
   pip3 install -r requirements.txt
   python3 manage.py migrate
   python3 manage.py createsuperuser

4. **Start the Server**: Launch the development server.
   ```bash
   python3 manage.py runserver

## Usage

Embrace the potential of DataLockr for secure data management.

- **Create User**: SignIn/SignUp a user within the [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

- **User Access**: Log in to DataLockr using the new user's credentials.

- **Efficient Management**: Create folders, Create files, and effortlessly manage your data securely and systematically.


## API Documentation 📚

Explore the power of DataLockr's APIs and learn how to interact with them effectively.

### API Endpoints 🚀

- **Generate JWT Token**: Obtain a JSON Web Token for authentication using your creds.
  - Endpoint: `POST /api/token/`

- **List and Create Subfolders**: Retrieve a list of subfolders and create new ones.
  - Endpoint: `GET /v1/api/subfolders/`
  - Endpoint: `POST /v1/api/subfolders/`

- **Delete Subfolder**: Remove a specific subfolder.
  - Endpoint: `DELETE /v1/api/subfolders/<int:pk>`

- **List and Create Files**: Access a list of files in a subfolder and upload new files.
  - Endpoint: `GET /v1/api/subfolders/<int:subfolder_id>/files`
  - Endpoint: `POST /v1/api/subfolders/<int:subfolder_id>/files`

- **Retrieve File Details**: Retrieve comprehensive details of a specific file.
  - Endpoint: `GET /api/subfolders/<int:subfolder_id>/file/<int:file_id>`

- **Edit File Content**: Modify the content of a specific file.
  - Endpoint: `PUT /api/subfolders/<int:subfolder_id>/file/<int:file_id>`

- **Delete File**: Delete a specific file.
  - Endpoint: `DELETE /api/subfolders/<int:subfolder_id>/file/<int:file_id>`

For detailed request and response formats, authentication details, and parameters, refer to the API documentation.

### Using cURL to Access APIs 🚀

Explore DataLockr's APIs using cURL commands to interact from the command line, Few examples are listed below.

1. **Generate JWT Token**: Obtain an authentication token.
  
     ```shell
     curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=<your_username>&password=<your_password>" http://127.0.0.1:8000/api/token/

2. **List Subfolders**: Retrieve a list of subfolders.

    ```shell
    curl -H "Authorization: Bearer <your_token>" http://127.0.0.1:8000/v1/api/subfolders/

3. **Create Subfolder**: Create a new subfolder.

    ```shell
    curl -X POST -H "Authorization: Bearer <your_token>" -d "name=<subfolder_name>" http://127.0.0.1:8000/v1/api/subfolders/

>Remember to replace <your_token>, <your_username>, <your_password>, <subfolder_id>, and <file_id> with appropriate values.

Unleash the power of cURL and master your API interactions from the command line! 🚀

### Using Swagger UI to Access APIs 🌐

Unlock the magic of Swagger UI to seamlessly interact with DataLockr's APIs.

1. **Start the Server**: Ensure your DataLockr server is running.

2. **Access Swagger UI**: Open your web browser and navigate to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to enter the world of Swagger UI.

3. **Explore Endpoints**: Swagger UI presents an interactive interface where you can discover all available API endpoints. Expand an endpoint to view request and response details.

4. **Authorize**: When dealing with authenticated endpoints, click "Authorize" at the top-right corner. Provide your JWT token to access authenticated functionality.

5. **Try It Out**: Inside each endpoint's section, hit the "Try it out" button. Customize parameters and witness responses within Swagger UI.

6. **Execute Requests**: After configuring parameters, click "Execute" to dispatch the request to the server. Swagger UI displays response status, headers, and body details.

7. **Learn and Validate**: Swagger UI is a potent tool for comprehending and validating APIs. It aids in understanding API operations and verifying your requests and responses.

Remember to adjust the server address (`http://127.0.0.1:8000/`) to match your DataLockr server.

Unleash the potential of Swagger UI and master your API interactions with ease! 🚀

## ScreenShots
>SignIn Page

![image](https://github.com/Ritika1007/dataLockr/assets/72782573/d93bdf2b-a567-48cc-aecf-1338b7495c42)

>SignUp Page

![image](https://github.com/Ritika1007/dataLockr/assets/72782573/c5a3aea8-78c1-42d6-a6a8-1b1ec3a5a227)

>Home Page(Folder's View)

![image](https://github.com/Ritika1007/dataLockr/assets/72782573/676c9f8d-542a-4b4a-9a5b-a1295a306a00)

>Files in a Folder View

![image](https://github.com/Ritika1007/dataLockr/assets/72782573/121e2cb0-a5ca-44d4-be89-7a221b1dc934)

>File View

![image](https://github.com/Ritika1007/dataLockr/assets/72782573/76da5982-0034-4449-b3ca-ca219a878ab7)

>Create File View

![image](https://github.com/Ritika1007/dataLockr/assets/72782573/170ba41f-e9f6-44a0-aa9c-8b7a69950117)

>Swagger UI View

![image](https://github.com/Ritika1007/dataLockr/assets/72782573/8d7366e8-e0c0-42eb-bfd5-1062608eeb9b)

>CLI
![image](https://github.com/Ritika1007/dataLockr/assets/72782573/26b4f55b-4e8b-4391-a249-ba03a63e1ae9)







