1. Install Docker
2. Set Docker to use over 4GB of RAM, (Elasticsearch requires at least 2)
    * Docker icon in Tray > Preferences
    * Resources > Advanced

3. Launch the services
    ```sh
    # Launch docker-compose
    docker-compose up elk

    # Build a new image on changes
    docker-compose build elk

    # Force the container to be recreated from image
    docker-compose up elk --force-recreate

    # Enter the container for troubleshooting
    docker exec -it $(docker ps | grep elk | cut -d ' ' -f 1) /bin/bash

    ## Nuke everything from high orbit
    yes | docker container rm $(docker ps -a | grep elk | cut -d ' ' -f 1)
    yes | docker image prune
    yes | docker image rm $(docker image ls -a | grep elk | cut -d ' ' -f 1)
    ```
