class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0
        while i < len(chars):
            group = 1
            while (i + group) < len(chars) and chars[group + i] == chars[i]:
                group += 1
            chars[insert] = chars[i]
            insert += 1
            if group > 1:
                chars[insert:insert  + len(str(group))] = list(str(group))
                insert += len(str(group))

            i += group

        return insert
                

