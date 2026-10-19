class Solution:

    # 'nums: list[int]': nums에는 정수 리스트가 들어옴
    # 예: [1, 2, 3, 1]
    # '-> bool':  True 또는 False를 반환한다는 타입 힌트

    def containsDuplicate(self, nums: list[int]) -> bool:

        # 지금까지 본 숫자들을 저장할 빈 set 생성
        # set은 중복값을 저장하지 않음
        # 예: seen = {1, 2, 3}
        seen = set()

        # nums의 숫자를 하나씩 순회
        # nums = [1, 2, 3, 1]이라면
        # 1회차: num = 1, 2회차: num = 2
        # 3회차: num = 3, 4회차: num = 1
        for num in nums:

            # 현재 숫자를 이전에 본 적이 있으면 중복이 존재하는 것이므로 True 반환
            # 예: num = 1 | seen = {1, 2, 3} | 1 in seen -> True
            if num in seen:
                return True

            # 아직 본 적 없는 숫자라면 set에 저장

            # 예: num = 1 | seen.add(1)
            # 결과: seen = {1}
            seen.add(num)

        # 반복문이 끝날 때까지 중복이 없었다면 모든 숫자가 서로 다르다는 뜻
        return False