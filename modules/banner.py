from colorama import Fore,Back,Style
import platform,os

OsName = platform.uname()[0]

def banner():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(Fore.LIGHTWHITE_EX + r"  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗██╗    ██╗██╗██████╗ ███████╗")
    print(Fore.LIGHTWHITE_EX + r" ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██║    ██║██║██╔══██╗██╔════╝")
    print(Fore.LIGHTWHITE_EX + r" ██║  ███╗███████║██║   ██║███████╗   ██║   ██║ █╗ ██║██║██████╔╝█████╗  ")
    print(Fore.CYAN          + r" ██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██║███╗██║██║██╔══██╗██╔══╝  ")
    print(Fore.CYAN          + r" ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ╚███╔███╔╝██║██║  ██║███████╗")
    print(Fore.CYAN          + r"  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝")

    print(Fore.LIGHTGREEN_EX + r"")
    print(r"                  ███████╗██████╗ ██╗   ██╗")
    print(r"                  ██╔════╝██╔══██╗╚██╗ ██╔╝")
    print(r"                  ███████╗██████╔╝ ╚████╔╝ ")
    print(r"                  ╚════██║██╔══██╗  ╚██╔╝  ")
    print(r"                  ███████║██║  ██║   ██║   ")
    print(r"                  ╚══════╝╚═╝  ╚═╝   ╚═╝   ")

    print(Fore.LIGHTBLACK_EX + "════════════════════════════════════════════════════════════════════════════")
    print(Fore.LIGHTCYAN_EX   + "                     👻 GHOSTWIRE-SRY v1.0.0")
    print(Fore.LIGHTWHITE_EX  + "               Advanced Cybersecurity Research Toolkit")
    print(Fore.LIGHTGREEN_EX  + "               ► SEE EVERYTHING • LEAVE NOTHING ◄")
    print(Fore.YELLOW          + "────────────────────────────────────────────────────────────────────────────")
    print(Fore.LIGHTYELLOW_EX + "                         ◆ DEVELOPED BY ◆")
    print(Fore.LIGHTMAGENTA_EX + "                  OFFICIAL_cyber_satyam27")
    print(Fore.LIGHTCYAN_EX   + "          GitHub  : github.com/OFFICIALcybersatyam27")
    print(Fore.LIGHTRED_EX    + "          YouTube : @official_cyber_satyam27")
    print(Fore.YELLOW          + "────────────────────────────────────────────────────────────────────────────")
    print(Fore.LIGHTBLACK_EX + "════════════════════════════════════════════════════════════════════════════")
    print(Style.RESET_ALL)

banner()