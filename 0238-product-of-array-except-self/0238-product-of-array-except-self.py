class Solution:

    # 'nums: list[int]': 정수 리스트가 들어옴
    # 예: [1, 2, 3, 4]
    # '-> list[int]': 정수 리스트를 반환

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # 결과 리스트 생성
        # 처음에는 곱셈에 영향 없는 1로 채움
        # 예: nums=[1,2,3,4] | result=[1,1,1,1]
        result = [1] * len(nums)

        # 현재 위치 왼쪽 숫자들의 누적 곱
        # 처음에는 왼쪽에 아무것도 없으므로 1
        prefix = 1

        # 왼쪽 -> 오른쪽 순회
        for i in range(len(nums)):

            # 현재 index의 왼쪽 숫자들의 곱 저장
            # 예: i=2 | prefix=1*2=2 | result[2]=2
            result[i] = prefix

            # 다음 index를 위해 현재 nums[i]까지 곱함
            # 예: i=2 | prefix=2 | nums[2]=3 | prefix=6
            prefix *= nums[i]

        # 현재 위치 오른쪽 숫자들의 누적 곱
        # 처음에는 오른쪽에 아무것도 없으므로 1
        suffix = 1

        # 오른쪽 -> 왼쪽 순회
        for i in range(len(nums) - 1, -1, -1):

            # 기존 왼쪽 곱에 오른쪽 곱을 곱함
            # 예: i=1 | result[1]=1 | suffix=12 | result[1]=12
            result[i] *= suffix

            # 다음 index를 위해 현재 nums[i]까지 곱함
            # 예: i=1 | suffix=12 | nums[1]=2 | suffix=24
            suffix *= nums[i]

        # 예: [24, 12, 8, 6]
        return result