"""################################
GLOSSARY
################################"""
repository == image


"""################################
GENERAL
################################"""
+---------------+----------------------------+---------------------+
| docker engine | docker desktop for Windows |                     |
+---------------+----------------------------+---------------------+
| WIN only      | WIN / LINUX                | possible containers |
+---------------+----------------------------+---------------------+

"""################################
SELECT MANY
################################"""
docker ps [OPTIONS]
# Options:
#   -a, --all             Show all containers (default shows just running)
#       --no-trunc        Pokazuje cale komendy
docker-compose ps                                                                    -> pokazuje TYLKO kontenery z sieci

docker images [OPTIONS]
docker volume ls [OPTIONS]
docker network inspect [OPTIONS] NETWORK                         -> Display detailed information on one or more networks


"""################################
SELECT SINGLE
################################"""
docker logs CONTAINER                   -> pokazuje, co widzialaby konsolka danego kontenera
docker diff CONTAINER                   -> pokazuje zmiany plikow  contenerze w stosunku do jego obrazu
docker inspect DOCKER_OBJECT            -> daje cale info (w tym volume))


"""################################
docker run % friends
################################"""
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
# Options:
# -d, --detach                         nie outputuje i wychodzi z termianala
# -it, --interactive && --tty          wymusza wbicie w terminal
# -e, --env list                       Set environment variables
    # EXAMPLE docker run  -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql
#     --name                           nazywamy jakos nasz kontener
# -p, --publish list                   Publish a container's port(s) to
    # EXAMPLE: docker run -p 80:80 nginx
# -v, --volume list                    zrobi polaczenie filesystemow
    # EXAMPLE 1: docker run -v <path_from_host>:<path_to_container> nginx
    # EXAMPLE 2: docker run  -v <volume_name, eq: db>:<path_to_container> mysql
# -w, --workdir string                 Working directory inside the container

docker start  CONTAINER                 -> uruchamiamy container (exec od uruchamia komende na kontenerze)
docker exec CONTAINER COMMAND [ARG...]  -> j.w.

"""################################
TRICKS
################################"""
"""Runnix Linux on Windows"""
docker run -rm IMAGE -v <path_from_host>:<path_to_container> [COMMAND] [ARG...]
# co robi `--rm` ->                                                                           usunie container na koniec

""" Image as script """
# EXAMPLE: docker run --rm weshigbee/nmap -v 192.168.0.0/24
# ocb?->                          nie ma podanej komendy (chyba mozna po prostu defaultowa wybrac przy tworzeniu obrazu)


"""################################
IMAGES
################################"""
docker cp CONTAINER:SRC_PATH DEST_PATH
docker cp SRC_PATH CONTAINER:DEST_PATH                -> Copy files/folders between a container and the local filesystem
# kopiujemy plik, folder, ?                                               -> zawartość jednego folderu do innego folderu

docker commit CONTAINER [REPOSITORY[:TAG]]                              -> Create a new image from a container's changes

docker build [OPTIONS] PATH                                                          -> Build an image from a Dockerfile
# Options:
# -t, --tag list                                                      Name and optionally a tag in the 'name:tag' format
    # EXAMPLE: docker build -t solitaire:nginx-df

# co to PATH? -> przede wszystkim to NIE JEST sciezka do dockerfile, a ustalenie, co bedzie domyslnym cwd w obrazie\
# trzeba dac przynajmniej kropke


"""################################
DOCKER COMPOSE
################################"""
docker-compose up

"""################################
EXAMPLES
################################"""
"docker-compose.yml" ->                                                             https://github.com/friism/MusicStore
"Dockerfile.yml" ->                        https://github.com/nginxinc/docker-nginx/blob/master/stable/alpine/Dockerfile