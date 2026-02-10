class Solution(object):
    def wonderfulSubstrings(self, word):
        # count[mask] = number of prefixes that produced this bitmask.
        # We only track 'a'..'j', so there are 2^10 possible masks.
        count = [0] * 1024
        result = 0
        prefix_xor = 0
        # Empty prefix has mask 0 (all counts even).
        count[prefix_xor] = 1
        
        for char in word:
            # Toggle this character bit in the running parity mask.
            char_index = ord(char) - ord('a')
            prefix_xor ^= 1 << char_index

            # Case 1: same mask -> all characters in substring are even.
            result += count[prefix_xor]

            # Case 2: masks differ by exactly one bit -> one odd character.
            for i in range(10):
                result += count[prefix_xor ^ (1 << i)]

            # Save current prefix mask for future substrings.
            count[prefix_xor] += 1
        
        return result
