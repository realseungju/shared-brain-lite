# Shared Brain Lite

여러 AI 에이전트가 Git 저장소를 공용 기억으로 사용하는 경량 스타터입니다.

핵심 흐름:

```text
아이디어 캡처 → 계획·Spec → Task → 작업 → Session 요약 → 다음 에이전트
```

모든 정보는 평문 Markdown으로 남습니다. 특정 모델이나 채팅 세션의 기억에 의존하지 않습니다.

## 포함 기능

- Claude, Codex, Gemini, Copilot용 공통 진입점
- Tier 0/1/2 계층형 읽기
- `inbox → spec → task` 계획 게이트
- `backlog → doing → done` task 생명주기
- 태그·훅이 있는 session 요약과 index
- task/session 생성기
- 기본 구조를 검사하는 `brain-lint`
- pre-commit과 GitHub Actions 품질 게이트
- 지식 노드와 ADR 템플릿

## 포함하지 않는 기능

- 개인 일정·아이디어 관리
- 연구 문서·실험 결과 관리
- 외부 캘린더나 GitHub Issue 동기화
- 멀티 worktree 자동 통합
- 모델 라우팅·평가·에이전트 안전 훅

`personal/`과 `research/`는 향후 확장 지점으로만 비워 두었습니다. 실제 사용자가 필요를 요청하면
`tasks/backlog/`의 선택형 기능 task를 Planning부터 진행하세요.

## 10분 시작

요구사항: Git, Python 3.10 이상. 외부 Python 패키지는 필요하지 않습니다.

1. `system/context.md`에 현재 프로젝트를 적습니다.
2. 첫 task를 생성합니다.

```sh
python infra/new-task.py first-task --title "첫 작업"
```

3. 생성된 파일을 `tasks/backlog/`에서 채우고, 착수할 때 `tasks/doing/`으로 옮깁니다.
4. 작업을 마칠 때 session 요약을 생성합니다.

```sh
python infra/new-session.py first-session \
  --agent Codex \
  --tags demo \
  --hook "첫 작업 흐름 검증" \
  --did "첫 task를 생성하고 구조를 확인함" \
  --next "실제 프로젝트 context 작성"
```

5. 구조를 검사합니다.

```sh
python infra/brain-lint.py
python -m unittest discover -s infra/tests -v
```

## 구조

```text
system/       운영 규칙·현재 context·session·ADR
tasks/        backlog/doing/done
specs/        구현 전 명세
inbox/        아직 계획되지 않은 아이디어
knowledge/    재사용 가능한 지식 노드
skills/       사용자 정의 스킬 확장점
personal/     선택형 확장점, 기본 기능 없음
research/     선택형 확장점, 기본 기능 없음
infra/        생성기·lint·테스트·Git hook
```

## Git hook

선택 사항입니다. 설치하면 commit 전에 `brain-lint`가 실행됩니다.

```sh
git config core.hooksPath infra/hooks
```

## 운영 원칙

- 기록되지 않은 작업은 다음 에이전트가 알 수 없습니다.
- 전체 저장소를 매번 읽지 말고 필요한 Tier만 읽습니다.
- inbox 항목은 Spec과 task로 구조화하기 전 구현하지 않습니다.
- 실제 개인정보·비밀·대용량 연구 데이터는 공개 저장소에 넣지 않습니다.
