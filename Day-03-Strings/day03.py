first_name = "Faisal"
last_name = "Mustafa"
company = "Simplelogix"
role = "CEO"
city = "Lahore"

print(f"Full Name: {first_name} {last_name}")
print(f"Role: {role} at {company}")
print(f"Location: {city}, Pakistan")
print(f"Name Length: {len(first_name) + len(last_name)}")
print(f"Company Uppercase: {company.upper()}")
print(f"First Character of Company: {company[0]}")
print(f"Company with Replaced: {company.upper().replace('SIMPLELOGIX', 'SIMPLELOGIX AI')}")
