GET /items

request -> router -> service -> crud/db -> response

Folder Structure

- `app/main.py`: application entry point
- `app/core/`: central configuration, such as connection to the database.
- `app/models/`: database tables
- `app/schemas/`: API input and output models
- `app/crud/`: rules for accessing data
- `app/routers/`: routes/endpoints
- `data/`: Where is the SQLite file located?