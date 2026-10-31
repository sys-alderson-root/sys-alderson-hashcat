import hashlib
import os
import sys
import time

BANNER = """
    ___________                 __  _          
   / ____/ ___/ /___  ____  _____/ /_(_)__  __  
  / /_   \__ \/ / __ \/ __ \/ ___/ __/ / _ \/ /  
 / __/  ___/ / / /_/ / / / / /__/ /_/ /  __/ /   
/_/    /____/_/\____/_/ /_/\___/\__/_/\___/_/    
                                                 
 [ sys-alderson-hashcat - REAL CRACKER ]
===================================================
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def crack_hash(target_hash, wordlist_path, algo):
    print(f"\n[*] Cible : {target_hash}")
    print(f"[*] Algorithme : {algo.upper()}")
    print(f"[*] Wordlist : {wordlist_path}")
    print("[*] Attaque en cours... (Ctrl+C pour arrêter)\n")
    
    try:
        with open(wordlist_path, "r", encoding="latin-1", errors="ignore") as file:
            count = 0
            for line in file:
                mdp = line.strip()
                if not mdp:
                    continue
                
                count += 1
                if count % 100000 == 0:
                    print(f"[*] {count} mots testés...", end="\r")
                
                # Hachage du mot testé
                if algo == "md5":
                    hashed = hashlib.md5(mdp.encode('utf-8', errors='ignore')).hexdigest()
                elif algo == "sha1":
                    hashed = hashlib.sha1(mdp.encode('utf-8', errors='ignore')).hexdigest()
                elif algo == "sha256":
                    hashed = hashlib.sha256(mdp.encode('utf-8', errors='ignore')).hexdigest()
                else:
                    print("[-] Algorithme non supporté.")
                    return

                if hashed == target_hash.lower():
                    print(f"\n\n[+] MATCH TROUVÉ ! Le mot de passe est : '{mdp}'")
                    print(f"[+] Trouvé après {count} tentatives.")
                    return
                    
        print(f"\n\n[-] ÉCHEC : Mot de passe introuvable dans les {count} mots de la liste.")
        
    except FileNotFoundError:
        print(f"\n[-] ERREUR : Le fichier '{wordlist_path}' est introuvable.")

def main():
    while True:
        clear()
        print(BANNER)
        target = input("[?] Entrez le hash à casser : ").strip()
        algo = input("[?] Algorithme (md5 / sha1 / sha256) : ").strip().lower()
        wordlist = input("[?] Chemin de la wordlist (ex: rockyou.txt) : ").strip()
        
        if target and algo and wordlist:
            start = time.time()
            crack_hash(target, wordlist, algo)
            print(f"[*] Temps écoulé : {time.time() - start:.2f} secondes")
            
        choix = input("\n[?] Recommencer ? (o/n) : ").lower()
        if choix != 'o':
            print("\n[i] Fermeture de sys-alderson-hashcat. Au revoir.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[-] Interrompu par l'utilisateur.")
        sys.exit()
