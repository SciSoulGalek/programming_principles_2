"""
A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces.
Create a function to convert grams to ounces.
ounces = 28.3495231 * grams
"""
def gramsToOunce(grams):
    return grams / 28.3495231
def ouncesToGrams(ounces):
    return ounces * 28.3495231

print("To convert from grams to ounces, input command 1 and click enter")
print("To convert from ounces to gram, input command 2 and click enter")

x = int(input())

if x != 1 and x != 2:
 print("Wrong command, use command 1 or 2 and nothing else!")
 exit()
elif x == 1:
 y = float(input("Grams to ounces:"))
 print(f"{y} grams = {gramsToOunce(y)} ounces") 
elif x == 2:
 y = float(input("Ounces to grams: "))
 print(f"{y} ounces = {ouncesToGrams(y)} grams")
 