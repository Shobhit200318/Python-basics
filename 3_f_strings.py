letter = "Hey my name is {1} and I from {0}"
country = "India"
name = "Harry"

print(letter.format(country,name))

# f-string method
print(f"Hey my name is {name} and I from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollars! "
print(txt)
print(f"{2 * 30}")
print(type(f"{2*30}"))