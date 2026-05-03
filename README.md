# Backend 프로젝트 실행 방법

## 개요

이 프로젝트는 FastAPI 기반 백엔드 서버입니다.
패키지 관리는 Poetry를 사용하며, 외부 기기에서 접속하기 위해 Cloudflare Tunnel을 사용할 수 있습니다.

## 1. 백엔드 서버 실행

프로젝트 루트 디렉토리에서 FastAPI 서버를 실행합니다.

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

`poetry run`을 사용하면 Poetry가 관리하는 가상환경 안에서 명령어가 실행됩니다.  
따라서 별도로 가상환경을 직접 활성화하지 않아도 됩니다.

서버가 정상적으로 실행되면 로컬에서 아래 주소로 접속할 수 있습니다.

```text
http://localhost:8000
```

---

## 2. HTTPS 터널 열기

아이폰 Safari 등 외부 기기에서 접속하려면 HTTPS 주소가 필요합니다.  
백엔드 서버를 실행한 상태에서 **새 터미널**을 열고 아래 명령어를 실행합니다.

```bash
cloudflared tunnel --url http://localhost:8000
```

실행하면 아래와 같은 임시 HTTPS 주소가 출력됩니다.

```text
https://something-random.trycloudflare.com
```

> 이 주소는 `cloudflared tunnel`을 실행할 때마다 달라질 수 있습니다.

---

## 3. 접속 주소

Cloudflare Tunnel 주소가 아래와 같이 나왔다고 가정합니다.

```text
https://something-random.trycloudflare.com
```

아이폰 Safari에서는 아래 주소로 접속합니다.

```text
https://something-random.trycloudflare.com/mobile
```

PC에서는 아래 주소로 접속합니다.

```text
https://something-random.trycloudflare.com/pc
```

---

## 4. 실행 요약

터미널 1에서 백엔드 서버 실행:

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

터미널 2에서 HTTPS 터널 실행:

```bash
cloudflared tunnel --url http://localhost:8000
```

출력된 `trycloudflare.com` 주소에 `/mobile` 또는 `/pc`를 붙여 접속합니다.

예시:

```text
https://something-random.trycloudflare.com/mobile
https://something-random.trycloudflare.com/pc
```
---

## 5. 자주 발생하는 문제

### 포트 8000이 이미 사용 중인 경우

다른 프로그램이 `8000` 포트를 사용 중일 수 있습니다.  
이 경우 기존 서버를 종료하거나 다른 포트로 실행합니다.

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

다른 포트를 사용했다면 Cloudflare Tunnel 명령어도 같은 포트로 맞춰야 합니다.

```bash
cloudflared tunnel --url http://localhost:8001
```

---

## 6. 종료 방법

서버 또는 터널을 종료하려면 실행 중인 터미널에서 아래 키를 누릅니다.

```text
Ctrl + C
```
