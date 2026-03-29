---
name: ps-problem-workflow
description: Project-specific workflow for this repository when reorganizing uncategorized `leetcode/` or `programmers/` solution files, updating `logs/YYYY-MM-DD.md`, and making per-problem commits followed by a daily summary commit.
---

# PS Problem Workflow

이 스킬은 이 저장소에서 `leetcode/`, `programmers/`, `logs/`를 정리할 때 사용하는 프로젝트 전용 워크플로우다.

## When to Use

- `leetcode/` 또는 `programmers/` 아래에 카테고리 미분류 `*.py` 파일이 있을 때
- 문제 풀이 파일을 유형별 디렉토리로 재배치해야 할 때
- 오늘 정리한 문제를 `logs/YYYY-MM-DD.md`에 요약해야 할 때
- 문제별 커밋과 일일 요약 커밋까지 한 번에 정리해야 할 때

## Required Workflow

1. `leetcode/`와 `programmers/` 아래에서 카테고리로 분류되지 않은 `*.py` 파일을 찾는다.
2. 각 문제를 풀이 방식과 사용 자료구조 기준으로 유형별로 분류한다.
3. 분류 결과에 맞춰 문제 파일을 적절한 카테고리 디렉토리로 이동한다.
4. 이동한 문제들을 `logs/YYYY-MM-DD.md`에 기록한다.
5. 각 문제 파일은 하나씩 개별 커밋한다.
6. 마지막으로 해당 날짜의 로그 파일을 별도 커밋한다.

## Log Format

- 로그 경로: `logs/YYYY-MM-DD.md`
- 각 항목은 최대한 간단하게 작성한다.
- 형식: `문제번호: 풀이방식 및 사용 데이터 구조`
- 문제 유형이 드러나도록 작성한다.

예시:

```md
42579: 해시 기반 집계, 딕셔너리 + 정렬
12978: 다익스트라, 힙
```

## Commit Rules

- 문제 파일 커밋 메시지: `[solve] 문제이름`
- 로그 파일 커밋 메시지: `[summary] YYYY-MM-DD`
- 문제 파일은 반드시 하나씩 따로 커밋한다.
- 로그 커밋은 모든 문제 정리 후 마지막에 수행한다.

## Must Do

- 기존 디렉토리 구조를 먼저 확인하고 그 구조에 맞는 카테고리로 이동한다.
- 분류 기준은 문제의 핵심 알고리즘/자료구조 기준으로 잡는다.
- 로그에는 이번에 이동하거나 정리한 문제만 추가한다.
- 커밋 전에 이동된 파일과 로그 내용을 다시 검토한다.

## Must Not Do

- 여러 문제를 한 커밋에 묶지 않는다.
- 로그 커밋을 문제 커밋보다 먼저 하지 않는다.
- 로그를 장황하게 쓰지 않는다.
- 임의로 문제 내용을 다시 풀거나 대규모 리팩터링하지 않는다.

## Repository Scope

- Problem sources: `leetcode/`, `programmers/`
- Log destination: `logs/`
