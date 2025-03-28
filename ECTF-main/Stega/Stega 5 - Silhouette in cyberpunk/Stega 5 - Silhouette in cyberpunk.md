# Stega 5 - Silhouette in cyberpunk

A coded message has been hidden in this picture. Your mission, if you accept it, is to find this message.  
Flag format: ectf{the_message}

### File:
Stega_5_-_Silhouette_in_cyberpunk.png

\Author - Antoine

#### Points :
`200`

## Solution
You get this image :  

<img width="500" alt="image" src="https://github.com/LupusArctos4/ECTF/blob/main/Stega/Stega%205%20-%20Silhouette%20in%20cyberpunk/Stega_5_-_Silhouette_in_cyberpunk.png?raw=true" />


The flag is hidden directly within the image, unlike other challenges where the flag is hidden in metadata or bits. Upon close inspection, you can notice dots on the buildings. These dots are Braille.  

Tool used : https://www.dcode.fr/alphabet-braille

### First building in the foreground
The first building in the foreground contains a decoy Braille message: "this is just a dummy, nice try."  

<img width="150" alt="image" src="https://github.com/LupusArctos4/ECTF/blob/main/Stega/Stega%205%20-%20Silhouette%20in%20cyberpunk/first_building.png?raw=true" />  
   
<img width="500" alt="image" src="https://github.com/LupusArctos4/ECTF/blob/main/Stega/Stega%205%20-%20Silhouette%20in%20cyberpunk/first_translation.png?raw=true" />  

### Second building in the background on the far left
The real flag is hidden in the building in the background on the far left. After decoding the Braille from this building, you get:  
h1dd3n_1n_th3_d4rkn3ss with underscores for spaces.  

<img width="150" alt="image" src="https://github.com/LupusArctos4/ECTF/blob/main/Stega/Stega%205%20-%20Silhouette%20in%20cyberpunk/second_building.png?raw=true" /> 
  
<img width="500" alt="image" src="https://github.com/LupusArctos4/ECTF/blob/main/Stega/Stega%205%20-%20Silhouette%20in%20cyberpunk/second_translation.png?raw=true"/>  

### Flag
To validate the flag, it had to be written in lowercase as ectf{h1dd3n_1n_th3_d4rkn3ss}. While the underscores are not very visible in the image, the challenge specifically instructed participants to separate the words with underscores. If there was any confusion, the challenge also mentioned submitting a ticket for clarification.

`ectf{h1dd3n_1n_th3_d4rkn3ss}`
