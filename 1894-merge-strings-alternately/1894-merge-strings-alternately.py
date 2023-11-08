class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = []
        pointer1 = 0

        if len(word1) < len(word2):
            while pointer1 < len(word1):
                output.append(word1[pointer1]);
                output.append(word2[pointer1]);
                pointer1 = pointer1 + 1;
            output.append(word2[pointer1:]);
            return "".join(output);

        elif len(word2) < len(word1):
            while pointer1 < len(word2):
                output.append(word1[pointer1]);
                output.append(word2[pointer1]);
                pointer1 = pointer1 + 1;
            output.append(word1[pointer1:]);
            return "".join(output);


        else:
            while pointer1 < len(word1):
                output.append(word1[pointer1]);
                output.append(word2[pointer1]);
                pointer1 = pointer1 + 1;
            return "".join(output);

        