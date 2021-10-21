
1. Install Docker
2. Update max_map_count in the docker host
    ```sh
    wsl -d docker-desktop
    echo 262144 >> /proc/sys/vm/max_map_count
    ```

3. Launch the services
    ```sh
    # Launch docker-compose
    docker-compose up elk

    # Build a new image on changes
    docker-compose build elk

    # Force the container to be recreated from image
    docker-compose up elk --force-recreate


    ```
