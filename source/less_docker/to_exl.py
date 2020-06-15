docker info -> liczba kontenerów, itd.
docker ps -> lista procesow
docker ps -a -> wszystkie
docker ps -a --no-trunc  -> pokazuje ostatnio uruchomione komendy
docker images -> lista image (!= kontenerow)
docker run <nazwa_apki> -> robi wszystko (#pdk)
docker run <nazwa_apki> <command> -> robi (po wszystkim) "<nazwa_apki> <command>" (jak przy normalnym uzyciu)
        -> (<command> == powershell) => odpali shella w kontenerze (warto zrobic wtedy Get-Process)
docker run -id -> wbije go od razu do downloads
docker exec <container> -> pozwala uruchomic kolejny process w konterze
        jaki bylby ciekawy-> np. bash (czyli wbijamy w kontener)
docker diff <container> -> pokazuje zmiany plikow  contenerze w stosunku do jego obrazu

docker run -p 80:80 nginx -> przekierowuje porty z hosta na contener (tu akurat 80 na 80)

docker images | sls <some_string> -> filter (szuka we wszystkich kolumnach)
docker start -> uruchamiamy container (exec tylko wbija do)
# TODO gdzie ten nginx do huja? (w sensie w task managerze, gdziekolwiek)

docker logs <container> -> pokazuje, co widzialaby konsolka danego kontenera

Get-Process | select Id, ProcessName ->redukcja

# TODO jak ziomek widzial te mongo na poczatku?
# TODO wbij na linuxie explorerem w kontenera

# FUTURE
docker run -it -> wymusza wbicie w terminal
docker run -d -> nie outputuje i wychodzi z termianala

microsoft/iis:nanoserver

docker inspect -> daje cale info (w tym volume))

##############################################
docker engine vs Docker for Windows
tylko windowsy | windowsy lub linuxy            KONTENERY
Computer Management - fajna opcja w windowsie
"""################################
Czy procesy w dockerze są izolowane?
################################"""
TAK, sprawdzałem po ID i zarówno kontener, jak i "main" maja calkiem rozne procesy.

"""################################
Running CLI apps
################################"""
# TODO save image vs build image
docker run --rm -v c:/Users:/data alpine ls /data
    --rm                                    -> usunie container na koniec
    -c <path_from_host>:<path_to_container> -> zrobi polaczenie filesystemow
    ls /data                                -> tutaj jako command do odpalnie

docker run --rm -v c:/Users/devoted_w:/data alpine tar -xf data/iss.tar -C data/iss
"""
jaki bedzie efekt powyzszej komendy?->               wykona operacje linuxowym programem (tutaj: `tar`) na windowsie !!!
JEDNA LINIJKA -> DA SIĘ PROSCIEJ? ->                                           tak, wbijasz bashem do kontenera i robisz
"""

"""################################
Image as script
################################"""
docker run --rm weshigbee/nmap -v 192.168.0.0/24
"""
ocb?->                            nie ma podanej komendy (chyba mozna po prostu defaultowa wybrac przy tworzeniu obrazu)
"""

"""################################
Kopiowanie
################################"""
docker cp <...>
# kopiujemy plik, doler, ?                                                -> zawartość jednego folderu do innego folderu
"""
how to pass source_name?
    assume the source is in "path/to/source", then
"""
cd path\to
docker cp .\source\. <...>

"""################################
container -> image
################################"""
docerk commit <container> <image>[:<tag>]

"""using Dockerfile (automated)"""
https://github.com/nginxinc/docker-nginx/blob/master/stable/alpine/Dockerfile

docker build -t solitaire:nginx-df .
    .           -> sciezka, ktora ma byc cwd (nazywamy tutaj kontekst)

# TODO automated build on docker hub

"""################################
Databases
################################"""
docker volume ls -> pokazuje volumy
# a co to volume? -> dumpy z baz danych

docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d -v db:/var/lib/mysql mysql
    -v db:/var/lib/mysql -> `db` jako nie-sciezka(!) stworzy volume (zamiast robi czwykle polaczenie, jak to robilo -v do tej pory)
    # co jest tutaj dojebanego? -> jesli volum ejuz istnialo, to po prostu podepnie stale.

"""################################
Powershell
################################"""
<command> $(<other command>) -> write output of one command to another


"""################################
Tricks
################################"""
docker rm $(docker ps -q)

"""################################
Docker compose
################################"""
docker netvork ls -> pokazuje sieci pomiedzy contenerami
docker network inspect <siec> -> wizualziuje siec
# TODO ogarnac `bridge` network (ten co lazy wszystkie contenery)
# TODO jak przeskakiwac miedzy bashami z jednego okienka
docker-compose ps -> pokazuje tylko kontenery z sieci
"zaawnsowany przyklad" -> https://github.com/friism/MusicStore
    # czasami nie mozna od razu `up`, jak jest obraz do zbudowania wczesniej