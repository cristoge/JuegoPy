from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# Arte ASCII con colores

menu_db = f"""
{Fore.CYAN}
··························································································
: _   __  __         _       _     _                   _                                 :
:/ | |  \/  |___  __| |___  / |   (_)_  _ __ _ __ _ __| |___ _ _                         :
:| |_| |\/| / _ \/ _` / _ \ | |   | | || / _` / _` / _` / _ \ '_|                        :
:|_(_)_|__|_\___/\__,_\___/ |_|_ _/ |\_,_\__, \__,_\__,_\___/_|         _ _  __ _    _ _ :
:|_  ) |  \/  |___  __| |___  / |__/(_)_ |___/ _ __ _ __| |___ _ _   __| (_)/ _(_)__(_) |:
: / / _| |\/| / _ \/ _` / _ \ | |   | | || / _` / _` / _` / _ \ '_| / _` | |  _| / _| | |:
:/___(_)_|  |_\___/\__,_\___/ |_|_ _/ |\_,_\__, \__,_\__,_\___/_|   \__,_|_|_| |_\__|_|_|:
:|__ / |  \/  |___  __| |___  |_  )__/(_)_ |___/ _ __ _ __| |___ _ _ ___ ___             :
: |_ \_| |\/| / _ \/ _` / _ \  / /    | | || / _` / _` / _` / _ \ '_/ -_|_-<             :
:|___(_)_|_ |_\___/\__,_\___/ /___|  _/ |\_,_\__, \__,_\__,_\___/_| \___/__/             :
:| | | / __| __ _| (_)_ _           |__/     |___/                                       :
:|_  _|\__ \/ _` | | | '_|                                                               :
:  |_(_)___/\__,_|_|_|_|                                                                 :
··························································································
{Style.RESET_ALL}
"""


escogerdb = f"""
{Fore.CYAN} ___                         ___           _          
| __|___ __ ___  __ _ ___   / _ \\ _ __  __(_)___ _ _  
| _|(_-</ _/ _ \\/ _` / -_) | (_) | '_ \\/ _| / _ \\ ' \\ 
|___/__\\/__\\___/\\__, \\___|  \\___/| .__\\/__|_\\___/_||_|
                |___/            |_|                  
{Style.RESET_ALL}
"""


adivina_numero = rf"""
{Fore.CYAN}   _      _ _     _                 _                                        _             _          _  __   __    _ 
{Fore.CYAN}  /_\  __| (_)_ _(_)_ _  __ _   ___| |  _ _ _  _ _ __  ___ _ _ ___   ___ _ _| |_ _ _ ___  / |  _  _  / |/  \ /  \  (_)
{Fore.CYAN} / _ \/ _` | \ V / | ' \/ _` | / -_) | | ' \ || | '  \/ -_) '_/ _ \ / -_) ' \  _| '_/ -_) | | | || | | | () | () |  _ 
{Fore.CYAN}/_/ \_\__,_|_|\_/|_|_||_\__,_| \___|_| |_||_\_,_|_|_|_\___|_| \___/ \___|_||_\__|_| \___| |_|  \_, | |_|\__/ \__/  (_)
{Fore.CYAN}                                                                                               |__/                   
"""

errordb  = f"""{Fore.RED} 
 _     _               _                                                                              _       
(_)_ _| |_ _ _ ___  __| |_  _ __ ___   _  _ _ _    _ _ _  _ _ __  ___ _ _ ___   __ ___ _ _ _ _ ___ __| |_ ___ 
| | ' \  _| '_/ _ \/ _` | || / _/ -/) | || | ' \  | ' \ || | '  \/ -/) '_/ _ \ / _/ _ \ '_| '_/ -/) _|  _/ _ \ 
|_|_||_\__|_| \___/\__,_|\_,_\__\___|  \_,_|_||_| |_||_\_,_|_|_|_\___|_| \___/ \__\___/_| |_| \___\__|\__\___/ 
"""



ganardb = f"""{Fore.GREEN}
···················································
: _ _  _                                  _     _ :
:(_) || |__ _ ___  __ _ __ _ _ _  __ _ __| |___| |:
:| | __ / _` (_-< / _` / _` | ' \/ _` / _` / _ \_|:
:|_|_||_\__,_/__/ \__, \__,_|_||_\__,_\__,_\___(_):
:                 |___/                           :
···················································
"""

perderdb = f"""{Fore.RED}
··················································
: _ _  _           ___            _ _    _     _ :
:(_) || |__ _ ___ | _ \___ _ _ __| (_)__| |___| |:
:| | __ / _` (_-< |  _/ -_) '_/ _` | / _` / _ \_|:
:|_|_||_\__,_/__/ |_| \___|_| \__,_|_\__,_\___(_):
··················································
"""
es_menordb = f"""{Fore.YELLOW}
········································································
:     _                                                                :
: ___| |  _ _ _  _ _ __  ___ _ _ ___   ___ ___  _ __  ___ _ _  ___ _ _ :
:/ -_) | | ' \ || | '  \/ -_) '_/ _ \ / -_|_-< | '  \/ -_) ' \/ _ \ '_|:
:\___|_| |_||_\_,_|_|_|_\___|_| \___/ \___/__/ |_|_|_\___|_||_\___/_|  :
········································································
"""

es_mayordb = rf"""{Fore.YELLOW}
·········································································
:     _                                                                 :
: ___| |  _ _ _  _ _ __  ___ _ _ ___   ___ ___  _ __  __ _ _  _ ___ _ _ :
:/ -_) | | ' \ || | '  \/ -_) '_/ _ \ / -_|_-< | '  \/ _` | || / _ \ '_|:
:\___|_| |_||_\_,_|_|_|_\___|_| \___/ \___/__/ |_|_|_\__,_|\_, \___/_|  :
:                                                          |__/         :
·········································································
"""

vidas5 = rf"""
{Fore.RED} _____ _                   ___       _    _         
{Fore.RED}|_   _(_)___ _ _  ___ ___ | __| __ _(_)__| |__ _ ___
{Fore.RED}  | | | / -_) ' \/ -_|_-< |__ \ \ V / / _` / _` (_-<
{Fore.RED}  |_| |_\___|_||_\___/__/ |___/  \_/|_\__,_\__,_/__/
"""


jugadores =f"""
{Fore.BLUE}    _                   _           _             _                   _           ___ 
 _ | |_  _ __ _ __ _ __| |___ _ _  / |  _  _   _ | |_  _ __ _ __ _ __| |___ _ _  |_  )
| || | || / _` / _` / _` / _ \ '_| | | | || | | || | || / _` / _` / _` / _ \ '_|  / / 
 \__/ \_,_\__, \__,_\__,_\___/_|   |_|  \_, |  \__/ \_,_\__, \__,_\__,_\___/_|   /___|
          |___/                         |__/            |___/                         
{Style.RESET_ALL}
"""

turno1 = f"""
{Fore.WHITE}············································································
: _____                       _          _                   _           _ :
:|_   _|  _ _ _ _ _  ___   __| |___   _ | |_  _ __ _ __ _ __| |___ _ _  / |:
:  | || || | '_| ' \/ _ \ / _` / -_) | || | || / _` / _` / _` / _ \ '_| | |:
:  |_| \_,_|_| |_||_\___/ \__,_\___|  \__/ \_,_\__, \__,_\__,_\___/_|   |_|:
:                                              |___/                       :
············································································
{Style.RESET_ALL}
"""

turno2 = f"""
{Fore.WHITE}··············································································
: _____                       _          _                   _           ___ :
:|_   _|  _ _ _ _ _  ___   __| |___   _ | |_  _ __ _ __ _ __| |___ _ _  |_  ):
:  | || || | '_| ' \/ _ \ / _` / -_) | || | || / _` / _` / _` / _ \ '_|  / / :
:  |_| \_,_|_| |_||_\___/ \__,_\___|  \__/ \_,_\__, \__,_\__,_\___/_|   /___|:
:                                              |___/                         :
··············································································
{Style.RESET_ALL}
"""


j1correcto = f"""
{Fore.GREEN}·····························································································································
: _  _                   _         _   _                           _           _           _                              _ :
:(_)(_)_  _ __ _ __ _ __| |___ _ _/ | | |_  __ _   __ _ __ ___ _ _| |_ __ _ __| |___   ___| |  _ _ _  _ _ __  ___ _ _ ___| |:
:| || | || / _` / _` / _` / _ \ '_| | | ' \/ _` | / _` / _/ -_) '_|  _/ _` / _` / _ \ / -_) | | ' \ || | '  \/ -_) '_/ _ \_|:
:|_|/ |\_,_\__, \__,_\__,_\___/_| |_| |_||_\__,_| \__,_\__\___|_|  \__\__,_\__,_\___/ \___|_| |_||_\_,_|_|_|_\___|_| \___(_):
: |__/     |___/                                                                                                            :
·····························································································································
{Style.RESET_ALL}
"""

j2correcto = f"""
{Fore.GREEN}······························································································································
: _  _                   _        ___   _                           _           _           _                              _ :
:(_)(_)_  _ __ _ __ _ __| |___ _ |_  ) | |_  __ _   __ _ __ ___ _ _| |_ __ _ __| |___   ___| |  _ _ _  _ _ __  ___ _ _ ___| |:
:| || | || / _` / _` / _` / _ \ '_/ /  | ' \/ _` | / _` / _/ -_) '_|  _/ _` / _` / _ \ / -_) | | ' \ || | '  \/ -_) '_/ _ \_|:
:|_|/ |\_,_\__, \__,_\__,_\___/_|/___| |_||_\__,_| \__,_\__\___|_|  \__\__,_\__,_\___/ \___|_| |_||_\_,_|_|_|_\___|_| \___(_):
: |__/     |___/                                                                                                             :
······························································································································
{Style.RESET_ALL}
"""

j1win = f"""
{Fore.YELLOW}·······························································································································
:    _                   _           _   _                                  _       _   _   _ :
: _ | |_  _ __ _ __ _ __| |___ _ _  / | | |_  __ _   __ _ __ _ _ _  __ _ __| |___  | | | | | |:
:| || | || / _` / _` / _` / _ \ '_| | | | ' \/ _` | / _` / _` | ' \/ _` / _` / _ \ |_| |_| |_|:
: \__/ \_,_\__, \__,_\__,_\___/_|   |_| |_||_\__,_| \__, \__,_|_||_\__,_\__,_\___/ (_) (_) (_):
:          |___/                                    |___/                                     :
·······························································································
{Style.RESET_ALL}
"""

j2win = f"""
{Fore.YELLOW}·································································································································
:    _                   _           ___   _                                  _       _   _   _ :
: _ | |_  _ __ _ __ _ __| |___ _ _  |_  ) | |_  __ _   __ _ __ _ _ _  __ _ __| |___  | | | | | |:
:| || | || / _` / _` / _` / _ \ '_|  / /  | ' \/ _` | / _` / _` | ' \/ _` / _` / _ \ |_| |_| |_|:
: \__/ \_,_\__, \__,_\__,_\___/_|   /___| |_||_\__,_| \__, \__,_|_||_\__,_\__,_\___/ (_) (_) (_):
:          |___/                                      |___/                                     :
·································································································
{Style.RESET_ALL}
"""

agradecimiento = f"""

{Fore.RED}······································································
:  ___             _           ___              _                    :
: / __|_ _ __ _ __(_)__ _ ___ | _ \___ _ _   _ | |_  _ __ _ __ _ _ _ :
:| (_ | '_/ _` / _| / _` (_-< |  _/ _ \ '_| | || | || / _` / _` | '_|:
: \___|_| \__,_\__|_\__,_/__/ |_| \___/_|    \__/ \_,_\__, \__,_|_|  :
:                                                     |___/          :
······································································
{Style.RESET_ALL}
"""