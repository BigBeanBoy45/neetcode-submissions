class Solution {
    public boolean hasDuplicate(int[] nums) {

        // true when duplicate, false when not

        HashSet<Integer> seen = new HashSet<>();

        for (int i : nums) {

            if (seen.contains(i)) return true;
            seen.add(i);

        }

        return false;

    }
}