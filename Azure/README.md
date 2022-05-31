# Codigos azure

Los códigos están divididos en las carpetas correspondientes dependiendo el tema que se haya visto, en caso de que se requieran instrucciones extra se pondrán en este documento

## Blob storage
Para blob storage se recomienda un ambiente virtual de python (venv) e instalar el `requeriments.txt`

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Además de exportar la key que nos ofrece blob storage:

Bash:
```bash
export AZURE_STORAGE_CONNECTION_STRING="<clave>"
```
PowerShell:
```powershell
setx AZURE_STORAGE_CONNECTION_STRING "<clave>"
```