class Solution2:
     def __init__(self,value):
        self.stringT = value
     def stringValue(self):
        return self.stringT
     def calculate_f(self,substring,subStringList):
        return len(substring)*self.count_occu(subStringList,substring)
     def calculate_max_value(self):
        max_value=0
        subStringList=self.get_substrings()
        for substring in subStringList:
                current_value=self.calculate_f(substring,subStringList)
                max_value=max(current_value,max_value)
        return max_value
        
     def get_substrings(self):
        s=self.stringT
        substrings = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                substrings.append(substring)

        return substrings
     def count_occu(self,substrArr,stringValue):
         count=0
         for item in substrArr:
            if item==stringValue:
                count+=1
         return count       

        


        