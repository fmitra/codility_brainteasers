/**

A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

int solution(char *S);
that, given a string S consisting of N characters, returns 1 if string 
S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and 
given S = "())", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage 
required for input arguments).

*/
package solution

func Solution(S string) int {
    b := []byte(S)
    stack := make([]byte, 0)
    answer := 0
    for i := range b {
        s := b[i]
        ln := len(stack)
        if ln > 0 && stack[ln-1] == '(' && s == ')' {
            stack = stack[:ln-1]
            continue
        }
        stack = append(stack, s)
    }
    
    if len(stack) == 0 {
        answer = 1
    } 
        
    return answer
}