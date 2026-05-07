class Solution {
    public boolean hasDuplicate(int[] nums) {

        // true when duplicate, false when not

        HashSet<Integer> seen = new HashSet<>();

        for (int i : nums) {

            boolean added = seen.add(i);
            if (!added) { return true; }

        }

        return false;

    }
}