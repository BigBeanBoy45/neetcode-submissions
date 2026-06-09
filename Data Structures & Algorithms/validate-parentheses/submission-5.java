class Solution {
    public boolean isValid(String s) {
        
        if (s.length() % 2 != 0) return false;
        
        Stack<Character> stack = new Stack<>();
        
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                System.out.println(stack);
                if (stack.isEmpty()) return false;
                if (!matchPar(stack.pop(), c)) return false;
            }
            
            i++;
        }

        return stack.isEmpty();
    }

    public boolean matchPar(char a, char b) {
        if (a == '(' && b == ')') return true;
        else if (a == '{' && b == '}') return true;
        else if (a == '[' && b == ']') return true;
        return false;
    }
}
