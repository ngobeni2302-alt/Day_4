n = "What will you do ?"
t = "Rebuild it"
s = "Just the way it was, brick for brick"
a = "Why do we fall sir?"
k = "So that we can learn to pick ourselves up"
o = "You still haven't given up on me"
p = "Never!"
print(n)

# Read inputs until the final marker `p` is entered.
# Print each input only once (ignore duplicates).
stop_marker = p
seen = set()

try:
    while True:
        user = input()
        if user in seen:
            continue
        seen.add(user)
        if user == stop_marker:
            break
except EOFError:
    pass

