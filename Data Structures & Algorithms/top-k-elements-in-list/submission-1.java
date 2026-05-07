class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // defining output
        // int[] res = new int[k];

        // value : frequency
        HashMap<Integer, Integer> frequencies = new HashMap<>();

        for (int n : nums) {

            frequencies.putIfAbsent(n, 0);
            frequencies.put(n, frequencies.get(n) + 1);

        }

        int[] res = frequencies.entrySet()
        .stream()
        // sort by frequencies
        .sorted( (freq1, freq2) -> freq2.getValue().compareTo(freq1.getValue()) )
        .limit(k)
        .mapToInt(entry -> entry.getKey())
        .toArray();

        return res;

        
    }
}
