class Solution {
    public int missingNumber(int[] nums) {
        int LENGTH = nums.length;
        int correct_sum = ((LENGTH) * (LENGTH+1)) / 2;

        return correct_sum - Arrays.stream(nums).sum();
    }
}
