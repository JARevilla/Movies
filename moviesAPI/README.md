# RestFulAPI for Searching and Capture movies in "https://real-fmovies.show/" 

Description: This project has a webcrawler to generate movies in "https://real-fmovies.show/" and expose an API endpoint to view generated movies.

- `moviesUI` - To access available web services.
- `Database` - Builtin djangjo database using sqlite3.
- `BeautifulSoup` - Used for webcrawling.
- `Containerization` - Docker setup for easy deployment.

## Instructions

1. Cloning the repository:
    ```sh
    git clone (https://github.com/JARevilla/Movies/tree/main/moviesAPI)
    cd moviesAPI
    ```
2. Create and activate a virtual environment:
    ```sh
    pip install virtualenvironment
    virtualenv {virtual-env-name}
    {virtual-env-name}/Scripts/Activate
    ```
3. Install dependencies listed in requirements.txt:
    ```sh
    pip install -r requirements.txt
    ```
4. Manually run the web crawler
    ```sh
    python manage.py webcrawler.py
    ```
6. Run the application:
    ```sh
    python manage.py runserver
    ```
   
## API Endpoints

- `GET /moviesUI/getMovie/?title=` - provide title of the movie; (Optional parameter: sitename) (Used in react.js project for User Interface)
- `POST /moviesUI/saveMovie/` - Save if only one movie
- `POST /moviesUI/bulkMovie/` - Save if multiple movie (Used by webcrawler)

## Containerization

1. Build and run the Docker container:
    ```sh
    docker-compose up --build
    ```
