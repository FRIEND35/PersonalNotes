ПОИСКОВИКИ:

candle
grams
torch
tor onionland

БЛОГИ И ПЕРСОНАЛЬНЫЕ САЙТЫ: drksh - Хакерский персональный блог

XMPP SETTINGS:
adress:127.0.0.1
port:9050
proxy:socks5

АНОНИМНОЕ СКАНИРОВАНИЕ:

1. sudo apt-get install torsocks tor

2. В самый конец файла /etc/tor/torrc добавьте строки:

AutomapHostsOnResolve  1
DNSPort                53530
TransPort              9040

3. Запустите и добавьте в автозапуск службу Tor:

sudo systemctl start tor 
sudo systemctl enable tor

СКАННИРОВАНИЕ С П.М NMAP:

proxychains4 nmap -sT -PN -sV --open -n [TARGET]


СКАННИРОВАНИЕ С П.М SQLMAP:

sqlmap -u [TARGET] --proxy socks5://127.0.0.1:9050


ПОДКЛЮЧЕНИЕ IRC C TOR:

$ http_proxy=http://127.0.0.1:6667/ torify irssi
