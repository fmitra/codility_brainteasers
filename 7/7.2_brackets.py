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
    if not S:
        return 1

    # It can never be properly nested with an odd number of elements
    ln = len(S)
    if ln % 2 != 0:
        return 0

    open_close_map = {
        '{': '}',
        '[': ']',
        '(': ')',
    }

    # A closer should always match that most recent opener in the list,
    # given the mapping above. If it does not match, it's not nested.
    openers = []
    for v in S:
        is_opener = v in open_close_map
        is_closer = not is_opener

        if is_opener:
            openers.append(v)
            continue

        if is_closer and not openers:
            return 0

        last_opener = openers.pop()
        closer = open_close_map[last_opener]
        if v != closer:
            return 0

    # There are openers leftover that have not been closed
    if openers:
        return 0

    return 1
