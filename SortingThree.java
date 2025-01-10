class Solution {
    public int minimumOperations(List<Integer> nums) {
        final int n = nums.size();
        int ans = n;

        for (int i = 0; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                int operations = 0;

                for (int k = 0; k < n; k++) {
                    int change = 0;

                    if (k < i) {
                        change = (nums.get(k) == 1) ? 0 : 1;
                    }
                    else if (k < j) {
                        change = (nums.get(k) == 2) ? 0 : 1;
                    }
                    else {
                        change = (nums.get(k) == 3) ? 0 : 1;
                    }

                    operations += change;
                }

                ans = Math.min(ans, operations);
            }
        }

        return ans;
    }
}