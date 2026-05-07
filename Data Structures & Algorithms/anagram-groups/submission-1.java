class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // output
        List<List<String>> res = new ArrayList<>();

        // group char counts with string anagrams
        HashMap<HashMap<Character, Integer>, List<String>> charCounts = new HashMap<>();

        for (String s : strs) {
            
            // collects frequencies of characters
            HashMap<Character, Integer> count = new HashMap<>();
            
            // parse string, record frequencies
            for (int i = 0; i < s.length(); i++) {

                char c = s.charAt(i);

                count.put(c, count.getOrDefault(c, 0) + 1); // getOrDefault(key, defaultIfFail)

            } // end string parse

            // if new anagram, create new key-value pair
            charCounts.putIfAbsent(count, new ArrayList<String>());
            
            // add current string value to existing key-value value
            charCounts.get(count).add(s);

        } // end strs traversal

        // transform data, collect strings with grouped anagrams
        for (List<String> l : charCounts.values()) res.add(l);

        return res;

    }
}
