#Maybe the flag was the friends we made along the way
password = "richardmc06 richardlee richardko richardishot richardgutierrez richardceniza richardb1 richard98 richard91 richard81 richard789 richard75 richard74 married joaquin azerty africa tootie kingdom female Desmond corvette stefania sugarbear sugarbaby shopping1 shearer scoobydoo1 sarah123 princess07 nuggets millos marivic loser123 lobito joe123 jenna1 jeannie iloverob genesis1 chrissy1 chick butters amparo alejita 25802580 2222222222 white poop123 pimp pekpek nikko mimama mahalqoh lovejesus lauris kitty2 kaitlyn1 jordan2 Ileana Gucci fingers dodgers1 colin cavalo catlover bracken blaze1 bahamas arellano almeida aiden1 858585 wildthing teacher1 taetae shitty reeree qazqaz princess15 ricardo babygurl heaven 55555 baseball martin greenday november alyssa madison mother 123321 123abc mahalkita batman victor horses tiffany mariana Eduardo andres courtney booboo kissme harley ronaldo iloveyou1 precious october inuyasha peaches veronica chris 888888 adriana cutie james banana prince friend jesus1 crystal celtic zxcvbnm edward oliver diana samsung freedom angelo kenneth master scooby carmen 456789 sebastian rebecca jackie spiderman Christopher karina johnny Hotmail 0123456789 school barcelona august orlando samuel cameron slipknot cutiepie monkey1 50cent bonita kevin maganda babyboy casper brenda adidas kitten karen mustang isabel natalie cuteako javier 789456123 123654 sarah bowwow portugal laura 777777 marvin denise tigers volleyball jasper rockstar january fuckoff alicia Nicholas flowers cristian tintin bianca chrisbrown chester 101010 smokey silver internet sweet strawberry Garfield dennis panget"

# Hidden mining coordinates (flag)
flag = "D1ggy_d1ggy_h0l3"

def find_positions(flag, crew_list):
    positions = []
    for char in flag:
        if char == "_":
            positions.append("_")  # Keep separators as-is
            continue
        found = False
        for i, name in enumerate(crew_list):
            if char.lower() in name.lower():
                positions.append([i, name.lower().index(char.lower())])
                found = True
                break
        if not found:
            positions.append([None, None])
    return positions

# Retrieve flag positions
positions = find_positions(flag, password.split())

# Create the mining report
output_text = "Mining report - flag coordinates: ectf{" + str(positions) + "}"

# Write the report to the file
with open("mining_report.txt", "w") as file:
    file.write(output_text)

# Display the result for verification
print("Rock and Stone! Report written to mining_report.txt:", output_text)
