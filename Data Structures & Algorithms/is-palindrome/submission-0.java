class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int r = s.length() - 1;

        while (i < r){
            while (i < r && !Character.isLetterOrDigit(s.charAt(i))){
                i++;
            }
            while (r > i && !Character.isLetterOrDigit(s.charAt(r))){
                r--;
            }
            if(Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }
            i++;
            r--;
        }
        return true;
    }
    
}
