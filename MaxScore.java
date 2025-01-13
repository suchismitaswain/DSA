import java.util.Comparator;
import java.util.HashSet;
import java.util.List;

class Solution {
    public int maxScore(List<List<Integer>> grid) {
        for (var row : grid)
            row.sort(Comparator.reverseOrder());
        solve(0, 0, new HashSet<>(), grid);
        return ans;
    }

    int ans = 0;

    void solve(int i, int sum, HashSet<Integer> set, List<List<Integer>> grid) {
        if (sum + (grid.size() - i) * (200 - (grid.size() - i - 1)) / 2 < ans)
            return;

        if (i == grid.size()) {
            ans = Math.max(ans, sum);
            return;
        }

        solve(i + 1, sum, set, grid);
        HashSet<Integer> rowVis = new HashSet<>();
        for (int x : grid.get(i)) {
            if (set.contains(x) || rowVis.contains(x))
                continue;
            rowVis.add(x);

            set.add(x);
            solve(i + 1, sum + x, set, grid);
            set.remove(x);
        }
    }
}