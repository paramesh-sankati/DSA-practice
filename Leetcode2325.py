'''You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

Example 1:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.'''
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
dici={}
v=97
for i in key:
    if i!=" " and i not in dici:
        dici[i]=chr(v)
        v+=1
s=""
for i in message:
    if i==" ":
        s=s+" "
    else:
        s=s+dici[i]
print(s)
