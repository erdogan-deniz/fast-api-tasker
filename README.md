# Pet project - "Tasker" 

> ### ABOUT 🔮

`Description`: this project was created for simple work with the database. Using a `POST` request, you can send the 
`Task` entity to the database. Using a `GET` request, you can get a list of `Task` in the form of a `JSON` file. 
For convenience, use the `Swagger UI` from `FastPI` using the `URL`: `/docs`. The entire project is built and run from 
`Dockerfile`.

> ### STACK 🛠

- `Deploy`: docker 
- `Database`: sqlite 
- `Local host`: uvicorn 
- `Patterns`: repository 
- `Web framework`: FastAPI ✈
- `Programming language`: Python >= 3.9 
- `Modules`: sqlalchemy, typing, pydantic 

> ### FILES 📂

- `.dockerignore`: using this file, you can set rules for excluding files from the build context, which means reducing 
the time required to assemble the tar archive and send it to the server.
- `.gitignore`: a file specifies intentionally untracked files that Git should ignore.
- `Dockerfile`: a dockerfile is a text document that contains all the commands a user could call on the command line to 
assemble an image.
- `README.md`: is used to generate the html summary you see at the bottom of projects. 
- `data.py`: contains all other information for the project.
- `database.py`: contains classes and methods for working with the database.
- `main.py`: the main file of the application launch.
- `repository.py`: repository pattern file for working with the database.
- `requirements.txt`: serves as a list of items to be installed by pip, when using pip install.
- `router.py`: contains the main routers to work with application.
- `schema.py`: contains a description of data structures.

> ### WARNINGS ⚠️

- If your language version is less than 3.9, use `<type1> | <type2>` instead of `Union[<type1>, <type2>]`.

> ### CREATE REPOSITORY ✏️

```
git init
git remote add origin git@github.com:<nickname>/<repository_name>.git
.... add gitignore
git add .
git commit -m "..."
git branch -M main
git push -u origin main
```

> ### PREPARE SERVER 🔧

- `git`:
    ```
    sudo apt-get update
    sudo apt-get install git
    ```

- `docker`:
    ```
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

> ### LAUNCH APPLICATION 🏉

```
docker build . --tag fastapi_app
docker run -p 80:80 fastapi_app
```
