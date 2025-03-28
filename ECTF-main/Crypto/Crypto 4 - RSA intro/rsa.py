from Crypto.Util.number import *

# Given values
n = 1184757578872726401875541948122658312538049254193811194706693679652903378440466755792536161053191231432973156335040510349121778456628168943028766026325269453310699198719079556693102485413885649073042144349442001704335216057511775363148519784811675479570531670763418634378774880394019792620389776531074083392140830437849497447329664549296428813777546855940919082901504207170768426813757805483319503728328687467699567371168782338826298888423104758901089557046371665629255777197328691825066749074347103563098441361558833400318385188377678083115037778182654607468940072820501076215527837271902427707151244226579090790964814802124666768804586924537209470827885832840263287617652116022064863681106011820233657970964986092799261540575771674176693421056457946384672759579487892764356140012868139174882562700663398653410810939857286089056807943991134484292518274473171647231470366805379774254724269612848224383658855657086251162811678080812135302264683778545807214278668333366983221748107612374568726991332801566415332661851729896598399859186545014999769601615937310266497300349207439222706313193098254004197684614395013043216709335205659801602035088735521560206321305834999363607988482888525092210585343868702766655032190348593070756595867719633492847013620378010952424253098519859359544101947494405255181048550165119679168071637363387551385352023888031983210940358096667928019837327581681936262186049576626435407253113152851511562799379477905913074052917135254673527350886619693800827592241738185465519368503599267554966329609741719839452532720121891782656000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001

e = 65537  

# Define the flag as bytes (explicitly using b'')
flag = b"ectf{b4sic_F4cT0rDb_rS4}"

# Convert the flag to a number (long)
m = bytes_to_long(flag)

# Encrypt the message using RSA: c = m^e % n
c = pow(m, e, n)

# Open a file and write the values of n, e, and c
with open("output.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
f.close()
