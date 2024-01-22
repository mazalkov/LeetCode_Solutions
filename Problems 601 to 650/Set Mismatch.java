class Solution {
    public int[] findErrorNums(int[] nums) {

        int repeated = 0;
        var seen = new HashSet<Integer>();
        int N = nums.length;
        int sumNums = (N * (N+1)) / 2;

        for (int num : nums) {
            sumNums -= num;

            if (seen.contains(num)) {
                repeated = num;
            }
            seen.add(num);
        }

        int[] result = {repeated, sumNums + repeated};
        return result;
    }
}
