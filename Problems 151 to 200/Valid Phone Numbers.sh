# https://leetcode.com/problems/valid-phone-numbers

# Runtime: 121 ms, faster than 68.51% of Bash online submissions for Valid Phone Numbers.
# Good runtime, perhaps would be faster if there wasn't the use of Perl regex? 

# Memory Usage: 3.2 MB, less than 8.52% of Bash online submissions for Valid Phone Numbers.
# Very poor memory usage, again likely to be caused by the use of Perl instead of standard regex


# Read from the file file.txt and output all valid phone numbers to stdout.
# thanks to: https://medium.com/@ChYuan/leetcode-193-valid-phone-numbers-%E5%BF%83%E5%BE%97-easy-ff49c940d484

grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
