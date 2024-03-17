from typing import List


class Solution:
    def restore_ip_addresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = list()
        segments = [0] * SEG_COUNT

        def dfs(seg_id: int, seg_start: int):
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            if seg_id == SEG_COUNT:
                if seg_start == len(s):
                    ip_addr = ".".join(str(seg) for seg in segments)
                    ans.append(ip_addr)
                return

            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if seg_start == len(s):
                return

            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[seg_start] == "0":
                segments[seg_id] = 0
                dfs(seg_id + 1, seg_start + 1)

            # 一般情况，枚举每一种可能性并递归
            addr = 0
            for seg_end in range(seg_start, len(s)):
                addr = addr * 10 + (ord(s[seg_end]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[seg_id] = addr
                    dfs(seg_id + 1, seg_end + 1)
                else:
                    break


        dfs(0, 0)
        return ans
