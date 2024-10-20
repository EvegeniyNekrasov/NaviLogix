# NaviLogix
Naval logistics app

Clone repo:
``` bash
git clone https://github.com/EvegeniyNekrasov/NaviLogix.git
```

To start a client app:
``` bash
cd client
pnpm install
pnpm dev
```

To start a server app:
``` bash
cd server
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
uvicorn storeapi.main:app --reload
```
