from bisect import bisect_left, bisect_right
class SuffixArray:
    def __init__(self, text:str):
        self.text=text
        self.sa=sorted(range(len(text)), key=lambda k:text[k:])
    def find(self, pat:str):
        l,r=0,len(self.sa)
        while l<r:
            m=(l+r)//2
            if self.text[self.sa[m]:].startswith(pat):
                r=m
            elif self.text[self.sa[m]:]<pat:
                l=m+1
            else:
                r=m
        start=l
        l,r=0,len(self.sa)
        while l<r:
            m=(l+r)//2
            if self.text[self.sa[m]:].startswith(pat):
                l=m+1
            elif self.text[self.sa[m]:]<pat:
                l=m+1
            else:
                r=m
        end=l
        return sorted(self.sa[start:end])
