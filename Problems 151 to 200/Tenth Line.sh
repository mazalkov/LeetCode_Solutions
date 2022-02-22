# https://leetcode.com/problems/tenth-line

# Runtime: 44 ms, faster than 49.75% of Bash online submissions for Tenth Line.
# Not experienced enough with Bash to comment on runtime, seems reasonable for the task.

# Memory Usage: 3.6 MB, less than 79.56% of Bash online submissions for Tenth Line.
# Again not experienced with Bash, the memory usage seems consistent enough for this.


# Read from the file file.txt and output the tenth line to stdout.

sed '10q;d' file.txt
