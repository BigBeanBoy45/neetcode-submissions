class Solution {
    public int evalRPN(String[] tokens) {


        Stack<Integer> nums = new Stack<>();
        Set<String> operators = Set.of("+", "-", "*", "/");

        for (String t : tokens) {

            if (operators.contains(t)) {
                nums.push(evalExpr(nums.pop(), nums.pop(), t));
            } else {
                nums.push(Integer.parseInt(t));
            }

        }

        return nums.peek();
        
    }

    // helper method
    private int evalExpr(int left, int right, String operation) {
        return switch (operation) {
            case "+" -> right + left;
            case "-" -> right - left;
            case "*" -> right * left;
            // case "/" -> right / left;
            default -> right / left;
        };
    }

}
