# practicaskeepcoding
Entregas y practicas Keepcoding
$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.17.0-windows-x86_64.zip -OutFile elastic-agent-8.17.0-windows-x86_64.zip 
Expand-Archive .\elastic-agent-8.17.0-windows-x86_64.zip -DestinationPath .
cd elastic-agent-8.17.0-windows-x86_64
.\elastic-agent.exe install --url=https://b3a13f1c93fb4e86a37f25814032bb4d.fleet.us-east-1.aws.elastic.cloud:443 --enrollment-token=U0dPLWJaUUJPN2RIbDhwczQybjE6aDZXYzQtR0tSYXlpdTN6QU01ekN3QQ==
