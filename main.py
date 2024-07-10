import subprocess
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

ascii_art = """
   *           (   (      (        ) (      (               )     ) 
 (  `    (     )\ ))\ )   )\ )  ( /( )\ )   )\ )      (  ( /(  ( /( 
 )\))(   )\   (()/(()/(  (()/(  )\()|()/(  (()/((     )\ )\()) )\())
((_)()((((_)(  /(_))(_))  /(_))((_)\ /(_))  /(_))\  (((_|(_)\ ((_)\ 
(_()((_)\ _ )\(_))(_))   (_))_  _((_|_))   (_))((_) )\___ ((_) _((_ )
|  \/  (_)_\(_) __/ __|   |   \| \| / __|  | _ \ __((/ __/ _ \| \| |
| |\/| |/ _ \ \__ \__ \   | |) | .` \__ \  |   / _| | (_| (_) | .` |
|_|  |_/_/ \_\|___/___/   |___/|_|\_|___/  |_|_\___| \___\___/|_|\_|
v.1.0 | by hashtagtodo | https://github.com/hashtagtodo
"""

print(Fore.RED + ascii_art)

target = input("Enter the domain to scan (without the .com or any other extension): ")

tlds = [
    ".com",
    ".net",
    ".org",
    ".info",
    ".biz",
    ".co",
    ".us",
    ".uk",
    ".ca",
    ".au",
    ".de",
    ".fr",
    ".it",
    ".es",
    ".nl",
    ".se",
    ".no",
    ".dk",
    ".fi",
    ".ru",
    ".jp",
    ".cn",
    ".in",
    ".br",
    ".za",
    ".mx",
    ".com.mx",
    ".tv",
    ".me",
    ".io",
    ".tech",
    ".xyz",
    ".app",
    ".dev",
    ".shop",
    ".site",
    ".online",
    ".website",
    ".store",
    ".space",
    ".cloud",
    ".blog",
    ".news",
    ".media",
    ".agency",
    ".solutions",
    ".systems",
    ".design",
    ".digital",
    ".global",
    ".asia",
    ".cat",
    ".jobs",
    ".mobi",
    ".museum",
    ".name",
    ".pro",
    ".tel",
    ".travel",
    ".int",
    ".gov",
    ".edu",
    ".mil",
    ".arpa",
    ".aero",
    ".coop",
    ".museum",
    ".post",
    ".ac",
    ".ad",
    ".ae",
    ".af",
    ".ag",
    ".ai",
    ".al",
    ".am",
    ".ao",
    ".aq",
    ".ar",
    ".as",
    ".at",
    ".aw",
    ".ax",
    ".az",
    ".ba",
    ".bb",
    ".bd",
    ".be",
    ".bf",
    ".bg",
    ".bh",
    ".bi",
    ".bj",
    ".bm",
    ".bn",
    ".bo",
    ".bq",
    ".bs",
    ".bt",
    ".bv",
    ".bw",
    ".by",
    ".bz",
    ".cc",
    ".cd",
    ".cf",
    ".cg",
    ".ch",
    ".ci",
    ".ck",
    ".cl",
    ".cm",
    ".cn",
    ".co",
    ".cr",
    ".cu",
    ".cv",
    ".cw",
    ".cx",
    ".cy",
    ".cz",
    ".dj",
    ".dm",
    ".do",
    ".dz",
    ".ec",
    ".ee",
    ".eg",
    ".eh",
    ".er",
    ".et",
    ".eu",
    ".fi",
    ".fj",
    ".fk",
    ".fm",
    ".fo",
    ".ga",
    ".gd",
    ".ge",
    ".gf",
    ".gg",
    ".gh",
    ".gi",
    ".gl",
    ".gm",
    ".gn",
    ".gp",
    ".gq",
    ".gr",
    ".gt",
    ".gu",
    ".gw",
    ".gy",
    ".hk",
    ".hm",
    ".hn",
    ".hr",
    ".ht",
    ".hu",
    ".id",
    ".ie",
    ".il",
    ".im",
    ".io",
    ".iq",
    ".ir",
    ".is",
    ".je",
    ".jm",
    ".jo",
    ".ke",
    ".kg",
    ".kh",
    ".ki",
    ".km",
    ".kn",
    ".kp",
    ".kr",
    ".kw",
    ".ky",
    ".kz",
    ".la",
    ".lb",
    ".lc",
    ".li",
    ".lk",
    ".lr",
    ".ls",
    ".lt",
    ".lu",
    ".lv",
    ".ly",
    ".ma",
    ".mc",
    ".md",
    ".mg",
    ".mh",
    ".mk",
    ".ml",
    ".mm",
    ".mn",
    ".mo",
    ".mp",
    ".mq",
    ".mr",
    ".ms",
    ".mt",
    ".mu",
    ".mv",
    ".mw",
    ".my",
    ".mz",
    ".na",
    ".nc",
    ".ne",
    ".nf",
    ".ng",
    ".ni",
    ".np",
    ".nr",
    ".nu",
    ".nz",
    ".om",
    ".pa",
    ".pe",
    ".pf",
    ".pg",
    ".ph",
    ".pk",
    ".pl",
    ".pm",
    ".pn",
    ".pr",
    ".ps",
    ".pt",
    ".pw",
    ".py",
    ".qa",
    ".re",
    ".ro",
    ".rs",
    ".rw",
    ".sa",
    ".sb",
    ".sc",
    ".sd",
    ".sg",
    ".sh",
    ".si",
    ".sk",
    ".sl",
    ".sm",
    ".sn",
    ".so",
    ".sr",
    ".ss",
    ".st",
    ".sv",
    ".sx",
    ".sy",
    ".sz",
    ".tc",
    ".td",
    ".tf",
    ".tg",
    ".th",
    ".tj",
    ".tk",
    ".tl",
    ".tm",
    ".tn",
    ".to",
    ".tr",
    ".tt",
    ".tv",
    ".tz",
    ".ua",
    ".ug",
    ".uy",
    ".uz",
    ".va",
    ".vc",
    ".ve",
    ".vg",
    ".vi",
    ".vn",
    ".vu",
    ".wf",
    ".ws",
    ".ye",
    ".yt",
    ".zm",
    ".zw",
]


date_output = datetime.now().strftime("%d%m%Y")
output_filename = f"{date_output}_{target}.txt"


with open(output_filename, "w") as output_file:
    for tld in tlds:
        domain = target + tld
        now = datetime.now().strftime("%I:%M:%S %p")

        print(
            Fore.GREEN
            + f"[+]====================================================================================[{now}]•x"
        )
        print(f"DNS RECON at: {domain}")
        print(
            Fore.GREEN
            + f"[+]====================================================================================[{now}]•x"
        )
        result = subprocess.run(
            f"dnsrecon -d {domain}", shell=True, capture_output=True, text=True
        )
        print(result.stdout)
        output_file.write(
            f"[+]====================================================================================[{now}]•x\n"
        )
        output_file.write(f"DNS RECON at: {domain}\n{result.stdout}\n")
        output_file.write(
            f"[+]====================================================================================[{now}]•x\n"
        )
        if "Could not resolve domain" in result.stdout:
            print(Fore.RED + f"[-] Could not resolve domain: {domain}")
            continue

        print(
            Fore.YELLOW
            + f"[+]====================================================================================[{now}]•x"
        )
        print(f"WHOIS: {domain}")
        print(
            Fore.YELLOW
            + f"[+]====================================================================================[{now}]•x"
        )
        result = subprocess.run(
            f"whois {domain}", shell=True, capture_output=True, text=True
        )
        print(result.stdout)
        output_file.write(
            f"[+]====================================================================================[{now}]•x\n"
        )
        output_file.write(f"WHOIS: {domain}\n{result.stdout}\n")
        output_file.write(
            f"[+]====================================================================================[{now}]•x\n"
        )
        print(
            Fore.BLUE
            + f"[+]====================================================================================[{now}]•x"
        )
        print(f"DNS ENUM at: {domain}")
        print(
            Fore.BLUE
            + f"[+]====================================================================================[{now}]•x"
        )
        result = subprocess.run(
            f"dnsenum {domain}", shell=True, capture_output=True, text=True
        )
        print(result.stdout)
        output_file.write(
            f"[+]====================================================================================[{now}]•x\n"
        )
        output_file.write(f"DNS ENUM at: {domain}\n{result.stdout}\n")
        output_file.write(
            f"[+]====================================================================================[{now}]•x\n"
        )
