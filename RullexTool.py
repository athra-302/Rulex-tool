# Yusuf's World Tool with Authentication
import os
import colorama
from colorama import Fore, Style
import pyfiglet
import time
import random
import requests
import marshal

colorama.init()

os.system ('clear')

# Constants for authentication
USERNAME = "TGONFIRE"
PASSWORD = "uniquetool"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.YELLOW, Fore.CYAN]
    banner = pyfiglet.figlet_format("MonxTer RuLex", font="slant")
    for color in colors:
        clear_screen()
        print(Colorate.Horizontal(Colors.blue_to_red, """  
        TEAM MONXTER RULEX


   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ 
 ( M | O | N | X | T | E | R )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

                                     
""", 1))
COLOR_DEFAULT = Style.RESET_ALL
COLOR_BLUE = Fore.BLUE
COLOR_MAGENTA = Fore.MAGENTA
COLOR_CYAN = Fore.CYAN
COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
ICON = "➤ "
ARRAY_ANIMATION = [    f"{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}    ",
    f" {COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}   ",
    f"  {COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_YELLOW}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}  ",
    f"   {COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON} ",
    f"    {COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_RED}{ICON}{COLOR_YELLOW}{ICON}{COLOR_MAGENTA}{ICON}"
]
                              
        time.sleep(0.5)

def authenticate():
    print(Fore.YELLOW + "Please log in to access the tool." + Style.RESET_ALL)
    username_input = input(Fore.CYAN + "Username: " + Style. RESET_ALL)
    password_input = input(Fore.CYAN + "Password: " + Style.RESET_ALL)

    if username_input != USERNAME or password_input != PASSWORD:
        print(Fore.RED + "Incorrect username or password." + Style.RESET_ALL)
        print(Fore.YELLOW + "For help, contact us at: facebook.com/Tgrulex" + Style.RESET_ALL)
        exit()

def print_menu():
    print(Fore.GREEN + Style.BRIGHT + "♠️❤️(-ꪑꪖﺃꪀ ꪑꫀꪀꪊ-)❤️♠️" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. " + Fore.CYAN + " ⪨༒𓊈𒆜ƒเℓε εɳ૮σ∂ε૨𒆜𓊉༒⪩" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print(Fore.MAGENTA + "2. " + Fore.BLUE + " ꧁.💕Fαƈҽზσσƙ Mҽʂʂαɠҽ Bσɱზҽɾ💖.꧂" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print(Fore.MAGENTA + "3. " + Fore.GREEN + " ༆༒💞αß⊕u†💞༒༆" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print(Fore.MAGENTA + "4. " + Fore.RED + " ꧁༒︎ᴴ_ᵃ_ᵗ_ᵉ_ʳ_ˢ_ _ᴺ_ᵃ_ᵐ_ᵉ_ _ᴹ_ᵃ_ᵏ_ᵉ_ʳ༒︎꧂" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print(Fore.MAGENTA + "5. " + Fore.LIGHTYELLOW_EX + " 🐙💙  𝔫ᑭ ⓕ𝕚𝐍ｄ𝒆𝓡  🍔☞" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print(Fore.MAGENTA + "6. " + Fore.WHITE + " ꧁༒︎Ĕ_Ж_Ĩ_Ť༒︎꧂" + Style.RESET_ALL)

def file_encoder():
    try:
        from pyfiglet import figlet_format
        from rainbowtext import text
        from colorama import init
    except ImportError:
        os.system('pip install pyfiglet rainbowtext colorama')
        from pyfiglet import figlet_format
        from rainbowtext import text
        from colorama import init

    init()
    os.system('clear')
    r = '\033[1;31m'
    g = '\033[32;1m'
    y = '\033[1;33m'
    w = '\033[1;37m'

    figleted = [figlet_format("Yusuf", font=font) for font in ['slant', 'banner', 'digital', 'devilish', 'diamond', 'arrows', 'heavy_me', 'epic', 'banner4', 'banner3-D', 'zig_zag_', 'banner3', 'shadow']]

    banner = text(random.choice(figleted) + '\n' +
                  '========================================\n' +
                  '|            Author: Monxter RuLex             |\n' +
                  '|  Python File Encoder & Obfuscator    |\n' +
                  '|    Github: github.com/athra-302      |\n' +
                  '|    Facebook: facebook.com/Tʜe'w Moŋxtɘr Insııdə    |\n' +
                  '========================================')
    print(banner)

    print(g)
    file_path = input('Please enter Python file path (example: src/file.py): ')
    if not file_path.endswith('.py'):
        print(f'{r}ERR: Please enter a .py file!')
        return

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            name = file_path.replace('.py', '')
    except IOError:
        print(f'{r}ERR: {y}No such file or directory')
        time.sleep(5)
        return

    try:
        compiled_file = compile(file_content, '', 'exec')
        encoded_code = marshal.dumps(compiled_file)
    except TypeError:
        print(f'{r}-ERR: {w}File already compiled!!!')
        time.sleep(5)
        return

    with open(f'{name}_encoded.py', 'w') as ofile:
        ofile.write('#Encoded by Yusuf\n#My Github: https://github.com/Yusufhere\n')
        ofile.write('import marshal\n')
        ofile.write('exec(marshal.loads(' + repr(encoded_code) + '))')
    
    print(f'{g}+{y}Success!!\nEncoded file saved in {r}{name}_encoded.py')
    time.sleep(5)

def facebook_message_bomber():
    os.system('clear')

    def send_message(token, message, target_id):
        url = f"https://graph.facebook.com/v21.0/t_{target_id}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ("Mozilla/5.0 (Linux; Android 14; Samsung Galaxy S23 Ultra (SM-S918B) Build/S918BXXU7CXK4; wv) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.135.125 Mobile Safari/537.36"),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
            "Referer": "www.google.com",
        }
        parameters = {
            "to": {"id": target_id},
            "message": message
        }
        try:
            response = requests.post(url, json=parameters, headers=headers)
            response.raise_for_status()
            print(Fore.GREEN + f"╰┈➤✦《 「꧁༒☠💥✨𝐀𝐓𝐓𝐀𝐂𝐊𝐈𝐍𝐆 𝟎𝐍 𝐓𝐀𝐑𝐆𝐄𝐓✨💥☠༒꧂」 ✦》────────────────────────────────────જ⁀➴")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[x] Error: {e}")

    banner = """
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
               💣𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙈𝙀𝙎𝙎𝘼𝙂𝙀 𝘽𝙊𝙈𝘽𝙀𝙍💣
                    💻𝙑𝙀𝙍𝙎𝙄𝙊𝙉 1.0💻
                   👑𝘼𝙐𝙏𝙃𝙊𝙍 {𝙈𝙊𝙉𝙓𝙏𝙀𝙍}👑
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    """

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN]
    print(Fore.MAGENTA + "\U0001F600" + " Dhanyavaad!")
    for line in banner.split('\n'):
        for i, char in enumerate(line):
            print(colors[i % len(colors)] + char, end='')
        print()
    print(Fore.RESET)

    def main():
        print("\033[38;5;201mW3LC0M3 \033[38;5;196mT00 \033[38;5;202mYU5UF \033[38;5;226mM3SS9G3 \033[0m \033[38;5;201mB0MB3R \033[38;5;196mT00L \033[38;5;202mB0MB3R \033[38;5;226m3NJ0Y \033[0m")
        print(Fore.CYAN + "-------------------------------------------------->")
        tokens_file = input(Fore.YELLOW + "꧁.💕EᑎTEᖇ TOKEᑎ ᖴIᒪᗴ💖.꧂: ").strip()
        print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
        target_id = input(Fore.YELLOW + "🔥(✖EᑎTEᖇ TᗩᖇGET Iᗪ✖)🔥: ").strip()
        print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
        messages_file = input(Fore.YELLOW + "꧁༒☠💥✨EᑎTEᖇ ᗰEᔕᔕᗩGE ᖴIᒪᗴ✨💥☠༒꧂: ").strip()
        print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
        haters_name = input(Fore.YELLOW + "▄︻テEᑎTEᖇ ᕼᗩᖇᗴᖇ ᑎᗩᗰᗴ══━一💥: ").strip()
        print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
        speed = float(input(Fore.YELLOW + "꧁༒☠💥✨EᑎTEᖇ ᔕᑭEEᗪ✨💥☠༒꧂: ").strip())
        print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)

        try:
            with open(messages_file, "r") as file:
                messages = file.readlines()
            with open(tokens_file, "r") as file:
                tokens = file.readlines()
        except IOError as e:
            print(Fore.RED + f"File error: {e}")
            return

        while True:
            for message_index, message in enumerate(messages):
                token_index = message_index % len(tokens)
                token = tokens[token_index].strip()
                full_message = f"{haters_name} {message.strip()}"
                send_message(token, full_message, target_id)
                time.sleep(speed)
            print(Fore.CYAN + "\n[+] ✎ (❁ᴗ͈ˬᴗ͈) ༉‧ 『R』『E』『S』『T』『A』『R』『T』『I』『N』『G』 ♡*.✧...\n")

    if __name__ == "__main__":
        main()

def about():
    os.system('clear')

    def print_banner():
        banner = pyfiglet.figlet_format("About Us", font="slant")
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)

    def print_about():
        clear_screen()
        print_banner()
        print(Fore.YELLOW + "***************************************" + Style.RESET_ALL)
        print(Fore.CYAN + "*            𝐕𝐞𝐫𝐬𝐢𝐨𝐧 𝟏.𝟓            *" + Style.RESET_ALL)
        print(Fore.YELLOW + "***************************************" + Style.RESET_ALL)

        print(Fore.MAGENTA + "𝘠𝘶𝘴𝘶𝘧'𝘴 𝘞𝘰𝘳𝘭𝘥 𝘪𝘴 𝘢 𝘗𝘺𝘵𝘩𝘰𝘯-𝘣𝘢𝘴𝘦𝘥 𝘵𝘰𝘰𝘭 𝘵𝘩𝘢𝘵 𝘱𝘳𝘰𝘷𝘪𝘥𝘦𝘴 𝘧𝘪𝘭𝘦 𝘦𝘯𝘤𝘰𝘥𝘪𝘯𝘨, 𝘥𝘢𝘵𝘢 𝘰𝘣𝘧𝘶𝘴𝘤𝘢𝘵𝘪𝘰𝘯, 𝘢𝘯𝘥 𝘱𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘨𝘦𝘯𝘦𝘳𝘢𝘵𝘪𝘰𝘯 𝘴𝘦𝘳𝘷𝘪𝘤𝘦𝘴." + Style.RESET_ALL)

        print("\n" + Fore.GREEN + "𝐎𝐮𝐫 𝐓𝐞𝐚𝐦:" + Style.RESET_ALL)
        print(Fore.CYAN + "𝙼𝚘𝚗𝚡𝚝𝚎𝚛 - 𝙵𝚘𝚞𝚗𝚍𝚎𝚛 & 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛" + Style.RESET_ALL)
        print(Fore.CYAN + "Facebook: facebook.com/Tʜe'w Moŋxtɘr Insııdə" + Style.RESET_ALL)
        print(Fore.CYAN + "Github: (link unavailable)" + Style.RESET_ALL)

        print("\n" + Fore.GREEN + "Ｏｕｒ Ｓｅｒｖｉｃｅｓ:" + Style.RESET_ALL)
        print(Fore.CYAN + "𝘍𝘪𝘭𝘦 𝘦𝘯𝘤𝘰𝘥𝘪𝘯𝘨" + Style.RESET_ALL)
        print(Fore.CYAN + "𝘍𝘢𝘤𝘦𝘣𝘰𝘰𝘬 𝘔𝘦𝘴𝘴𝘢𝘨𝘦 𝘉𝘰𝘮𝘣𝘦𝘳" + Style.RESET_ALL)
        print(Fore.CYAN + "𝘏𝘢𝘵𝘦𝘳 𝘕𝘢𝘮𝘦 𝘔𝘢𝘬𝘦𝘳" + Style.RESET_ALL)

        print("\n" + Fore.GREEN + "Our Vision:" + Style.RESET_ALL)
        print(Fore.CYAN + "To prioritize the security and privacy of your data." + Style.RESET_ALL)
        print(Fore.CYAN + "To provide easy-to-use and effective tools." + Style.RESET_ALL)

        print("\n" + Fore.YELLOW + "🐠  🎀  𝒯𝒽𝒶𝓃𝓀 𝒴💍𝓊❣  🎀  🐠" + Style.RESET_ALL)
        print(Fore.YELLOW + "***************************************" + Style.RESET_ALL)
        print(Fore.GREEN + "𝙋𝙧𝙚𝙨𝙨 𝙀𝙣𝙩𝙚𝙧 𝙩𝙤 𝙜𝙤 𝙗𝙖𝙘𝙠 𝙩𝙤 𝙩𝙝𝙚 𝙢𝙖𝙞𝙣 𝙢𝙚𝙣𝙪." + Style.RESET_ALL)
        input()

    print_about()

def haters_name_maker():
    import colorama
    from colorama import Fore, Back, Style
    import pyfiglet
    import os

    colorama.init()
    os.system('clear')

    def create_clip(server_runner, hater_name):
        clip = f"""
{Back.GREEN}{Fore.BLACK}
HN 1. || ♠️♦️|| 3:) 𝙇𝙀𝙂𝙀𝙉𝘿 {server_runner} 𝙄𝙎 𝙃𝙀𝙍𝙀 ❤️‍🔥 || ♦️♠️ ||  𝘈𝘓𝘓 ||𝘕𝘐𝘒𝘒𝘌 || 𝘎𝘜𝘔𝘕𝘈𝘈𝘔 || 𝘛𝘈𝘛𝘛𝘌 || 𝘓𝘈𝘎𝘖 || 𝘓𝘐𝘕𝘌 || 𝘔𝘌 || ✓ <----------------------> {hater_name} + 𝘼𝙇𝙇 - 𝘼𝘼𝙏𝙐 - 𝙅𝙃𝘼𝙏𝙐 - 𝙃𝙀𝙇𝙋𝙀𝙍𝙎 -  𝙆𝙄 - 𝙂𝘼𝘼𝙉𝘿 - 𝙆𝙊 - 𝘼𝙋𝙉𝙀 - 𝙇𝙀𝙂𝙀𝙉𝘿𝘼𝙍𝙔 - 𝙇𝙊𝘿𝙀 - 𝙋𝘼𝙍 - 𝙍𝘼𝙆𝙃 - 𝙆𝙀 - 𝘾𝙃𝙀𝙀𝙍 - 𝘿𝙀𝙉𝙀 - 𝙒𝘼𝙇𝘼 - || ♦️♠️ || {server_runner} - 𝙊𝙉 - 𝙏𝘼𝘽𝘼𝙃𝙄 || ♠️♦️ ||>>> {hater_name}

HN 2. ♠♥ || ⫷ {server_runner} 0𝐍 𝐓𝐀𝐁𝐀𝐇𝐈 𝐒𝐄𝐑𝐕𝐄𝐑 0𝐍 ⫸ || ♠♥  [[= 𝐉𝐇𝐀𝐓-  {hater_name} 𝐆𝐀𝐀𝐍𝐃𝐔 + 𝐀𝐋𝐋 𝐇𝐄𝐋𝐏𝐄𝐑  𝐍𝐀𝐌𝐀𝐊  𝐂𝐇𝐔𝐃𝐄 𝐇𝐔𝐘𝐄 𝐓𝐀𝐓𝐓𝐄 <<======>> <(") TUM9R|| ^^^ GH9R ^^^ K|| BH^N0 K0 CH0DN3 ^^^ W9L9 ^^^= [[  {server_runner} ON FIRE ]]= H3R3 <(") 3:) <3 8) ^!!^ <(") 4^M '-,-'  7^H=3 :D G(=+ R3 '-,-' 4  7 '-,-'  ^3^^ <(") ^5=7 '-,-'  ^W=4^ <(") ^R  R^ <(")  <(") ^!!^ <(") 73 '-,-' C  ^ <(") ^7^ <(")  ^R^U^ <(") (=+  =L '-,-' 4 :D ^5^ <3 '-,-' ^!!^ =5 '-,-' H '-,-' ^ <(") 3  '-,-' R=^ <(")  3 '-,-' <(") <3 :D =]] <3 :D ||> ___ <3 <3 :D :D (^^^) :P 3:) ]] {hater_name} KI GAAND MAARNE WAALA [[[ {server_runner} 𝐇𝐄𝐑𝐄]]] > {hater_name}

HN 3. <(("))> <3 3^9 <(^^^)> <3 '-,-' |< <3 <(("))> <3 3 '-,-' <(("))> <3 '-,-' <3 <(^^^)> '-,-' <3 | <(("))> W <3 |) <(("))> 3 <3 '-,-' (^^^) <3 '-,-' 7 <3 <(("))> !! <3 M <(("))> 4 <3 '-,-' |< <(("))> <3 '-,-' (^^^) ( |-| <(("))> <3 |) ^7 <(("))> 4 <3 (^^^) '-,-' <3 <(("))> <3 4^ |_| <3 <(("))> 5^4 <3 <(^^^)> <3 | 3 <(("))> '-,-' <3 ( |-| <(("))> 4 <3 M <(("))> 4 '-,-' <3 <(^^^)> <3 2 '-,-' <(") <(("))> <(") '-,-' <3 <(("))> <(") '-,-' 7 (=_=) 2 ^ !! <(("))> () <3 =D (Y) :D [[-------____ {hater_name} (^_^) K!!!DX ( _!!_ ) P4^R^ ____------]] <3 [[[ {server_runner} <09> F^!!R3]]]  (Y) :V 3:) ♥ =D <('') {hater_name}

HN 4. [[♥️_♥ {server_runner} 𝙃3𝙍3 =𝘿  {hater_name} +  𝘼𝙇𝙇 𝙃3𝙇𝙋3𝙍𝙎 𝙇𝙐𝙉𝘿 𝙋3 <(") ♥️_♥️]] :𝙋 :𝙊 [] •• [] (𝙔) - 3:) - <(") - <3 - 𝘽) [] •• []^[] •• []^[] •• []^[] •• []^[] •• [] (𝙔) - 3:) - <(") - <3 - :𝙋 [] •• []^[] •• []^[] •• []^[] •• []^[] •• []^[] :𝙥 - :𝘿 - <3 (𝙐𝙇𝙏𝙈4𝙏3𝘿••𝙓𝘿••𝙎𝙋33𝘿­) []••[] (𝙔) - 3:) - (^^^) - (^^^) - 𝘽) []••[] (𝙔) - 3:) - (^^^) - (^^^) - 𝙊:) []••[] (𝙔) - 3:) - <(") - <3 - :𝙋 - 𝘽) (𝙔) - 909 - 570𝙋 - 𝙓|) <3  ;) - 𝘽) (𝙔) 4𝙇0𝙉3 𝙎𝙏4𝙉𝘿 > {server_runner} - 𝙊𝙉- 𝘿𝙄𝙎𝙏𝙍𝙐𝘾𝙏𝙄𝙊𝙉  - <3😀❤👍 {hater_name}

HN 5. 𝙉09𝙎70𝙋_𝙏9𝘽9𝙃𝙄𝙄__𝙋 :𝙋 :𝙋 :𝙋 :𝙋  =𝙋 ] =𝘿 ] =𝙋 ] =𝙋 ] =𝙋 ] =𝘿 ] =𝘿 ] =|| =𝘿 ] =𝘿 ] [^^] [<|>] =𝘿  𝙃𝘼𝙏𝙀𝙍𝙎 {hater_name} /𝙆𝙄💋𝘽𝙃3𝙉 𝙆𝙄 𝘾𝙃𝙐𝙏𝙏💋𝙈9𝙍𝙉3 𝙒9𝙇9 𝙃9𝙍9𝙈𝙄𝙄💋𝘽𝙊𝙔 ] =𝙋 ] =𝘿 ] =𝘿 ] =𝘿 =𝘿 ] =𝘿 ] :𝙋 :𝙋 =𝘿 <3 <3 <3 <3 :] :] :[ :[ :[ :𝙋 (𝙔) (𝙔) (𝙔) (𝙔) (𝙔) (𝙔)  =𝘿 =𝘿 =𝘿 =𝘿 =𝘿  𝘽| 𝘽| 𝘽| (^^^) =𝘿  [ =𝘿 ] [ =𝘿 ] [ =𝙋 ] [ =𝘿 ] [ =𝘿 ] [ ^__^ ] (( =𝙋 )) (( ? )) (( =𝘿) (( =𝘿 )) (( :3__(( =𝘿 ))<<3____𝙐.𝙉.5.7.0.𝙋.𝙋,4.𝘽.𝙇.3____𝙇,3.𝙂.3.𝙉.𝘿.𝙎.]][ #__𝘿9𝙉𝙂3𝙍𝙊𝙐𝙎__𝘽𝙊𝙔__{server_runner}__𝙄𝙉𝙎𝙄𝙄𝘿3 ]]]_______<3 <3  =𝘿 <3 <3 (^^^) (^^^) {hater_name}

HN 6. #___R9ND11__K3 (Y) (Y) (•) S9L3 S9D3 HU3 K3 P9DISH:-(T3R|| M99 K9 B|-|0XD9 F9D D|_|N B3 L0WD3 K3 B(|3=]] :D#___R9ND11__K3 (Y) (Y) (•) F33L KRT444 J444 MU9994 T3R1 BH39 K0 CH0DU9(✌#__{server_runner}__JUST_N0NST0P_T9B9H1 <3 3:) =]] < 3 = D {hater_name}

HN 7. [[ B) 𝐊𝐔𝐓𝐓𝐄 - 𝐉𝐇𝐔𝐍𝐃 - 𝐌𝐄 - 𝐀𝐀𝐓𝐄 - 𝐇𝐀𝐈𝐍 - 🦁 𝐒𝐇𝐄𝐑 - 𝐀𝐊𝐄𝐋𝐀 - 𝐀𝐀𝐓𝐀 - 𝐇𝐀𝐈 🔥 <<<<<< [[[[ {server_runner} 𝙄𝙎 𝙃𝙀𝙍𝙀 ;P 𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 💪🏻 𝙊𝙁 𝙔𝙊𝙐𝙍 𝘿𝘼𝘿 👿]]]](_(--{server_runner} 𝙊𝙉 𝙏𝘼𝘽𝘼𝙃𝙄--)_)_**𝙃𝙀𝙇𝙋𝙀𝙍 🤣 𝙆𝙄 𝙈𝘼 🆓𝙁𝙍𝙀𝙀🆓 𝙈𝙀 🫣 𝘾𝙃𝙐𝘿𝙄**__ :) <3 #{hater_name}_𝙋𝙞𝙞𝙡𝙡3 __((!!"!!)__𝙏(3)𝙍!!__|| 𝘽"3"|-|"3"!!!! ||__ = [𝙆!!] = __((!!"!!))__-//- 𝙆|-|33𝙉𝘾|-| -||-__ <3 :) __((!!"!!)) <3 :) 𝙇(𝙐)𝙉𝙂9 <(") - 3:) || 𝙈9!)9𝙍𝘾|-|0!) "" = 𝙆3 = "" 𝘽[[9]]𝘾𝘾"|-|"3" * __ (("!!")) << || 𝙎(9)𝙇'3 || >> <3 :) 𝙅|-|[9]𝙏 * = 𝙆3 = * (( : ~ 𝘽99𝙇~ : ))___*******𝘽𝘼𝘾𝙃𝘼 ^^^𝙎𝘼𝙆𝙊]]  𝙏𝙊𝙃 ? [[𝘽𝘼𝘾𝙃𝘼 ✓ 𝙆𝙀 [[𝘿𝙄𝙆𝙃𝘼𝙊]] 𝙈𝙀𝙍𝙀^^^ 𝙇𝘼𝙉𝘿]] 𝙆𝙀 𝙒𝘼𝙍] 𝙎𝙀 [[𝘼𝙋𝙉𝙄 𝘽𝙀𝙃𝙉𝙊]] 𝙆𝙊******_______<[[:~𝙏𝙃"3 "" 𝘿𝙄𝙄𝙎𝙏𝙍𝙐𝘾𝙏"3"𝙍 "" 𝘽0𝙄𝙄 ""😘__{server_runner} " 𝙃3𝙍3 " 3:) <("){hater_name}

{Style.RESET_ALL}
"""
        print(clip)

    def main():
        banner()
        server_runner = input(f"{Fore.GREEN}𝐒𝐄𝐑𝐕𝐄𝐑 𝐇𝐄𝐑𝐎: {Style.RESET_ALL}")
        hater_name = input(f"{Fore.GREEN}𝐇𝐀𝐓𝐄𝐑 𝐍𝐀𝐌𝐄: {Style.RESET_ALL}")
        custom_server_runner = custom_font(server_runner)
        custom_hater_name = custom_font(hater_name)
        create_clip(custom_server_runner, custom_hater_name)
        input(Fore.GREEN + "𝙋𝙧𝙚𝙨𝙨 𝙀𝙣𝙩𝙚𝙧 𝙩𝙤 𝙜𝙤 𝙗𝙖𝙘𝙠 𝙩𝙤 𝙩𝙝𝙚 𝙢𝙖𝙞𝙣 𝙢𝙚𝙣𝙪." + Style.RESET_ALL)

    main()

def custom_font(text):
    font_map = {
        'A': '𝘼', 'B': '𝘽', 'C': '𝘾', 'D': '𝘿', 'E': '𝙀',
        'F': '𝙁', 'G': '𝙂', 'H': '𝙃', 'I': '𝙄', 'J': '𝙅',
        'K': '𝙆', 'L': '𝙇', 'M': '𝙈', 'N': '𝙉', 'O': '𝙊',
        'P': '𝙋', 'Q': '𝙌', 'R': '𝙍', 'S': '𝙎', 'T': '𝙏',
        'U': '𝙐', 'V': '𝙑', 'W': '𝙒', 'X': '𝙓', 'Y': '𝙔',
        'Z': '𝙕',
        'a': '𝙖', 'b': '𝙗', 'c': '𝙘', 'd': '𝙙', 'e': '𝙚',
        'f': '𝙛', 'g': '𝙜', 'h': '𝙝', 'i': '𝙞', 'j': '𝙟',
        'k': '𝙠', 'l': '𝙡', 'm': '𝙢', 'n': '𝙣', 'o': '𝙤',
        'p': '𝙥', 'q': '𝙦', 'r': '𝙧', 's': '𝙨', 't': '𝙩',
        'u': '𝙪', 'v': '𝙫', 'w': '𝙬', 'x': '𝙭', 'y': '𝙮',
        'z': '𝙯'
    }
    result = ""
    for char in text:
        if char.isalpha():
            result += font_map[char]
        else:
            result += char
    return result

def banner():
    unicode_banner = """ ꧁༒︎Y_U_S_U_F_ _H_A_T_E_R_S_ _N_A_M_E_ _M_A_K_E_R_ _T_O_O_L_ ༒︎꧂ """
    print(f"{Fore.RED}{unicode_banner}{Style.RESET_ALL}")
    
def np_finder():
    colorama.init()

def find_txt_files():
    os.system("clear")
    print(Fore.CYAN + Style.BRIGHT + """ 
    ▀█▀ █▀▀   ▀█▀ █▀█ █▀█ █░░ █▀ 
    ░█░ █▄█   ░█░ █▄█ █▄█ █▄▄ ▄█ 
    "This tool finds the (np folder) in your phone storage and gives the location of the txt files in it. To use it, create an np folder in your phone storage and add txt files to it. and get the location of all at once" 
    """)
    print(Style.RESET_ALL)

    folder_name = "NP"
    storage_path = "/storage/emulated/0"
    folder_path = os.path.join(storage_path, folder_name)

    def find_txt_files(path):
        txt_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    txt_files.append(os.path.join(root, file))
        return txt_files

    if os.path.exists(folder_path):
        txt_files = find_txt_files(folder_path)
        if txt_files:
            print(Fore.CYAN + Style.BRIGHT + "TXT file ki location:")
            for file in txt_files:
                print(Fore.MAGENTA + file)
            print()
        else:
            print(Fore.RED + "Koi TXT file nahi mila.")
            
    else:
        print(Fore.RED + "Folder nahi mila.")
        print(Style.RESET_ALL)
    

def main_menu():
    authenticate()  # Call the authentication function
    while True:
        print_banner()
        print_menu()
        choice = input("𝙒𝙝𝙖𝙩 𝙬𝙤𝙪𝙡𝙙 𝙮𝙤𝙪 𝙡𝙞𝙠𝙚 𝙩𝙤 𝙙𝙤? (𝙀𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙘𝙝𝙤𝙞𝙘𝙚): ")

        if choice == "1":
            file_encoder()
        elif choice == "2":
            facebook_message_bomber()
        elif choice == "3":
            about()
        elif choice == "4":
            haters_name_maker()
        elif choice == "5":
            np_finder()
        elif choice == "6":
            print(Fore.BLUE + Style.BRIGHT + "꧁.💕G͎o͎o͎d͎b͎y͎e͎💖.꧂!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐜𝐡𝐨𝐢𝐜𝐞. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧." + Style.RESET_ALL)
            input("𝐏𝐫𝐞𝐬𝐬 𝐄𝐧𝐭𝐞𝐫 𝐭𝐨 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐞...")

if __name__ == "__main__":
    main_menu()