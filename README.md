
## Test the full Docker build locally
<pre>
# Build and start all containers
docker compose up --build  # if image exists, then without --build

<!-- docker compose -f docker-compose.dev.yml up --build -->

# To stop the container
docker compose down
</pre>

Then visit `http://localhost:8000`, the app should be fully functioning inside of the Docker.

