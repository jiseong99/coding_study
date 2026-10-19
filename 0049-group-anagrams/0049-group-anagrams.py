class Solution:

    # 'strs: list[str]': 문자열 리스트가 들어옴
    # 예: ["eat", "tea", "tan", "ate", "nat", "bat"]
    # '-> list[list[str]]': 문자열 리스트들을 묶은 리스트를 반환

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # 같은 anagram끼리 묶어서 저장할 딕셔너리
        # key = 정렬된 문자열 / value = 같은 그룹의 원본 문자열 리스트
        # 예: "aet" -> ["eat", "tea", "ate"]
        groups = {}

        # strs 안의 문자열을 하나씩 순회
        # 예: "eat" -> "tea" -> "tan" ...
        for word in strs:

            # 문자열을 정렬해서 같은 anagram인지 판단할 key 생성
            # sorted("eat") -> ['a', 'e', 't']
            # ''.join(...) -> "aet"
            key = ''.join(sorted(word))

            # key가 아직 딕셔너리에 없으면 빈 리스트 생성
            # 예: key = "aet" | groups["aet"] = []
            if key not in groups:
                groups[key] = []

            # 현재 단어를 해당 anagram 그룹에 추가
            # 예: groups["aet"].append("eat")
            # 결과: {"aet": ["eat"]}
            groups[key].append(word)

        # 딕셔너리의 value들만 리스트로 반환
        # 예: {"aet": [...], "ant": [...], "abt": [...]}
        # -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
        return list(groups.values())