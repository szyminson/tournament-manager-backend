# Tournament manager backend
## Development
### VSCode + Docker
1. Install `ms-vscode-remote.remote-containers` extension
2. Start Docker and open project's dir in VSCode
3. Create `.env` file from `.env.example`
```bash
cp .env.example .env
```
4. `Ctrl+Shift+P` -> Remote-Containers: Reopen in Container
5. You can run a debugger using F5 key or just run the app using VSCode's integrated terminal:
```bash
./manage.py runserver
```
### Tips
You can install python dependencies inside the container using pip in the integrated terminal. If you want dependencies to be persisted in the repository you have to add them to `requirements.txt` or `requirements-dev.txt` file. The first one contains project specific dependecies and the second file should contain dev environment specific ones. After each change of these two files the container should be rebuilt using `docker-compose build` command to apply changes. 