FROM python:3.11-slim

WORKDIR /app

# (선택) 빌드에 필요한 최소 유틸
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

# uv 설치
RUN pip install --no-cache-dir uv

# 소스 복사
COPY . /app

# 의존성 설치
# uv.lock이 있으면 가장 안정적입니다.
RUN uv sync --frozen || uv sync

# FastAPI 포트
EXPOSE 8000

# 서버 실행
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]