"""
A string S consisting of N characters is considered to be properly nested 
if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

int solution(char *S);
that, given a string S consisting of N characters, returns 1 if S is 
properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given 
S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" 
and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage 
required for input arguments).
"""
def solution(S):
    openers = "{[("
    closers = "}])"
    sets = zip(openers, closers)
    ln = len(S)
    if S == "":
        return 1
    
    if S[0] in closers:
        return 0
        
    validated = []
    last_opener = []
    total_opens = 0
    total_closes = 0
    for i in xrange(ln):
        c = S[i]
        if len(validated) == 0 or c in openers:
            validated.append(c)
            last_opener.append(c)
            total_opens += 1
            
        if c in closers:
            p = validated[-1:][0]
            o = [s for s in sets if s[1] == c][0][0]
            closed = False
            if len(last_opener) == 0:
                return 0
            
            if p in closers and o != last_opener[-1:][0]:
                return 0
            else:
                closed = True
                
            if p not in closers and o != p:
                return 0
            else:
                closed = True
            
            if closed:
                validated.append(c)
                last_opener.pop()
                total_closes += 1
    
    if total_closes == total_opens:
        return 1
    else:
        return 0
