#!/bin/bash

# Password string
passwords="richardmc06 richardlee richardko richardishot richardgutierrez richardceniza richardb1 richard98 richard91 richard81 richard789 richard75 richard74 married joaquin azerty africa tootie kingdom female Desmond corvette stefania sugarbear sugarbaby shopping1 shearer scoobydoo1 sarah123 princess07 nuggets millos marivic loser123 lobito joe123 jenna1 jeannie iloverob genesis1 chrissy1 chick butters amparo alejita 25802580 2222222222 white poop123 pimp pekpek nikko mimama mahalqoh lovejesus lauris kitty2 kaitlyn1 jordan2 Ileana Gucci fingers dodgers1 colin cavalo catlover bracken blaze1 bahamas arellano almeida aiden1 858585 wildthing teacher1 taetae shitty reeree qazqaz princess15 ricardo babygurl heaven 55555 baseball martin greenday november alyssa madison mother 123321 123abc mahalkita batman victor horses tiffany mariana Eduardo andres courtney booboo kissme harley ronaldo iloveyou1 precious october inuyasha peaches veronica chris 888888 adriana cutie james banana prince friend jesus1 crystal celtic zxcvbnm edward oliver diana samsung freedom angelo kenneth master scooby carmen 456789 sebastian rebecca jackie spiderman Christopher karina johnny Hotmail 0123456789 school barcelona august orlando samuel cameron slipknot cutiepie monkey1 50cent bonita kevin maganda babyboy casper brenda adidas kitten karen mustang isabel natalie cuteako javier 789456123 123654 sarah bowwow portugal laura 777777 marvin denise tigers volleyball jasper rockstar january fuckoff alicia Nicholas flowers cristian tintin bianca chrisbrown chester 101010 smokey silver internet sweet strawberry Garfield dennis panget"

# Convert the password string into an array
password_array=($(echo "$passwords"))

# Variable for the current ZIP file
current_zip=""
final_file="mining_report.txt"  # The mining report file included in the first ZIP

# Counter for naming ZIP files
counter=1

# Create nested ZIP files
for password in "${password_array[@]}"; do
    next_zip="dwarf_vault_${counter}.zip" # Name of the next ZIP file with a "dwarf vault" theme
    
    if [ -n "$current_zip" ]; then
        # If a previous ZIP exists, include it in the next one
        zip --password "$password" "$next_zip" "$current_zip" >/dev/null
        rm "$current_zip" # Delete the old ZIP file
    else
        # If it's the first ZIP, include the mining report file
        zip --password "$password" "$next_zip" "$final_file" >/dev/null
        rm "$final_file" # Delete the mining report file
    fi

    # Update the current ZIP file
    current_zip="$next_zip"
    counter=$((counter + 1))
done

echo "Nested dwarf vaults successfully created. The outermost vault is: $current_zip"
