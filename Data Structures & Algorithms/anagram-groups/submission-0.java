class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> res = new ArrayList<>();
        int len = strs.length;
        HashMap<HashMap<Character, Integer>, List<String>> charCounts = new HashMap<>();
        // group char counts with string anagrams

        for (String s : strs) {

            HashMap<Character, Integer> count = new HashMap<>();
            
            // parse string
            for (int i = 0; i < s.length(); i++) {

                char c = s.charAt(i);

                count.put(c, count.getOrDefault(c, 0) + 1); // getOrDefault(key, defaultIfFail)

            } // end string parse

            charCounts.putIfAbsent(count, new ArrayList<String>());
            charCounts.get(count).add(s);

        } // end strs traversal

        // transform data
        for (List<String> l : charCounts.values()) {
            res.add(l);
        }

        return res;

    }
}
