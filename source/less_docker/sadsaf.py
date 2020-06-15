docker info -> liczba kontenerów, itd.
docker ps -> lista procesow
docker ps -a -> wszystkie
docker ps -a --no-trunc  -> pokazuje ostatnio uruchomione komendy
docker images -> lista image (!= kontenerow)
docker run <nazwa_apki> -> robi wszystko (#pdk)
docker run <nazwa_apki> <command> -> robi (po wszystkim) "<nazwa_apki> <command>" (jak przy normalnym uzyciu)
        -> (<command> == powershell) => odpali shella w kontenerze (warto zrobic wtedy Get-Process)
docker run -id -> wbije go od razu do downloads

docker run -p 80:80 nginx -> przekierowuje porty z hosta na contener (tu akurat 80 na 80)
# TODO gdzie ten nginx do huja? (w sensie w task managerze, gdziekolwiek)

Get-Process | select Id, ProcessName ->redukcja

# TODO jak ziomek widzial te mongo na poczatku?
# TODO wbij na linuxie explorerem w kontenera

# FUTURE
docker run -it -> umozliwia rpzeskakiwanie miedzy teminalami

microsoft/iis:nanoserver

##############################################
docker engine vs Docker for Windows
tylko windowsy | windowsy lub linuxy            KONTENERY
Computer Management - fajna opcja w windowsie
"""################################
Czy procesy w dockerze są izolowane?
################################"""
TAK, sprawdzałem po ID i zarówno kontener, jak i "main" maja calkiem rozne procesy.