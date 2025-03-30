def sentencePalindrome(s):
  
    s1 = []
    for ch in s:
        if ch.isalnum():
            s1.append(ch.lower())
	
    s1 = ''.join(s1)
   
    rev = s1[::-1]
   
    return s1 == rev

if __name__ == "__main__":
    s = "Too hot to hoot."
    print("True" if sentencePalindrome(s) else "False")