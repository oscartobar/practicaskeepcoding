#!/bin/bash

#Creamos la carpeta "recopilacion" en el HOME de nuestro usuario para almacenar algunos ficheros que neesitaremos durante el curso
mkdir $HOME/recopilacion
mkdir $HOME/recopilacion/lists

#Instalación de diferentes utilidades que usaremos durante el módulo de recopilación de información

#go
sudo apt-get update
sudo apt-get install golang-go chromium

#mapcidr
go install github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest
sudo ln -s $HOME/go/bin/mapcidr /usr/bin/mapcidr

#dnsx
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
sudo ln -s $HOME/go/bin/dnsx /usr/bin/dnsx

#MurMurHash
git clone https://github.com/Viralmaniar/MurMurHash.git /tmp/murmurhash
pip install -r /tmp/murmurhash/requirements.txt --break-system-packages
sudo mv /tmp/murmurhash/MurMurHash.py /usr/bin/murmurhash
sudo sed -i '1s/^/#!\/usr\/bin\/env python\n/' /usr/bin/murmurhash 
sudo chmod +x /usr/bin/murmurhash
rm -rf /tmp/murmurhash

#massdns
git clone https://github.com/blechschmidt/massdns.git /tmp/massdns
cd /tmp/massdns && make
sudo mv /tmp/massdns/bin/massdns /usr/bin/massdns
rm -fr /tmp/massdns
cd $HOME

#shuffledns
go install github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest
sudo ln -s $HOME/go/bin/shuffledns /usr/bin/shuffledns
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt -O $HOME/recopilacion/lists/domains.txt

#dnsvalidator
git clone https://github.com/vortexau/dnsvalidator.git /tmp/dnsvalidator 
cd /tmp/dnsvalidator
sudo python3 /tmp/dnsvalidator/setup.py install
pip install -r /tmp/dnsvalidator/requirements.txt --break-system-packages
cd $HOME
sudo rm -fr /tmp/dnsvalidator

#AnalyticsRelationships
git clone https://github.com/Josue87/AnalyticsRelationships.git /tmp/analytics
pip install -r /tmp/analytics/Python/requirements.txt --break-system-packages
sudo mv /tmp/analytics/Python/analyticsrelationships.py /usr/bin/analyticsrelationships
sudo chmod +x /usr/bin/analyticsrelationships
sudo sed -i '1s/^/#!\/usr\/bin\/env python\n/' /usr/bin/analyticsrelationships
rm -fr /tmp/analytics

#cero
go install github.com/glebarez/cero@latest
sudo ln -s $HOME/go/bin/cero /usr/bin/cero

#katana
go install github.com/projectdiscovery/katana/cmd/katana@latest
sudo ln -s $HOME/go/bin/katana /usr/bin/katana

#unfurl
go install github.com/tomnomnom/unfurl@latest
sudo ln -s $HOME/go/bin/unfurl /usr/bin/unfurl

#ctfr
git clone https://github.com/UnaPibaGeek/ctfr.git /tmp/ctfr
pip install -r /tmp/ctfr/requirements.txt --break-system-packages
sudo mv /tmp/ctfr/ctfr.py /usr/bin/ctfr
sudo chmod +x /usr/bin/ctfr
rm -fr /tmp/ctfr

#gau
go install github.com/lc/gau/v2/cmd/gau@latest
sudo ln -s $HOME/go/bin/gau /usr/bin/gau


#amass
go install -v github.com/owasp-amass/amass/v4/...@master
sudo rm -f /usr/bin/amass
sudo ln -s $HOME/go/bin/amass /usr/bin/amass

#httpx
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
sudo rm -fr /usr/bin/httpx
sudo ln -s $HOME/go/bin/httpx /usr/bin/httpx

#gowitness
go install github.com/sensepost/gowitness@latest
sudo ln -s $HOME/go/bin/gowitness /usr/bin/gowitness

