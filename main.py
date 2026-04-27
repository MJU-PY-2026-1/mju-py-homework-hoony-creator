# 파일 이름 : 프로젝트 볼트
# 작 성 자 : 변성훈

# 2차 과제용: 입출력 + 리스트 + 조건문

print("===== 프로젝트 볼트(Project Vault) v2.0 =====")

# 1. 프로젝트 정보 입력
project_name = input("프로젝트 이름을 입력하세요: ")
project_field = input("프로젝트 분야를 입력하세요: ")
final_goal = input("최종 목표를 입력하세요: ")

progress = int(input("현재 진행률(0~100)을 입력하세요: "))
file_count = int(input("저장한 자료 개수를 입력하세요: "))
priority = int(input("프로젝트 중요도(0~10)를 입력하세요: "))
inactive_days = int(input("최근 활동 공백일 수를 입력하세요: "))
review_input = input("회고를 작성했나요? (yes/no): ")
link_count = int(input("등록한 링크 개수를 입력하세요: "))

# 2. 회고 작성 여부를 True / False로 변환
if review_input.lower() == "yes":
    review_done = True
else:
    review_done = False

# 3. 프로젝트 정보를 리스트에 저장
project = [
    project_name,
    project_field,
    final_goal,
    progress,
    file_count,
    priority,
    inactive_days,
    review_done,
    link_count
]

# 4. 전체 프로젝트 보관용 리스트에 추가
project_vault = []
project_vault.append(project)

# 5. 준비도 점수 계산
readiness_score = progress + (file_count * 5) + (link_count * 3) + priority

if review_done:
    readiness_score = readiness_score + 10

# 6. 프로젝트 상태 판정
if inactive_days >= 7:
    status = "휴면 프로젝트"
elif readiness_score >= 90:
    status = "순항"
elif readiness_score >= 70:
    status = "진행 중"
elif readiness_score >= 50:
    status = "정체"
else:
    status = "위험"

# 7. 특별 칭호 판정
title = "일반 프로젝트"

if progress >= 80 and file_count >= 8 and review_done:
    title = "포트폴리오 완성형"
elif file_count >= 10 and link_count >= 5:
    title = "아카이브 마스터"
elif progress >= 70 and inactive_days <= 1:
    title = "폭풍 성장 프로젝트"
elif file_count >= 8 and progress < 40:
    title = "자료만 많은 프로젝트"

# 8. 결과 출력
print("\n===== 저장된 프로젝트 정보 =====")
print(f"프로젝트 이름: {project_vault[0][0]}")
print(f"프로젝트 분야: {project_vault[0][1]}")
print(f"최종 목표: {project_vault[0][2]}")
print(f"현재 진행률: {project_vault[0][3]}%")
print(f"저장한 자료 개수: {project_vault[0][4]}개")
print(f"프로젝트 중요도: {project_vault[0][5]}")
print(f"최근 활동 공백일 수: {project_vault[0][6]}일")
print(f"회고 작성 여부: {project_vault[0][7]}")
print(f"등록한 링크 개수: {project_vault[0][8]}개")

print("\n===== 프로젝트 분석 결과 =====")
print(f"준비도 점수: {readiness_score}")
print(f"현재 상태: {status}")
print(f"특별 칭호: {title}")

print(f"\n'{project_name}' 프로젝트가 프로젝트 볼트에 저장되었습니다.")
