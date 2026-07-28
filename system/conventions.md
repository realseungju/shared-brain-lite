# Conventions

## 파일명

| 위치 | 형식 |
|---|---|
| `tasks/*/` | `TYYYY-MM-DD-{slug}.md` |
| `system/sessions/` | `YYYY-MM-DD-{slug}.md` |
| `specs/` | `{slug}.md` |
| `knowledge/` | `{slug}.md` |
| `inbox/` | `YYYYMMDD-{source}-{slug}.md` |

slug는 소문자 영문·숫자·하이픈만 쓴다.

## Task 상태

```text
backlog → doing → done
```

완료 이유:

- `completed`: 목표 달성
- `cancelled`: 중단하고 재개 계획 없음
- `superseded`: 다른 접근으로 대체

## Commit

Conventional Commits를 권장한다.

```text
<type>(<scope>): <imperative summary>
```

## 문서

- 결론을 먼저 쓴다.
- 같은 내용을 여러 문서에 복제하지 않는다.
- 실제 상태와 재사용 지식을 분리한다.
- 다음 에이전트가 필요한 만큼만 남긴다.
