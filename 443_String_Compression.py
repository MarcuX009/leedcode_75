# Solution for `443. String Compression`
class Solution:
    def compress(self, chars: List[str]) -> int:
        write_position = 0
        i = 0 # current_position

        while i < len(chars):
            char = chars[i] # record this char
            count = 0

            # continue to count
            while i < len(chars) and chars[i] == char:
                count += 1
                i += 1

            # if not the same, records this char into `chars``
            chars[write_position] = char
            write_position += 1

            # record the num
            if count > 1:
                for digit in str(count):
                    chars[write_position] = digit
                    write_position += 1
        
        return write_position
