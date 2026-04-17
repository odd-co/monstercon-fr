# monstercon-fr
Un patch non officiel français pour Monster Prom 4 - Monster con! (En dev.)

Riripo je suis dans ton placard.

"Oublie d'avoir tuer la chaussette avant de vendre sa peau à l'ours"

---

# Progression
**Pour l'instant...**
- Les scripts pythons la dedans marchent sûrement que sur mon mac
- C'est chiant à installer
- C'est pas compilé
- C'EST PAS FINIIIII RAGHHH LES 27 000 LIGNES
- Trouver quelqu'un pour aider svp...
- C'est probablement bourré de fautes...

# Projet frère :33
Un outil créé pour le projet et utilisé durant le développement du patc, qui est techniquement une version boosté au stéroides du fichier make.py du projet.

[https://github.com/LinkfandosVF/PromTool]


**Cependant! Voici la progression;**
- ♢ metatexts.bytes - Ligne 631 sur Ligne 2501 (Interface, UI, Trucs utilisés partout) orthographe à vérifier, je devais être bourré.
- ☑ events_prologue - (Intro, Tuto??)
- ☑ prologue_conpopquiz
- ☑ prologue_likes
- ⌑ events_maingame - 21,3 sur 24743 (Désolée, j'ai commencé au milieu - Tkt lol fait comme tu veux)
- ⌑ events_endings - Ligne 242 sur 2079
    - success 100%
    - finalsuccess à faire
    - failure à faire
    - secretending à faire
        - secretending success à faire
        - secretending fail à faire
- ⌑ events_maingame - 1 sur 700 et des boulettes events 
- ⌑ events_endings - à faire! 
- ⌑ events_comic - Ligne 119 sur 1162 (comic_intro terminé, il reste le reste...)
- ⌑ events_challenge - Ligne 89 sur 207, Challenge 23 (yay! j'suis à la moitié! plus sur la branche test. la branche test est mort. rest in rip.)
- ⌑ D'autres...????... J'ai la flemme de tout écrire ici.

**Ce que j'ai à faire pour plus tard...**
- Faire un meilleur Readme
- Wiki avec des instructions pour installer le patch
- Release avec le patch Copy-Pasteable
- De la pub! (Sinon personne ne sais que ça existe... Et c'est un peu triste...)
- Faire une seule branche aaazjrhlsdjqfhlsd

# Installation
**Et le dossier?**
En gros, il suffit de prendre le text_assets_all.bundle dans les releases, et de le mettre dans le bon dossier... et de **bien choisir de remplacer.**

Windows: Dossierdujeu/StreamingAssets/aa/StandaloneWindows64/

MacOS: Dossierdujeu.app/Contents/Resources/Data/StreamingAssets/aa/StandaloneOSX/

Unix/GNU+Linux: Je sais pas encore, mais surement le même chemin avec Standalonequelquechose

NOTE: Sur mac, pour accéder au dossier du jeu, faites Clic Droit sur l'application et "Afficher le contenu du paquet". Vous DEVEZ aussi utiliser Rosetta pour lancer le jeu sur les plateformes Silicon M1/M2/M3/M4, sans quoi un message d'erreur s'afficheras... (CMD + I > Ouvrir avec Rosetta), ça vaut en général aussi pour Steam(???).


# Building
Il vous faut python3 et le module pip UnityPy. C'est tout.
Téléchargez le repo, et tapez "python3 make.py", et voilà! Elle est pas belle la vie?


Le fichier prends ce qu'il y à dans le dossier french et les renommes avant de les compiler. Le dossier english sert de référence.


En gros...

Sur MacOS. (Needs brew.sh)
```
cd monstercon-fr/
brew install python3
python3 -m pip install UnityPy
python3 build.py
```

Sur Debian/Ubuntu (Ou autre distro basée sur Debian avec apt)
```
cd monstercon-fr/
sudo apt install python3
python3 -m pip install UnityPy  --break-system-packages
python3 build.py
```

Sur Arch (Ou autre distro basée sur Arch avec pacman)
```
cd monstercon-fr/
sudo pacman -S python3
python3 -m pip install UnityPy  --break-system-packages
python3 build.py
```

La sortie de build devrais être texts_assets_all.bundle.
---

Vous voulez me supporter? Allez faire un tour sur mon Ko-Fi... ou pas. Comme vous voulez.


Ko-Fi - [https://ko-fi.com/linkfandos](https://ko-fi.com/linkfandos)

Discord - [https://discord.gg/Vuspk9cAcS](https://discord.gg/Vuspk9cAcS)


Je fais tout mes projets, souvent seul (pas cette fois), sans IA (ewww cé nul l'ia générativeeeee), sur du matériel bas de gamme... Donc merci de vous amuser! :3
