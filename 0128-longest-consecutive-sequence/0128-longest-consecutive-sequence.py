class Solution:

    # 'nums: list[int]': 정수 리스트가 들어옴
    # 예: [100, 4, 200, 1, 3, 2]
    # '-> int': 가장 긴 연속 수열의 길이를 정수로 반환

    def longestConsecutive(self, nums: list[int]) -> int:

        # 빠른 탐색을 위해 nums를 set으로 변환
        # 예: [100,4,200,1,3,2] -> {100,4,200,1,3,2}
        num_set = set(nums)

        # 가장 긴 연속 수열 길이 저장
        longest = 0

        # set 안의 숫자를 하나씩 확인
        for num in num_set:

            # num-1이 없으면 현재 num이 연속 수열의 시작점
            # 예: num=1 | 0 not in num_set -> 시작점
            if num - 1 not in num_set:

                current = num
                length = 1

                # 다음 숫자가 계속 존재하면 길이 증가
                # 예: 1 -> 2 -> 3 -> 4
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # 지금까지 찾은 최대 길이와 비교
                # 예: longest=0 | length=4 -> longest=4
                longest = max(longest, length)

        return longest