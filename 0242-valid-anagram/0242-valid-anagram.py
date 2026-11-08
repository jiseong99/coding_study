class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        # 길이가 다르면 같은 문자 구성일 수 없으므로 바로 False
        # 예: "rat" 길이=3 | "cars" 길이=4 -> False
        if len(s) != len(t):
            return False

        # 각 문자가 몇 번 나왔는지 저장할 딕셔너리
        # key = 문자 | value = 등장 횟수
        # 예: count = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        count = {}

        # s의 문자 개수를 하나씩 증가
        # dict.get(key, 0): key가 없으면 기본값 0 반환
        # 예: ch='a' | count.get('a', 0)=0 | count['a']=1
        # 딕셔너리.get(key, 기본값): key가 있으면 value 반환, 없으면 기본값 반환
        # count[ch] = value: key가 없으면 추가, 있으면 기존 value 수정
        # 예: count={} | ch='a' | get('a',0)=0 → count={'a':1}
        # 예: count={'a':1} | ch='a' | get('a',0)=1 → count={'a':2}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # t의 문자 개수를 하나씩 감소
        # 예: ch='a' | count['a']=3 -> 2
        for ch in t:

            # t에 s에는 없던 문자가 나오면 anagram이 아님
            # 예: ch='c' | 'c' not in count -> False
            if ch not in count:
                return False

            # 해당 문자(ch)의 등장 횟수(value)를 1 감소
            # -= 1은 count[ch] = count[ch] - 1과 동일
            # 예: ch='a' | count={'a':3} → count['a'] -= 1 → {'a':2}
            count[ch] -= 1

            # 어떤 문자가 s보다 더 많이 나오면 anagram이 아님
            # 예: count['a'] = -1 -> False
            if count[ch] < 0:
                return False

        # 모든 문자 개수가 정확히 맞으면 True
        return True