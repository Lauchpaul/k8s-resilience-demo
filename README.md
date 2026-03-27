# K8s Self-Healing Demo (The Bare Minimum)

## Worum geht es?
Ehrlich gesagt: Die Architektur dieser Applikation ist s*ht. Es ist kein Production-Grade Setup, ignoriert Best Practices der Plattformentwicklung und laeuft auf einem rudimentaeren Docker Desktop Cluster. 

Der einzige Sinn und Zweck dieses Projekts ist der isolierte Beweis eines Kernkonzepts von Kubernetes: **Self-Healing und die automatische Wiederherstellung des Soll-Zustands (Reconciliation Loop).**

## Die Komponenten
Das Setup besteht aus vier Microservices:
* **3x Victim Pods (Ports 4000, 4001, 4002):** Dumme Flask-Container. Sie zeigen lediglich ihren aktuellen K8s-Pod-Namen an und warten auf ihre Terminierung.
* **1x Control Panel (Port 6969):** Ein simples UI, um gezielt Kill-Signale (SIGTERM) an die einzelnen Pods zu senden.

## Ausführung
Das Start-Skript deployt die Manifeste, ConfigMaps und erzwingt persistente Port-Forwards auf localhost, um das Abbrechen der Tunnel beim Pod-Tod zu umgehen.

```bash
chmod +x start.sh
./start.sh
