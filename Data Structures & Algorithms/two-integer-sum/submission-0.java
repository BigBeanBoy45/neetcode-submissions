class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();
        // {value : index}

        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            Integer val = map.get(target - n);
            if (val != null) return new int[] {val, i};
            map.put(n, i);
        }

        return null;
        
    }
}
