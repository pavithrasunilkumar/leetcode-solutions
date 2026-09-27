s = input("Enter the sentence: ")

clean = ""

for char in s:
    if char.isalnum():
        clean += char.lower()

left = 0
right = len(clean) - 1

while left < right:
    if clean[left] != clean[right]:
        print("Not a palindrome")
        break

    left += 1
    right -= 1

else:
    print("Palindrome")