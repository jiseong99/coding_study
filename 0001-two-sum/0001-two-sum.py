class Solution:

    # nums: list[int]     nums에는 정수들이 들어있는 리스트가 들어올 예정
    # 예: [2, 7, 11, 15]
    # 자동 캐스팅이 아니라 "타입 힌트"
    # target: int    # target에는 정수가 들어올 예정
    # -> list[int] # 이 함수가 정수 리스트를 반환할 예정이라는 "반환타입힌트"

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 빈 딕셔너리 생성
        # key = 숫자 / value = 그 숫자의 index
        # 예: seen = {2: 0}  /  의미: 숫자 2를 index 0에서 봤다
        seen = {}

        # enumerate(nums):
        # nums를 처음부터 순회하면서ndex와 실제 값을 동시에 가져옴
        # nums = [2, 7, 11, 15]라면
        # 1회차: i = 0, num = 2
        # 2회차: i = 1, num = 7
        # 3회차: i = 2, num = 11
        # 4회차: i = 3, num = 15
        for i, num in enumerate(nums):

            # 현재 숫자 num과 더해서
            # target이 되려면 필요한 숫자를 계산
            # 예: target = 9 | num = 2 | complement = 9 - 2 = 7
            complement = target - num

            # 필요한 숫자(complement)를 이전에 이미 본 적이 있는지 확인
            # 예: complement = 2 | seen = {2: 0} | 2 in seen → True
            if complement in seen:

                # 필요한 숫자의 index와 현재 숫자의 index를 반환
                # 예: seen[2] = 0 | i = 1
                # return [0, 1]
                return [seen[complement], i]

            # 아직 정답을 못 찾았다면 현재 숫자와 index를 딕셔너리에 저장
            # 예: num = 2 | i = 0 | seen[2] = 0
            # 결과: seen = {2: 0}
            seen[num] = i