# 파일 이름 : 프로젝트 볼트
# 작 성 자 : 변성훈

# 3차 과제: 무한 루프 + 메뉴 시스템 + 리스트 + 조건문 + 반복문

print("===== Project Vault v3.0 =====")
print("장기 프로젝트와 포트폴리오 자료를 함께 관리하는 시스템입니다.")

project_vault = []

while True:
    print("\n==============================")
    print("1. 프로젝트 등록")
    print("2. 전체 프로젝트 조회")
    print("3. 위험 / 휴면 프로젝트 조회")
    print("4. 포트폴리오 완성형 프로젝트 조회")
    print("5. 자료 추가 기록")
    print("0. 프로그램 종료")
    print("==============================")

    menu = input("메뉴 번호를 선택하세요: ").strip()

    # 1. 프로젝트 등록
    if menu == "1":
        print("\n[프로젝트 등록]")

        project_name = input("프로젝트 이름: ").strip()
        project_field = input("프로젝트 분야: ").strip()
        final_goal = input("최종 목표: ").strip()

        while True:
            progress_input = input("현재 진행률(0~100): ").strip()
            if progress_input.isdigit():
                progress = int(progress_input)
                if 0 <= progress <= 100:
                    break
            print("진행률은 0~100 사이의 정수를 입력하세요.")

        while True:
            file_input = input("저장한 자료 개수: ").strip()
            if file_input.isdigit():
                file_count = int(file_input)
                break
            print("자료 개수는 0 이상의 정수를 입력하세요.")

        while True:
            priority_input = input("프로젝트 중요도(0~10): ").strip()
            if priority_input.isdigit():
                priority = int(priority_input)
                if 0 <= priority <= 10:
                    break
            print("중요도는 0~10 사이의 정수를 입력하세요.")

        while True:
            inactive_input = input("최근 활동 공백일 수: ").strip()
            if inactive_input.isdigit():
                inactive_days = int(inactive_input)
                break
            print("공백일 수는 0 이상의 정수를 입력하세요.")

        while True:
            review_input = input("회고를 작성했나요? (yes/no 또는 예/아니오): ").strip().lower()
            if review_input in ["yes", "y", "예", "ㅇ"]:
                review_done = True
                break
            elif review_input in ["no", "n", "아니오", "아니요", "ㄴ"]:
                review_done = False
                break
            print("yes/no 또는 예/아니오 형태로 입력하세요.")

        while True:
            link_input = input("등록한 링크 개수: ").strip()
            if link_input.isdigit():
                link_count = int(link_input)
                break
            print("링크 개수는 0 이상의 정수를 입력하세요.")

        while True:
            memo_input = input("저장한 메모 개수: ").strip()
            if memo_input.isdigit():
                memo_count = int(memo_input)
                break
            print("메모 개수는 0 이상의 정수를 입력하세요.")

        project = [
            project_name,   # 0
            project_field,  # 1
            final_goal,     # 2
            progress,       # 3
            file_count,     # 4
            priority,       # 5
            inactive_days,  # 6
            review_done,    # 7
            link_count,     # 8
            memo_count      # 9
        ]

        project_vault.append(project)
        print(f"\n'{project_name}' 프로젝트가 Project Vault에 저장되었습니다.")

    # 2. 전체 프로젝트 조회
    elif menu == "2":
        print("\n[전체 프로젝트 조회]")

        if len(project_vault) == 0:
            print("저장된 프로젝트가 없습니다.")
        else:
            number = 1
            for project in project_vault:
                project_name = project[0]
                project_field = project[1]
                final_goal = project[2]
                progress = project[3]
                file_count = project[4]
                priority = project[5]
                inactive_days = project[6]
                review_done = project[7]
                link_count = project[8]
                memo_count = project[9]

                readiness_score = progress + (file_count * 5) + (link_count * 3) + (memo_count * 2) + priority
                if review_done:
                    readiness_score = readiness_score + 10

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

                title = "일반 프로젝트"
                if progress >= 80 and file_count >= 8 and review_done:
                    title = "포트폴리오 완성형"
                elif file_count >= 10 and link_count >= 5:
                    title = "아카이브 마스터"
                elif progress >= 70 and inactive_days <= 1:
                    title = "폭풍 성장 프로젝트"
                elif file_count >= 8 and progress < 40:
                    title = "자료만 많은 프로젝트"

                print("\n------------------------------")
                print(f"[{number}] 프로젝트 이름: {project_name}")
                print(f"분야: {project_field}")
                print(f"최종 목표: {final_goal}")
                print(f"진행률: {progress}%")
                print(f"자료 개수: {file_count}개")
                print(f"링크 개수: {link_count}개")
                print(f"메모 개수: {memo_count}개")
                print(f"중요도: {priority}")
                print(f"최근 활동 공백일 수: {inactive_days}일")
                print(f"회고 작성 여부: {review_done}")
                print(f"준비도 점수: {readiness_score}")
                print(f"현재 상태: {status}")
                print(f"특별 칭호: {title}")
                number = number + 1

    # 3. 위험 / 휴면 프로젝트 조회
    elif menu == "3":
        print("\n[위험 / 휴면 프로젝트 조회]")

        if len(project_vault) == 0:
            print("저장된 프로젝트가 없습니다.")
        else:
            found = 0
            number = 1

            for project in project_vault:
                project_name = project[0]
                progress = project[3]
                file_count = project[4]
                priority = project[5]
                inactive_days = project[6]
                review_done = project[7]
                link_count = project[8]
                memo_count = project[9]

                readiness_score = progress + (file_count * 5) + (link_count * 3) + (memo_count * 2) + priority
                if review_done:
                    readiness_score = readiness_score + 10

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

                if status == "위험" or status == "휴면 프로젝트":
                    print(f"{number}. {project_name} / 준비도 점수: {readiness_score} / 상태: {status}")
                    found = found + 1
                number = number + 1

            if found == 0:
                print("위험하거나 휴면 상태인 프로젝트가 없습니다.")

    # 4. 포트폴리오 완성형 프로젝트 조회
    elif menu == "4":
        print("\n[포트폴리오 완성형 프로젝트 조회]")

        if len(project_vault) == 0:
            print("저장된 프로젝트가 없습니다.")
        else:
            found = 0
            number = 1

            for project in project_vault:
                project_name = project[0]
                progress = project[3]
                file_count = project[4]
                priority = project[5]
                inactive_days = project[6]
                review_done = project[7]
                link_count = project[8]
                memo_count = project[9]

                readiness_score = progress + (file_count * 5) + (link_count * 3) + (memo_count * 2) + priority
                if review_done:
                    readiness_score = readiness_score + 10

                title = "일반 프로젝트"
                if progress >= 80 and file_count >= 8 and review_done:
                    title = "포트폴리오 완성형"
                elif file_count >= 10 and link_count >= 5:
                    title = "아카이브 마스터"
                elif progress >= 70 and inactive_days <= 1:
                    title = "폭풍 성장 프로젝트"
                elif file_count >= 8 and progress < 40:
                    title = "자료만 많은 프로젝트"

                if title == "포트폴리오 완성형":
                    print(f"{number}. {project_name} / 준비도 점수: {readiness_score} / 특별 칭호: {title}")
                    found = found + 1
                number = number + 1

            if found == 0:
                print("포트폴리오 완성형 프로젝트가 없습니다.")

    # 5. 자료 추가 기록
    elif menu == "5":
        print("\n[자료 추가 기록]")

        if len(project_vault) == 0:
            print("먼저 프로젝트를 등록해야 합니다.")
        else:
            print("저장된 프로젝트 목록:")
            number = 1
            for project in project_vault:
                print(f"{number}. {project[0]}")
                number = number + 1

            while True:
                target_input = input("자료를 추가할 프로젝트 번호를 선택하세요: ").strip()
                if target_input.isdigit():
                    target_index = int(target_input) - 1
                    if 0 <= target_index < len(project_vault):
                        break
                print("올바른 프로젝트 번호를 입력하세요.")

            while True:
                add_file_input = input("추가할 자료 개수: ").strip()
                if add_file_input.isdigit():
                    add_file = int(add_file_input)
                    break
                print("자료 개수는 0 이상의 정수를 입력하세요.")

            while True:
                add_link_input = input("추가할 링크 개수: ").strip()
                if add_link_input.isdigit():
                    add_link = int(add_link_input)
                    break
                print("링크 개수는 0 이상의 정수를 입력하세요.")

            while True:
                add_memo_input = input("추가할 메모 개수: ").strip()
                if add_memo_input.isdigit():
                    add_memo = int(add_memo_input)
                    break
                print("메모 개수는 0 이상의 정수를 입력하세요.")

            project_vault[target_index][4] = project_vault[target_index][4] + add_file
            project_vault[target_index][8] = project_vault[target_index][8] + add_link
            project_vault[target_index][9] = project_vault[target_index][9] + add_memo

            print(f"\n'{project_vault[target_index][0]}' 프로젝트의 자료가 업데이트되었습니다.")

    # 0. 종료
    elif menu == "0":
        print("\nProject Vault를 종료합니다.")
        print("프로그램을 이용해 주셔서 감사합니다.")
        break

    # 잘못된 메뉴 입력
    else:
        print("올바른 메뉴 번호를 입력하세요.")
