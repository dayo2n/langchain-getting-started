# langchain-getting-started

LangChain 공식 quickstart와 LangChain Academy 과정을 따라가며 학습한 코드 저장소.
모델은 주로 Google Gemini (`gemini-2.5-flash`)를 사용한다.

## 구조

```
.
├── basic_agent.py            # LangChain quickstart의 기본 에이전트 (날씨 툴)
├── realworld_agent.py        # quickstart real-world 예제 (Gutenberg 문서 분석)
├── main.py                   # uv 기본 진입점
├── langchain_academy/        # LangChain Academy L1–L7 실습
│   ├── langchain_academy_l1_fast_agent.py
│   ├── langchain_academy_l2_messages.py
│   ├── langchain_academy_l3_streaming.py
│   ├── langchain_academy_l4_tools.py
│   ├── langchain_academy_l5_tools_with_mcp.py
│   ├── langchain_academy_l6_memory.py
│   └── langchain_academy_l7_structured_output.py
├── pyproject.toml
└── uv.lock
```

## 학습 진도

| 파일 | 주제 | 핵심 |
|------|------|------|
| `basic_agent.py` | 기본 에이전트 | `create_agent`, 단일 툴, ReAct 루프 |
| `realworld_agent.py` | 실전 에이전트 | `fetch_text_from_url`, `create_deep_agent`, `InMemorySaver` |
| `academy_l1_fast_agent` | SQL 에이전트 | `RuntimeContext`, `SQLDatabase`, Chinook DB 분석 |
| `academy_l2_messages` | 메시지 | `HumanMessage`, `AIMessage`, 메시지 구조 |
| `academy_l3_streaming` | 스트리밍 | `agent.stream()`, 청크 단위 응답 |
| `academy_l4_tools` | 툴 정의 | `@tool` 데코레이터, `parse_docstring`, 다중 툴 |
| `academy_l5_tools_with_mcp` | MCP 통합 | `MultiServerMCPClient`, 외부 MCP 서버 연결 |
| `academy_l6_memory` | 메모리 | `checkpointer`, `thread_id`로 대화 유지 |
| `academy_l7_structured_output` | 구조화 출력 | `TypedDict`, `response_format` |

## 셋업

### 1. uv 설치 (없으면)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 의존성 설치
```bash
uv sync
```

### 3. `.env` 파일 생성
```
GOOGLE_API_KEY=AIza...
```
키 발급: https://aistudio.google.com/apikey

### 4. 실행
```bash
uv run basic_agent.py
uv run langchain_academy/langchain_academy_l1_fast_agent.py
```

> Chinook.db가 필요한 예제(L1, L6)는 사전에 다운로드 필요:
> ```bash
> curl -L https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite -o Chinook.db
> ```

## 의존성

| 패키지 | 용도 |
|--------|------|
| `langchain`, `langchain-google-genai` | 코어, Gemini 연동 |
| `langchain-community` | SQLDatabase 등 커뮤니티 도구 |
| `langchain-anthropic`, `langchain-openai` | 다른 모델 제공자 (옵션) |
| `langchain-mcp-adapters` | MCP 서버 연동 (L5) |
| `deepagents` | `create_deep_agent` (realworld_agent) |
| `langgraph-cli[inmem]` | LangGraph Studio 로컬 실행 |
| `truststore` | 사내 SSL 인증서 체인 사용 (선택) |
| `python-dotenv` | `.env` 로드 |

## 참고 자료

- LangChain Quickstart: https://docs.langchain.com/oss/python/langchain/quickstart
- LangChain Academy: https://academy.langchain.com
- Gemini API: https://ai.google.dev/gemini-api/docs
