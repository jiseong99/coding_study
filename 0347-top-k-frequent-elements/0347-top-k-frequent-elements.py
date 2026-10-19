class Solution:

    # 'nums: list[int]': 정수 리스트가 들어옴
    # 예: [1,1,1,2,2,3]
    # 'k: int': 가장 자주 나온 숫자 몇 개를 찾을지
    # '-> list[int]': 정수 리스트를 반환

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # 각 숫자가 몇 번 나왔는지 저장할 딕셔너리
        # key = 숫자 / value = 등장 횟수
        # 예: {1: 3, 2: 2, 3: 1}
        count = {}

        # nums의 숫자를 하나씩 순회하면서 빈도수 증가
        # 예: num=1 | count.get(1, 0)=0 | count[1]=1
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # bucket[i] = i번 등장한 숫자들을 저장
        # nums 길이가 6이면 index 0~6까지 생성
        # 예: bucket[3] = [1] -> 숫자 1이 3번 등장
        bucket = [[] for _ in range(len(nums) + 1)]

        # count 딕셔너리의 key, value를 동시에 순회
        # 예: num=1 | freq=3
        for num, freq in count.items():
            bucket[freq].append(num)

        # 최종 정답을 저장할 리스트
        result = []

        # 빈도수가 높은 곳부터 역순으로 확인
        # 예: len(nums)=6이면 6 -> 5 -> 4 -> 3 -> ...
        for freq in range(len(bucket) - 1, 0, -1):

            # 해당 빈도수에 있는 숫자들을 하나씩 확인
            for num in bucket[freq]:

                # 결과 리스트에 추가
                # 예: result=[] | num=1 -> result=[1]
                result.append(num)

                # k개를 모았으면 바로 반환
                # 예: k=2 | result=[1,2] -> return
                if len(result) == k:
                    return result