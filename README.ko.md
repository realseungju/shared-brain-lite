# Shared Brain Lite

여러 AI 에이전트가 Git 저장소를 **공용 장기 기억**으로 쓰기 위한 경량 스타터입니다.

English: [README.md](README.md)

채팅 세션은 잊습니다. Claude·Codex·Gemini·Copilot은 서로의 기억을 공유하지 않습니다.
이 저장소는 기억을 *저장소 자체*에 둡니다 — 평문 Markdown, 모든 도구가 읽는 단일 진입점,
그리고 기록이 썩지 않게 막는 lint 게이트.

```text
아이디어 캡처 → 계획·Spec → Task → 작업 → Session 요약 → 다음 에이전트
```

## 그냥 메모 폴더와 뭐가 다른가

자유 형식 메모는 아무것도 강제하지 않아서 썩습니다. 썩지 않게 하는 장치는 셋입니다.

- **계층형 읽기.** 에이전트는 `system/RULES.md`, `system/context.md`, session index 꼬리
  몇 줄, `tasks/doing/` 파일명만 읽습니다. 나머지는 그 task가 필요로 할 때만 엽니다.
  저장소가 커져도 온보딩 비용이 일정하게 유지됩니다.
- **손편집 대신 생성기.** task·session 파일은 스크립트가 만듭니다. 그래서 모든 기록이
  같은 frontmatter 스키마를 갖고 올바른 위치에 놓입니다.
- **lint 게이트.** `brain-lint.py`가 pre-commit과 CI에서 돕니다. index에 없는 session,
  result 없이 `done/`에 있는 task, 파일명과 어긋나는 task id — 전부 거부됩니다.
  검사하지 않는 구조는 조용히 사실이 아니게 됩니다.

## 10분 시작

요구사항: Git, Python 3.10 이상. 외부 Python 패키지는 필요하지 않습니다.

1. `system/context.md`에 실제 하는 일을 적습니다.
2. 첫 task를 생성합니다.

```sh
python infra/new-task.py first-task --title "첫 작업"
```

3. `tasks/backlog/`에 생성된 파일을 채웁니다. 착수할 때 `tasks/doing/`으로 옮기고
   **`agent`와 `started` 필드를 반드시 채웁니다** — `brain-lint`가 요구하므로 비워 두면
   pre-commit에서 커밋이 막힙니다. 필드 이름과 허용값은
   [`system/conventions.md`](system/conventions.md)에 전부 있습니다.
4. 작업을 마칠 때 session 요약을 생성합니다.

```sh
python infra/new-session.py first-session \
  --agent Codex \
  --tags demo \
  --hook "다음 에이전트가 이 줄만 읽고 본문을 열지 판단한다" \
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
system/       운영 규칙·현재 context·session 요약·ADR
tasks/        backlog / doing / done
specs/        만들기 전에 쓰는 명세
inbox/        아직 계획되지 않은 아이디어
knowledge/    프로젝트를 넘어 재사용되는 교훈
research/     프로젝트별 연구 문서·실험 기록 (Tier 2)
skills/       도구별 스킬 확장점
personal/     확장점, 기본은 비어 있음
infra/        생성기·lint·테스트·Git hook
```

`system/RULES.md`가 운영 규칙의 단일 출처입니다. `CLAUDE.md`·`AGENTS.md`·`GEMINI.md`·
`.github/copilot-instructions.md`는 전부 그걸 가리키는 얇은 stub이라, 새 AI 도구를 붙일 때
규칙 사본이 아니라 stub 하나만 늘어납니다.

## 포함 기능

- Claude·Codex·Gemini·Copilot 공통 진입점
- Tier 0/1/2 계층형 읽기
- `inbox → spec → task` 계획 게이트
- `backlog → doing → done` task 생명주기
- 태그·훅이 있는 session 요약과 append-only index
- task/session 생성기
- pre-commit과 GitHub Actions에 연결된 `brain-lint` 구조 검사
- spec·knowledge 노드·연구 문서·실험 기록 템플릿

## 포함하지 않는 기능

- 개인 일정·아이디어 관리 (`personal/`은 의도적으로 비움 — ADR-002)
- 외부 캘린더·GitHub Issue 동기화
- 멀티 worktree 자동 통합
- 모델 라우팅·평가 하니스·에이전트 안전 훅

전부 의도적으로 뺐습니다. 이유는 `system/decisions.md`에, 실제로 필요해졌을 때 착수할
opt-in task는 `tasks/backlog/`에 있습니다.

## Git hook

선택 사항이지만 권장합니다. 매 commit 전에 `brain-lint`가 실행됩니다.

```sh
git config core.hooksPath infra/hooks
```

**실제로 도는지 확인하세요** — 있다고 믿는데 안 도는 게이트는 없느니만 못합니다.

```sh
git commit --allow-empty -m "hook check"   # "brain-lint: 클린 ✓"가 찍혀야 정상
```

GitHub Actions가 push·PR마다 같은 lint와 테스트를 돌리므로, 로컬 훅이 빠져도 CI가 잡습니다.

## 둘 이상이 같이 쓸 때

각자 자기 사본을 쓰거나, 하나의 repo를 공유할 수 있습니다. 공유한다면
`system/sessions/index.md`가 append-only라 두 사람이 session을 닫을 때마다 확정적으로
충돌합니다 — `.gitattributes`에 `merge=union`을 걸어 두어 양쪽 줄이 모두 보존됩니다.
task·session 본문은 1항목=1파일이라 충돌면이 없습니다.

## 원칙

- 기록되지 않은 작업은 다음 에이전트에게 존재하지 않습니다.
- 저장소 전체가 아니라 필요한 Tier만 읽습니다.
- inbox 항목은 Spec이나 task가 되기 전에 구현하지 않습니다.
- 실제 비밀정보·개인정보·대용량 연구 산출물은 공개 저장소에 넣지 않습니다.

## License

MIT — [LICENSE](LICENSE) 참조.
